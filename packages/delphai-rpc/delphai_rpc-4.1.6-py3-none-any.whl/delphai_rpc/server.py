import aio_pika
import aio_pika.connection
import asyncio
import contextvars
import functools
import inspect
import logging
import pydantic
import socket
import time

from aio_pika.abc import (
    AbstractChannel,
    AbstractExchange,
    AbstractRobustConnection,
    AbstractQueue,
)
from typing import Any, Callable, Dict, Optional, cast

from . import errors
from . import metrics
from .connection_manager import get_connection
from .models import Request, Response
from .types import IncomingMessage, Message, Priority, RequestContext
from .utils import clean_service_name, fix_message_timestamp


logger = logging.getLogger(__name__)

request_context: contextvars.ContextVar[Optional[RequestContext]] = (
    contextvars.ContextVar("request_context", default=None)
)


class RpcServer:
    def __init__(self, service_name) -> None:
        self._service_name = clean_service_name(service_name)
        self._app_id = f"{self._service_name}@{socket.gethostname()}"

        self._handlers: Dict[str, Callable] = {}

        self._reset()

        self.bind(self._ping)
        self.bind(self._help)

    def _reset(self) -> None:
        self._connection: Optional[AbstractRobustConnection] = None
        self._channel: Optional[AbstractChannel] = None
        self._exchange: Optional[AbstractExchange] = None
        self._queue: Optional[AbstractQueue] = None

    def bind(
        self, handler: Optional[Callable] = None, *, name: Optional[str] = None
    ) -> Callable:
        """
        Binds to be exposed handlers (functions) to RPC server instance:

        @server.bind
        def add(*, a: float, b: float) -> float:
            ...

        # or

        def sub(*, a: float, b: float) -> float:
            ...

        server.bind(sub)

        # or

        @server.bind(name="mul")
        def multiply(*, a: float, b: float) -> float:
            ...

        """

        def decorator(handler):
            self._bind_handler(handler=handler, name=name)
            return handler

        return decorator(handler) if handler else decorator

    def _bind_handler(self, *, handler: Callable, name: Optional[str] = None) -> None:
        handler_name = name or handler.__name__
        if handler_name in self._handlers:
            raise KeyError(f"Handler {handler_name} already defined")

        if hasattr(handler, "raw_function"):
            # Unwrap `pydantic.validate_call` decorator
            handler = handler.raw_function

        self._validate_handler(handler)

        self._handlers[handler_name] = pydantic.validate_call(validate_return=True)(
            handler
        )

    def _validate_handler(self, handler: Callable) -> None:
        if not inspect.iscoroutinefunction(handler):
            raise TypeError("Handlers must be coroutine functions")

        positional_only = []
        positional_or_keyword = []

        for parameter_name, parameter in inspect.signature(handler).parameters.items():
            if parameter.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD:
                positional_or_keyword.append(parameter_name)

            elif parameter.kind in [
                inspect.Parameter.POSITIONAL_ONLY,
                inspect.Parameter.VAR_POSITIONAL,
            ]:
                positional_only.append(parameter_name)

        if positional_only:
            raise TypeError(
                "{} has positional-only parameters {} that are not supported in {}".format(
                    handler,
                    positional_only,
                    self.__class__,
                )
            )

        if positional_or_keyword:
            logger.warning(
                "%s has positional parameters %s, only keyword parameters are supported in %s",
                handler,
                positional_or_keyword,
                self.__class__,
            )

    async def start(self, connection_string: str, prefetch_count: int = 1) -> None:
        if self._connection:
            raise RuntimeError("Already started")

        connection = self._connection = await get_connection(
            connection_string, self._service_name
        )
        channel = self._channel = await connection.channel()
        await channel.set_qos(prefetch_count=prefetch_count)

        exchange = self._exchange = await channel.declare_exchange(
            name=f"service.{self._service_name}",
            type=aio_pika.ExchangeType.TOPIC,
            durable=True,
        )

        queue = self._queue = await channel.declare_queue(
            name=f"service.{self._service_name}",
            durable=True,
            arguments={
                "x-max-priority": max(Priority),
                "x-dead-letter-exchange": f"service.{self._service_name}.dlx",
            },
        )

        await queue.bind(exchange, "#")
        await queue.consume(fix_message_timestamp(self._on_message))

        logger.info("RPC server is consuming messages from `%s`", queue)

    async def stop(self) -> None:
        channel = self._channel
        if channel:
            self._reset()
            await channel.close()

    async def serve_forever(
        self, connection_string: str, prefetch_count: int = 1
    ) -> None:
        await self.start(connection_string, prefetch_count=prefetch_count)
        try:
            await asyncio.Future()
        finally:
            await self.stop()

    async def _on_message(self, message: IncomingMessage) -> None:
        consumed_timestamp = time.time()

        logger.debug(
            "[MID:%s] Got `%s` message from `%s` service",
            message.message_id,
            message.type or "[untyped]",
            message.app_id or "unknown",
        )

        message_consumed = functools.partial(
            metrics.message_consumed,
            exchange=message.exchange,
            routing_key=message.routing_key,
            type=message.type,
            priority=message.priority,
            redelivered=message.redelivered,
            payload_size=message.body_size,
        )

        if message.type != "rpc.request":
            logger.warning(
                "[MID:%s] Unexpected message type: `%s`",
                message.message_id,
                message.type,
            )
            await message.reject()
            message_consumed(error="WRONG_MESSAGE_TYPE")
            return

        if message.reply_to and not message.correlation_id:
            logger.warning("[MID:%s] `correlation_id` is not set", message.message_id)
            message_consumed(error="NO_CORRELATION_ID")
            await message.reject()
            return

        published_timestamp = None
        if message.timestamp:
            published_timestamp = message.timestamp.timestamp()

        deadline = None
        if published_timestamp and message.expiration:
            deadline = published_timestamp + cast(float, message.expiration)

        request_context.set(
            RequestContext(
                deadline=deadline,
                priority=Priority(message.priority or 0),
            )
        )

        try:
            response = await asyncio.wait_for(
                self._process_message(message, consumed_timestamp, published_timestamp),
                timeout=(deadline - time.time()) if deadline else None,
            )
        except asyncio.TimeoutError:
            logger.info(
                "[MID:%s] [CID:%s] Execution of `%s` from `%s` service timed out",  # noqa: E501
                message.message_id,
                message.correlation_id,
                message.type,
                message.app_id or "unknown",
            )

            await message.ack()
            message_consumed(error="TIMEOUT")
            return

        if message.reply_to:
            response_message = Message(
                body=response,
                app_id=self._app_id,
                priority=message.priority,
                correlation_id=message.correlation_id,
                expiration=(deadline - time.time()) if deadline else None,
                type="rpc.response",
            )

            await message.channel.basic_publish(
                body=response_message.body,
                routing_key=message.reply_to,
                properties=response_message.properties,
            )
            metrics.message_published(
                exchange="",
                routing_key="",  # random, causes high cardinality metric
                type=response_message.type or "",
                priority=response_message.priority or 0,
                payload_size=response_message.body_size,
            )

        await message.ack()
        message_consumed()

        logger.debug(
            "[MID:%s] [CID:%s] Handled `%s` from `%s` service, success: %s",  # noqa: E501
            message.message_id,
            message.correlation_id,
            message.type,
            message.app_id or "unknown",
            response.error is None,
        )

    @Response.wrap_errors
    async def _process_message(
        self,
        message: IncomingMessage,
        consumed_timestamp: float,
        published_timestamp: Optional[float],
    ) -> Response:
        request = Request.model_validate_message(message)

        timings = request.timings
        queued_for = None
        if published_timestamp is not None:
            timings.append(("queue.published", published_timestamp))
            queued_for = consumed_timestamp - published_timestamp

        timings.append((f"queue.consumed by {self._app_id}", consumed_timestamp))

        with metrics.server_requests_in_progress.labels(
            method=request.method_name
        ).track_inprogress():
            elapsed = -time.perf_counter()
            response = await self._process_request(request)
            elapsed += time.perf_counter()
        timings.append(("execution.completed", consumed_timestamp + elapsed))

        response.context = request.context
        response.timings = timings

        metrics.server_request_processed(
            priority=message.priority or 0,
            method=request.method_name,
            error=response.error,
            queued_for=queued_for or 0,
            elapsed=elapsed,
        )

        logger.info(
            "[MID:%s] Processed `%s` from `%s` service to method `%s`. In queue: %ims, execution: %ims, success: %s%s",
            message.message_id,
            message.type,
            message.app_id or "unknown",
            request.method_name,
            (None if queued_for is None else max(queued_for * 1000, 0)),
            elapsed * 1000,
            response.error is None,
            (f", error: {response.error.message}" if response.error else ""),
        )

        return response

    @Response.wrap_errors
    async def _process_request(self, request: Request) -> Response:
        handler = self._handlers.get(request.method_name)
        if handler is None:
            raise errors.UnknownMethodError(request.method_name)

        try:
            result = await handler(**request.arguments)
        except Exception as error:
            raise errors.ExecutionError(repr(error))

        if isinstance(result, pydantic.BaseModel):
            result = result.model_dump()

        return Response(result=result)

    async def _ping(self) -> None:
        return None

    async def _help(self) -> Dict[str, Any]:
        """
        Returns methods list
        """
        return {
            "methods": [
                {
                    "method_name": method_name,
                    "signature": f"{method_name}{inspect.signature(handler)}",
                    "description": handler.__doc__,
                }
                for method_name, handler in self._handlers.items()
            ]
        }
