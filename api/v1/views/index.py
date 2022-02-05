#!/usr/bin/python3
"""Index view file """
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def index():
    """Returns a JSON """
    return jsonify({"status": "OK"})

@app_views.route('/api/vi/stats')
def obj_count():
    """counts the number of objects in each class"""
    for clss in storage.classes:
        print(jsonify({clss: storage.all.count()}))
        return
