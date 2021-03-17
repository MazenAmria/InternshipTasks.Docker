#!/bin/python3

from flask import Flask, jsonify
from stats_collector import *
import logging
import psutil
app = Flask(__name__)

logging.basicConfig()

@app.route("/cpu/current")
def get_currnet_cpu_stats():
  res = collect_cpu_stats()
  return jsonify(res)

@app.route("/memory/current")
def get_currnet_mem_stats():
  res = collect_memory_stats()
  return jsonify(res)

@app.route("/disk/current")
def get_currnet_disk_stats():
  res = collect_disk_stats()
  return jsonify(res)

if __name__ == "__main__":
  app.run()
