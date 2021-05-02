#! /usr/bin/python3

import os
from db_connector import DBConnector
import json
from tracer import trace
import logging
import paramiko

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@trace(logger)
def collect_stats(resource=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        os.getenv("HOST"),
        username=os.getenv("HOST_USER"),
        password=os.getenv("HOST_PASSWORD")
    )

    cmd = "python /opt/stats_collector.py"
    stdin, stdout, stderr = ssh.exec_command(cmd)
    stats = json.loads(stdout.read())

    ssh.close()

    if resource is not None \
            and resource in stats.keys():
        stats = stats[resource]

    return stats


if __name__ == "__main__":
    conn = DBConnector()

    stats = collect_stats()

    for resource in stats.keys():
        conn.submit_stats(resource, stats[resource])

    conn.close()
