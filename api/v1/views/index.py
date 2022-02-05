#!/usr/bin/python3
from api.v1.views import app_views

print("Hello World")
@app_views.route('/status')
def index():
    json = {"status": "OK"}
    return "
