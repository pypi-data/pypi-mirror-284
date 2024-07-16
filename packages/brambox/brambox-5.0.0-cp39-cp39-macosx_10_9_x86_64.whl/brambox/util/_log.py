#
#   Copyright EAVISE
#   Author: Tanguy Ophoff
#
#   Logging utilities
#
import logging

__all__ = ['LogAggregator']


class LogAggregator:
    """
    Log aggregator that filters similar error messages and shows them only once.
    This tool is not meant to be used publicly, and is created to reduce the logging clutter when using the EVAL objects.
    """

    def __init__(self, msg=None, loggername='brambox'):
        self.logger = logging.getLogger(loggername)
        self.msg = msg
        self.set = set()

    def __enter__(self):
        logger = self.logger
        while logger is not None:
            for handler in logger.handlers:
                handler.addFilter(self)
            logger = logger.parent

    def __exit__(self, type, value, traceback):
        logger = self.logger
        while logger is not None:
            for handler in logger.handlers:
                handler.removeFilter(self)
            logger = logger.parent

    def filter(self, record):
        info = (record.name, record.levelno, record.getMessage())
        if info in self.set:
            return False

        self.set.add(info)
        if self.msg is not None:
            record.msg = self.msg.format(record.msg)
        return True
