#!/usr/bin/python3
""" main app file """
from flask import Flask, make_response, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown(exc):
    """close session"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    host_ = getenv('HBNB_API_HOST', default='0.0.0.0')
    port_ = getenv("HBNB_API_PORT", default=5000)
    app.run(host=host_, port=port_, threaded=True)
