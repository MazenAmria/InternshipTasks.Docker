#!/bin/python3

from functools import wraps

def trace(logger):
  def wrapper(func):
    @wraps(func)
    def logging_enabled(*args, **kwargs):
      logger.info(f" * calling {func.__name__}")
      return func(*args, **kwargs)
    return logging_enabled
  return wrapper