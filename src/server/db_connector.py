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
	assumes to deal with single database.

	Environment Variables
	---------------------
		* `DB_HOST` : the IP address of the database server machine.
		* `DB_PORT` : the port of the database server at the host machine.
		* `DB_NAME` : the name of the database to connect.
		* `DB_USER` and `DB_PASSWORD` : user credintials to access that database.
	"""
	@trace(logger)
	def __init__(self):
		self.client = MongoClient(
			host=os.getenv("DB_HOST"),
			port=int(os.getenv("DB_PORT")),
			username=os.getenv("DB_USER"),
			password=os.getenv("DB_PASSWORD"),
			authSource=os.getenv("DB_NAME")
		)
		self.db = self.client[os.getenv("DB_NAME")]

	@trace(logger)
	def close(self):
		"""Close the connection with the database
		"""
		self.client \
			.close()
		
	@trace(logger)
	def submit_stats(self, resource, stats):
		"""Submits the collected stats
		to the desired resource collection.

		Parameters
		----------
			* `resource` : the resource collection to be stored in.
			* `stats` : the object to be stored in the database.
		"""
		self.db[resource] \
			.insert_one(stats)

	@trace(logger)
	def get_stats(self, resource, n=None):
		"""Retrieve the last `n` records
		from certain resource collection in the stats database.

		Parameters
		----------
			* `resource` : the resource collection to be fetched from.
			* `n` : the number of records to be returned (default = 24).

		Return
		------
			* `list` contains the last `n` records.
		"""
		if n is None:
			n = 24
		
		return list(
			self.db[resource] \
				.find({}, {
					"_id": 0
				}) \
				.sort("_id", pymongo.DESCENDING) \
				.limit(n)
		)
