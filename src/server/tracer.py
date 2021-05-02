#! /usr/bin/python3

from functools import wraps


def trace(logger):
    """A decorator that enable logging function
    name when it's called.

    Parameters
    ----------
            * `logger`: the logging object that will
            be used to log messages.
    """
    def wrapper(func):
        @wraps(func)
        def logging_enabled(*args, **kwargs):
            logger.info(f" * calling {func.__name__}")
            return func(*args, **kwargs)
        return logging_enabled
    return wrapper
