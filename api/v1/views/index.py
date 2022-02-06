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
    of objects in each class
    """
    return jsonify({"amenities": storage.count("Amenity"),
                    "cities": storage.count("City"),
                    "places": storage.count("Place"),
                    "reviews": storage.count("Review"),
                    "states": storage.count("State"),
                    "users": storage.count("User")})
