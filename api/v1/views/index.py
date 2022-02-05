#!/usr/bin/python3
"""Index view file """
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def index():
    """Returns a JSON """
    return jsonify({"status": "OK"})
