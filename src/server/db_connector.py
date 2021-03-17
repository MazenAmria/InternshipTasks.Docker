#!/bin/python3

from tracer import trace
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

@trace(logger)
def submit_stats(stats):
  pass