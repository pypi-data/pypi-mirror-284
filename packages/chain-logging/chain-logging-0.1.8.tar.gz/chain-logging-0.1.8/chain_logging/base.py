"""
Base File of Chain Logging
"""
import inspect
import logging
import sys
import time
import typing


class ChainFilter(logging.Filter):
    """
    Chain Filter for chained logging tools

    Params:
        - log_format (str) : use `exec_id` on your format to enable unique id for each request
        - level (int) : log level (NOTSET < DEBUG < INFO < ERROR < WARNING < CRITICAL)
        - **kargs (Mapped[Any, Any]) : put your desired value to the filter
            ex:
                - logformat = [%(asctime)s][%(my_name)s][%(my_age)s] - %(message)s'
                - here `my_name` and `my_age` is a custom value to `LogRecord` object
                - applying this format to the logger would enable you to insert the value :
                    `ChainFilter(log_format, logging.INFO, my_name="joy", my_age=22)`
    """
    def __init__(
        self,
        log_format: str = '[%(asctime)s][ID:%(exec_id)s][%(filename)s:%(lineno)s][%(levelname)s] - %(message)s',
        level: int = logging.INFO,
        id_generator: typing.Optional[typing.Callable] = None,
        **kargs
    ):
        self.disabled = False
        self.level = level
        self._unapplied = ["_log_format", "_unapplied"]
        self._log_format = log_format
        self._kargs = kargs
        self._embed_attr(**kargs)
        if not callable(id_generator):
            id_generator = time.time_ns
        self._exec_id = id_generator()

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, val):
        self.__level = logging._checkLevel(val)

    @property
    def allowed_levels(self):
        """
        Allowed filter levels property

        Return:
            - levels (List[int]) : allowed levels to be logged
        """
        raw_levels = list(logging._nameToLevel.values())
        if self.level:
            levels = [lv for lv in raw_levels if lv >= self.level]
        else:
            levels = []
        return levels

    def _embed_attr(self, **kargs):
        """
        Embed the mapped key-value into to self `ChainFilter` object
        """
        if kargs:
            for key in kargs:
                if not key in self.__dict__:
                    setattr(self, key, kargs[key])

    def _apply_record_attr(self, record: logging.LogRecord):
        """
        Apply attribute from `ChainFilter` object to the log record

        Params:
            - record (logging.LogRecord)
        """
        for attr, value in vars(self).items():
            if (attr not in record.__dict__) and (attr not in self._unapplied):
                setattr(record, attr, value)
        setattr(record, "exec_id", self._exec_id)

    def filter(self, record: logging.LogRecord):
        if not self.disabled and record.levelno in self.allowed_levels:
            self._apply_record_attr(record)
            return True
        return False

    def get_child_filter(self):
        """
        Generate child filter

        Return:
            - new_chain_filter (ChainFilter)

        """
        new_chain_filter = ChainFilter(self._log_format, self.level, **self._kargs)
        return new_chain_filter

    async def get_child_filter_async(self):
        """
        Generate child filter

        Return:
            - new_chain_filter (ChainFilter)

        """
        new_chain_filter = ChainFilter(self._log_format, self.level, **self._kargs)
        return new_chain_filter


class ChainStreamer(logging.StreamHandler):
    """
    Stream Handler for `ChainLogger`

    Params:
        - filter_object (ChainFilter)
    """
    def __init__(self, filter_object: ChainFilter):
        super(ChainStreamer, self).__init__(sys.stdout)
        self._formatter = logging.Formatter(filter_object._log_format)
        self.setFormatter(self._formatter)
        self.addFilter(filter_object)
        self._filter = filter_object
        self.setLevel(self._filter.level)


class ChainLogger(logging.getLoggerClass()):
    """
    Chained Logger

    This logger is used to chain every logger used in every request in every function
    to be used the same logger with the same request id

    Params:
        - name (str)
        - filter_object (ChainFilter)
    """
    def __init__(self, name: str, filter_object: ChainFilter):
        super(ChainLogger, self).__init__(name, 0)
        self._streamer = ChainStreamer(filter_object)
        self.addHandler(self._streamer)
        self._filter = filter_object
        self.setLevel(self._filter.level)

    @property
    def _exec_id(self):
        """`_exec_id` properties. represent the request id"""
        return self._filter._exec_id

    @_exec_id.setter
    def _exec_id(self, exec_id):
        """`_exec_id` setter"""
        self._filter._exec_id = exec_id

    def disable(self):
        """disable the logger"""
        self._filter.disabled = True

    def enable(self):
        """enable the logger"""
        self._filter.disabled = False

    @property
    def time_elapsed(self):
        """
        Elapsed time in miliseconds. Measured since the logger is initiated before
        request is dispached until this properties is called.

        Every time this property is called, it will also update the elapsed time

        Return:
            - elapsed (int) : time in miliseconds with 2 decimal
        """
        elapsed = time.time_ns()-self._exec_id
        elapsed = round(elapsed/1e6, 2)
        return elapsed

    def get_child_logger(self):
        """
        Generate child logger
        """
        child_filter = self._filter.get_child_filter()
        return ChainLogger(self.name, child_filter)

    async def get_child_logger_async(self):
        """
        Generate child logger
        """
        child_filter = await self._filter.get_child_filter_async()
        return ChainLogger(self.name, child_filter)
