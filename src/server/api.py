from flask import Flask, jsonify
from db_connector import DBConnector
from stats_collector import *
import logging
import psutil
app = Flask(__name__)

logging.basicConfig()

conn = DBConnector()

@app.route("/cpu/current/")
def get_currnet_cpu_stats():
  """handler to return the current
  CPU statistics as a response.

  Path: `/cpu/current/`

  Response: `json` object contains the
  current CPU statistics.
  """
  res = collect_cpu_stats()
  return jsonify(res)

@app.route("/cpu/")
def get_cpu_stats():
  """handler to return the CPU 
  statistics for the last 24 hours.

  Path: `/cpu/`

  Response: `json` object contains a list
  of objects denoting the CPU statistics
  for the last 24 hours.
  """
  res = conn.get_cpu_stats()
  return jsonify(res)

@app.route("/memory/current/")
def get_currnet_mem_stats():
  """handler to return the current
  Memory statistics as a response.

  Path: `/memory/current/`

  Response: `json` object contains the
  current Memory statistics.
  """
  res = collect_memory_stats()
  return jsonify(res)

@app.route("/memory/")
def get_mem_stats():
  """handler to return the Memory 
  statistics for the last 24 hours.

  Path: `/memory/`

  Response: `json` object contains a list
  of objects denoting the Memory statistics
  for the last 24 hours.
  """
  res = conn.get_mem_stats()
  return jsonify(res)

@app.route("/disk/current/")
def get_currnet_disk_stats():
  """handler to return the current
  Disk statistics as a response.

  Path: `/disk/current/`

  Response: `json` object contains the
  current Disk statistics.
  """
  res = collect_disk_stats()
  return jsonify(res)

@app.route("/disk/")
def get_disk_stats():
  """handler to return the Disk 
  statistics for the last 24 hours.

  Path: `/disk/`

  Response: `json` object contains a list
  of objects denoting the Disk statistics
  for the last 24 hours.
  """
  res = conn.get_disk_stats()
  return jsonify(res)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
