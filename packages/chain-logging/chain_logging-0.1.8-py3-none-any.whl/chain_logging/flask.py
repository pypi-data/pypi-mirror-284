import logging
import time
import sys
import typing
from base import ChainFilter, ChainLogger, ChainStreamer
from flask import Flask, current_app, g, request, Response
from functools import wraps
from werkzeug.local import LocalProxy
from werkzeug.exceptions import HTTPException


_base_logger = None


def chain_with_parent_logger(func):
    """
    [CELERY USE ONLY]

    Chain the worker logger with the parent logger.
    Actually just bind the execution id for easier tracking

    Please add `_exec_id` keyword-arguments on your call in `<function_name>.delay(_exec_id=logger._exec_id)` to enable

    Params:
        - func (callable) : unchained celery task

    Returns:
        - wrapped_func (callable) : chained celery task
    """
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        """
        Wraps the chained celery task

        Params:
            - _exec_id (int) : parent execution id
        Returns:
            - func (callable) : chained celery task
        """
        global _base_logger

        if not "_exec_id" in kwargs:
            raise TypeError("Please add `_exec_id` keyword-arguments on your call in `<function_name>.delay(_exec_id=logger._exec_id)` to enable")

        g._logger = _base_logger
        g._logger._exec_id = kwargs.pop("_exec_id")

        return func(*args, **kwargs)

    return wrapped_func


def setup_chained_logger(
    app: Flask,
    logger: typing.Optional[ChainLogger] = None,
    before_request: typing.Optional[typing.Callable] = None,
    after_request: typing.Optional[typing.Callable] = None,
    handle_exception: bool = False
):
    """
    Setup the middleware of chained logger that has a unique request ID
    this is used to distinct each request log for each other
    so we could distinct every process

    Please setup any logger modification after setup this log
    because anything you write under root logger will be cleaned

    This setup allows you to use chained logger either from `current_app.logger` or `log_tools.logger`
    It doesn't matter what function you're running, as long as you call the logger from between
    those 2, you are actually using the same logging handler

    Params:
        - app (Flask)
        - handle_exception (bool)
    """
    global _base_logger

    if not logger:
        logger = ChainLogger(name="FlaskChainLogger", filter_object=ChainFilter())

    assert isinstance(logger, ChainLogger)
    _base_logger = logger

    # override handlers to avoid multiple channels print out the same output
    root_logger = logging.getLogger()
    root_logger.setLevel(_base_logger._filter.level)
    app.logger.handlers = _base_logger.handlers

    # applying middleware
    app.before_request(init_global_logger)

    if callable(before_request):
        app.before_request(before_request)
    else:
        def before_request_call():
            g._logger.info(f"Received {request.method} {request.path}")
        app.before_request(before_request_call)

    if callable(after_request):
        app.after_request(after_request)
    else:
        def after_request_call(response: Response):
            current_app.logger.info(f"Request done in {logger.time_elapsed}ms")
            return response
        app.after_request(after_request_call)

    if handle_exception:
        app.errorhandler(Exception)(traceback_error_logger)


def init_global_logger():
    """
    Enabling the logger `LocalProxy` to be used globally.
    Its an initiation of logger with different id that distinct each request for easier tracking
        and avoid any messy logging due to massive request

    g._logger -> will enable the `logger` to be used whenever its imported using flask's `LocalProxy`
    get_child_logger -> will return a logger with different execution id (exec_id),
        this exec_id is equals with request id where each request will only have one
        this could easily tracks the request in a server with massive request without any worries
        to get lost in track because we have the exec_id

    Child logger is used to make each request has different execution id.
    """
    global _base_logger
    g._logger = _base_logger.get_child_logger()
    current_app.logger.handlers[0] = g._logger.handlers[0]


def traceback_error_logger(error: Exception):
    """
    Log any errors before raised to `Traceback`

    Params:
        - error (Exception)

    Raises:
        - InvalidUsage: won't be logged
        - Exception: errors will be raised if catched,
            means error is not handled in code level
    """
    if isinstance(error, HTTPException):
        logger.error(f"[HTTPException] : {error}")
        return error

    logger.error(f"[TRACEBACK] : {error}")
    raise error


def get_global_logger():
    """
    Get global logger in `LocalProxy` scope

    Returns:
        - logger (ChainLogger)
    """
    global _base_logger
    if not "_logger" in vars(g):
        g._logger = _base_logger
    return g._logger


logger: ChainLogger = LocalProxy(get_global_logger)
