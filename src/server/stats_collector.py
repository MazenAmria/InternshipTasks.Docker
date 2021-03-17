#!/bin/python3

from collections import OrderedDict
from db_connector import submit_stats
from tracer import trace
import datetime
import psutil
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@trace(logger)
def collect_cpu_stats(interval=None):
  """Collects CPU statistics
  
  collected statistics
  --------------------
    * `usage_percentage` : CPU usage percentage

  Parameters
  ----------
    * `interval` : `float`
      The period of time (in seconds) to calculate
      the CPU usage percentage over.
      `0.0` or `None` values will return the
      instantanuous CPU usage percentage.

  Retruns
  -------
    * `OrderedDict` :
      an ordered dictionary containing
      the statistics of CPU.
  """
  
  return OrderedDict([
    ("usage_percentage", psutil.cpu_percent(interval))
  ])

@trace(logger)
def collect_memory_stats():
  """Collects Memory statistics
  
  collected statistics
  --------------------
    * `total` : total physical memory available.
    * `available` : the memory that can be given instantly
      to processes without the system going into swap.
      This is calculated by summing different memory
      values depending on the platform and it is supposed
      to be used to monitor actual memory usage in 
      a cross platform fashion.
    * `percent` : the percentage usage calculated as 
      `(total - available) / total * 100`
    * `used` : memory used, calculated as `total - free`
    * `free` : memory not being used at all (zeroed) 
      that is readily available; note that this doesn't 
      reflect the actual memory available (use 'available' instead)
    * `active` : memory currently in use or very 
      recently used, and so it is in RAM.
    * `inactive` : memory that is marked as not used.
    * `buffers` : cache for things like file system metadata.
    * `cached` : cache for various things.
    * `shared` : memory that may be simultaneously 
      accessed by multiple processes.

  Retruns
  -------
    * `OrderedDict` :
      an ordered dictionary containing
      the statistics of the Memory.
  """

  return psutil.virtual_memory()._asdict()

@trace(logger)
def collect_disk_stats(path="/"):
  """Collects Disk statistics
  
  collected statistics
  --------------------
    * `total` : total disk space.
    * `percent` : the percentage usage calculated as 
      `(total - free) / total * 100`
    * `used` : disk used, calculated as `total - free`
    * `free` : disk not being used.

  Parameters
  ----------
    * `path` : `str`
      the path to calculate the disk stats over,
      if not passed it will calculate the disk stats
      over the root directory `/`.

  Retruns
  -------
    * `OrderedDict` :
      an ordered dictionary containing
      the statistics of the Disk.
  """

  return psutil.disk_usage(path)._asdict()

if __name__ == "__main__":
  stats = {
    "timestamp": datetime.datetime.now(),
    "cpu_stats": collect_cpu_stats(interval=5),
    "memory_stats": collect_memory_stats(),
    "disk_stats": collect_disk_stats()
  }
  submit_stats(stats)
