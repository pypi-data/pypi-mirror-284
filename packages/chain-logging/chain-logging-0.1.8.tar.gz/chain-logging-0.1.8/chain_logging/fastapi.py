import inspect
import logging
import sys
import time
import typing
from .base import ChainFilter, ChainLogger, ChainStreamer
from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint


async def get_chained_logger(request: Request) -> ChainLogger:
    if "_logger" not in vars(request.state).get("_state"):
        await ChainLoggerMiddleware.initiate_logger(request)
    return request.state._logger


class ChainLoggerMiddleware(BaseHTTPMiddleware):
    """
    Enable logging with unique ID for each request

    :params: before_request
    ```
    async def before_request_call(request: Request):
        # do something
        ...
    ```

    :params: after_request
    ```
    async def after_request_call(request: Request, response: Response):
        # do something
        ...
    ```
    """
    _base_logger = None

    def __init__(
        self, app: FastAPI,
        logger: typing.Optional[ChainLogger] = None,
        before_request: typing.Union[bool, typing.Callable, None] = False,
        after_request: typing.Union[bool, typing.Callable, None] = False,
    ):
        super().__init__(app)

        if not logger:
            logger = ChainLogger(name="FastAPIChainLogger", filter_object=ChainFilter())

        assert isinstance(logger, ChainLogger)
        ChainLoggerMiddleware._base_logger = logger

        if callable(before_request):
            self._before_request = before_request
            self.before_request = before_request
        else:
            async def before_request_call(request: Request):
                logger = await get_chained_logger(request)
                if self._before_request:
                    logger.info(f"Received {request.method} {request.url.path}")
            self.before_request = before_request_call
            self._before_request = before_request

        if callable(after_request):
            self._after_request = after_request
            self.after_request = after_request
        else:
            async def after_request_call(request: Request, response: Response):
                logger = await get_chained_logger(request)
                if self._after_request:
                    logger.info(f"Request done in {logger.time_elapsed}ms")
            self.after_request = after_request_call
            self._after_request = after_request

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        if inspect.iscoroutinefunction(self.before_request):
            await self.before_request(request)
        else:
            self.before_request(request)

        response = await call_next(request)

        if inspect.iscoroutinefunction(self.after_request):
            await self.after_request(request, response)
        else:
            self.after_request(request, response)
        return response

    @staticmethod
    async def initiate_logger(request: Request):
        logger = await ChainLoggerMiddleware._base_logger.get_child_logger_async()
        root_logger = logging.getLogger()
        root_logger.setLevel(ChainLoggerMiddleware._base_logger._filter.level)
        root_logger.handlers = logger.handlers
        request.state._logger = logger
