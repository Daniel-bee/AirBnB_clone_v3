#!/usr/bin/python3
"""Index view file """
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def index():
    """Returns a JSON """
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def stats():
    """counts the number:
    of objects in each class
    """
    dict_ = {}
    for value in storage.all().values():
        key = '{}s'.format(value.__class__.__name__.lower())
        dict_[key] = storage.count(value.__class__)
    return jsonify(dict_)
