#!/usr/bin/python3
"""Index view file """
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def index():
    """Returns a JSON """
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def obj_count():
    """counts the number:
    of objects in each class"""
    classlist = []
    for value in storage.all().values():
        classlist.append(value.__class__)
    dict_ = {"amenitys": storage.count(classlist[0]),
             "cities": storage.count(classlist[1]),
             "places": storage.count(classlist[2]),
             "reviews": storage.count(classlist[3]),
             "states": storage.count(classlist[4]),
             "users": storage.count(classlist[5])}
    return jsonify(dict_)
