import aio_pika.message
import functools
import logging
import msgpack
import pydantic
import zlib

from typing import Callable, Dict, Any, List, Optional, Tuple, Type, TypeVar

from . import errors


logger = logging.getLogger(__name__)


TBaseModel = TypeVar("TBaseModel", bound="BaseModel")


class BaseModel(pydantic.BaseModel):
    @classmethod
    def model_validate_message(
        cls: Type[TBaseModel], message: aio_pika.message.Message
    ) -> "TBaseModel":
        body = message.body
        if message.content_encoding == "deflate":
            try:
                body = zlib.decompress(body)
            except Exception as error:
                raise errors.ParsingError(f"Message decompression failed: `{error!r}`")

        elif message.content_encoding:
            raise errors.ParsingError(
                f"Unknown content_encoding: `{message.content_encoding}`"
            )

        if message.content_type != "application/msgpack":
            raise errors.ParsingError(
                f"Got a message with unknown content type: {message.content_type}"
            )

        try:
            return cls.model_validate(msgpack.loads(body))
        except ValueError as error:
            raise errors.ParsingError(f"Message deserialization failed: `{error!r}`")

    def model_dump_msgpack(self, **kwargs) -> bytes:
        kwargs.setdefault("exclude_defaults", True)
        return msgpack.dumps(self.model_dump(**kwargs))


class Request(BaseModel):
    method_name: str
    arguments: Dict[str, Any] = {}
    context: Optional[Any] = None
    timings: List[Tuple[str, float]] = []


class ResponseError(BaseModel):
    type: str
    message: Optional[str] = None


class Response(BaseModel):
    result: Optional[Any] = None
    error: Optional[ResponseError] = None
    context: Optional[Any] = None
    timings: List[Tuple[str, float]] = []

    @classmethod
    def wrap_errors(cls, func: Callable) -> Callable:
        @functools.wraps(func)
        async def inner(*args, **kwargs):
            try:
                response = await func(*args, **kwargs)
                if not isinstance(response, cls):
                    raise TypeError(f"Incorrect response type, got: {type(response)}")

            except errors.RpcError as error:
                response = cls(
                    error={"type": type(error).__name__, "message": error.args[0]}
                )

            except Exception as error:
                logger.exception("Unhandled error")
                response = cls(error={"type": "UnhandledError", "message": repr(error)})

            return response

        return inner
