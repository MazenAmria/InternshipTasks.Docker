#!/bin/python3

import pymongo
from pymongo import MongoClient
import os
from tracer import trace
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class DBConnector:
  """Database helper that creates a
  connection with MongoDB, insert and
  query the desired data from the DB,
  all needed parameters must be stored 
  as environment variables. The class
  assumes to deal with single collection
  in single database.

  Environment Variables
  ---------------------
    * `DB_HOST` : the IP address of the database server machine.
    * `DB_PORT` : the port of the database server at the host machine.
    * `DB_NAME` : the name of the database to connect.
    * `DB_COLLECTION` : the collection's name in that database.
    * `DB_USER` and `DB_PASSWORD` : user credintials to access that database.
  """
  @trace(logger)
  def __init__(self):
    # self.client = MongoClient(
    #   os.getenv("DB_HOST"),
    #   os.getenv("DB_PORT")
    # )
    # self.db = self.client[os.getenv("DB_NAME")]
    # self.db.authenticate(
    #   os.getenv("DB_USER"),
    #   os.getenv("DB_PASSWORD")
    # )
    # self.collection = self.db[os.getenv("DB_COLLECTION")]

    self.client = MongoClient(
      host="127.0.0.1",
      port=27017
    )
    self.db = self.client["server_monitor"]
    self.db.authenticate("admin", "admin")
    self.collection = self.db["sys_stats"]
  
  @trace(logger)
  def close(self):
    """Close the connection with the database
    """
    self.client \
        .close()
    
  @trace(logger)
  def submit_stats(self, stats):
    """Submits the collected stats
    to the collection `DB_COLLECTION`

    Parameters
    ----------
      * `stats` : the object to be stored in the database.
    """
    self.collection \
        .insert_one(stats)

  @trace(logger)
  def get_cpu_stats(self):
    """Retrieve the last 24 record
    of the CPU stats.

    Return
    ------
      * `list` contains the last 24 records
        only with the CPU stats.
    """
    return list(
      self.collection
          .find({}, {
            "_id": 0, 
            "memory_stats": 0,
            "disk_stats": 0,
            })
          .sort("timestamp", pymongo.DESCENDING)
          .limit(24)
    )

  @trace(logger)
  def get_mem_stats(self):
    """Retrieve the last 24 record
    of the Memory stats.

    Return
    ------
      * `list` contains the last 24 records
        only with the Memory stats.
    """
    return list(
      self.collection
          .find({}, {
            "_id": 0, 
            "cpu_stats": 0,
            "disk_stats": 0,
            })
          .sort("timestamp", pymongo.DESCENDING)
          .limit(24)
    )

  @trace(logger)
  def get_disk_stats(self):
    """Retrieve the last 24 record
    of the Disk stats.

    Return
    ------
      * `list` contains the last 24 records
        only with the Disk stats.
    """
    return list(
      self.collection
          .find({}, {
            "_id": 0, 
            "cpu_stats": 0,
            "memory_stats": 0,
            })
          .sort("timestamp", pymongo.DESCENDING)
          .limit(24)
    )