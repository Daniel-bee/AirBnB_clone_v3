#!/usr/bin/python3
"""Index view file """
from flask import jsonify
from api.v1.views import app_views
from models import storage
import json

@app_views.route('/status')
def index():
    """Returns a JSON """
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def obj_count():
    """counts the number:
    of objects in each class"""
    dict_ = {}
    for value in storage.all().values():
        cls = value.__class__.__name__.lower()+'s'
        dict_[cls] = storage.count(value.__class__)
    return json.dumps(dict_, indent=2)
