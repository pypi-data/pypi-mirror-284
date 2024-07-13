import logging
from logging.config import fileConfig
import os
import sys
import time
from inspect import getframeinfo, stack
from enum import IntEnum

# import time
# import random
# log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging_config.ini')
# logging.config.fileConfig(log_file_path)

# class Logger:


class LogLevel(IntEnum):
    TRACE = 1
    DEBUG = 2
    INFO = 3
    DETAIL = 4
    WARNING = 5
    ERROR = 6
    CRITICAL = 7
    NONE = 8


fileConfig(os.path.dirname(os.path.realpath(__file__))+'/logger_config.ini')
logging.Formatter.converter = time.gmtime
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
message_format = '{{{}:{}:{}}} {}'
#
#     def getLogger(cls):
#
#         return logging.getLogger()
level = LogLevel.INFO

def set_level( level_to_set: LogLevel):
    global level
    level = level_to_set

def setLevel( levelToSet: LogLevel):
    set_level(levelToSet)

def critical( exception):
    if level <= LogLevel.CRITICAL:
        this_function = getframeinfo(stack()[0][0])
        caller = getframeinfo(stack()[1][0])
        logger.critical(message_format.format(os.path.basename(caller.filename), caller.function, caller.lineno, f"{this_function.function}{10*' '}{exception}"), exc_info=exception)
        sys.exit(1)

def error( exception):
    if level <= LogLevel.ERROR:
        this_function = getframeinfo(stack()[0][0])
        caller = getframeinfo(stack()[1][0])
        if isinstance(exception, Exception):
            logger.error(message_format.format(os.path.basename(caller.filename), caller.function, caller.lineno, f"{this_function.function}{10*' '}{exception}"), exc_info=exception)
        else:
            logger.warning(message_format.format(os.path.basename(caller.filename), caller.function, caller.lineno, f"{this_function.function}{10*' '}{exception}"))

def warning( message):
    if level <= LogLevel.WARNING:
        this_function = getframeinfo(stack()[0][0])
        caller = getframeinfo(stack()[1][0])
        logger.warning(message_format.format(os.path.basename(caller.filename), caller.function, caller.lineno, f"{this_function.function}{10*' '}{message}"))


def info( message):
    if level <= LogLevel.INFO:
        this_function = getframeinfo(stack()[0][0])
        caller = getframeinfo(stack()[1][0])
        logger.info(message_format.format(os.path.basename(caller.filename), caller.function, caller.lineno, f"{this_function.function}{10*' '}{message}"))

def detail( message):
    if level <= LogLevel.DETAIL:
        this_function = getframeinfo(stack()[0][0])
        caller = getframeinfo(stack()[1][0])
        logger.info(message_format.format(os.path.basename(caller.filename), caller.function, caller.lineno, f"{this_function.function}{10*' '}{message}"))

def debug( message):
    if level <= LogLevel.DEBUG:
        this_function = getframeinfo(stack()[0][0])
        caller = getframeinfo(stack()[1][0])
        logger.debug(message_format.format(os.path.basename(caller.filename), caller.function, caller.lineno, f"{this_function.function}{10*' '}{message}"))

def trace( message):
    if level <= LogLevel.TRACE:
        this_function = getframeinfo(stack()[0][0])
        caller = getframeinfo(stack()[1][0])
        logger.debug(message_format.format(os.path.basename(caller.filename), caller.function, caller.lineno, f"{this_function.function}{10*' '}{message}"))




# ccEnter = 'enter'
# ccExit = 'exit'
# def auto_str(cls):
#     def __repr__(self):
#         return '%s(%s)' % (
#             type(self).__name__,
#             ', '.join('%s=%s' % item for item in vars(self).items())
#         )
#     __repr__ = __repr__
#     return cls

# def log_sleep(seconds):
#     if seconds > 0:
#         logger.info('going to sleep {} seconds'.format(seconds))
#         time.sleep(seconds)
#
# def log_sleep_with_backoff(baseline_sleep_seconds, n, max_sleep_seconds, with_jitter):
#     log_sleep(min(baseline_sleep_seconds * ((2 ** n) + (random.randint(0, 1000) / 1000 if with_jitter else 0)), max_sleep_seconds))
