import os
from os import popen
from db_connector import DBConnector
import json
from tracer import trace
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

@trace(logger)
def collect_stats(resource=None):
	pipe = popen(f'ssh {os.getenv("HOST_USER")}@localhost "python /opt/stats_collector.py"')
	stats = json.loads(pipe.read())

	if resource in stats.keys():
		stats = stats[resource]

	return stats


if __name__ == "__main__":
	conn = DBConnector()

	stats = collect_stats()

	for resource in stats.keys():
		conn.submit_stats(resource, stats[resource])

	conn.close()
