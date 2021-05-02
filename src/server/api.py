#! /usr/bin/python3

from flask import Flask, request, jsonify
from db_connector import DBConnector
from stats_collector import *
import logging
app = Flask(__name__)

logging.basicConfig()

conn = DBConnector()


@app.route("/current/")
def get_currnet_stats():
    """handler to return the current
    statistics of all resources
    as a response.

    Path: `/current/`

    Response: `json` object with keys as resources
    and values as objects containing the current 
    statistics of that resource.
    """

    res = collect_stats()

    return jsonify(res)


@app.route("/<resource>/current/")
def get_currnet_resource_stats(resource):
    """handler to return the current
    statistics of a certain resource
    as a response.

    Path: `/<resource>/current/`

    Response: `json` object contains the
    current statistics of the desired resource.
    """

    assert resource == request.view_args['resource']

    res = collect_stats(resource)

    return jsonify(res)


@app.route("/<resource>/")
def get_stats(resource):
    """handler to return the statistics
    of a certain resource for the last `n` hours.

    Path: `/<resource>/?n=24`

    Response: `json` object contains a list
    of objects denoting the statistics of the
    desired resource for the last `n` hours.
    """

    assert resource == request.view_args['resource']
    n = request.args.get('n', type=int)

    res = conn.get_stats(resource, n)

    return jsonify(res)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
