#!/usr/bin/python3
"""
Create a new view for User object that
handles all default RESTFul API actions:
"""
from flask import abort, jsonify, request
from api.v1.views import app_views
from models import storage, user


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """list of all User objects: GET /api/v1/users"""
    users = storage.all(user.User).values()
    lis = []
    for value in users:
        lis.append(value.to_dict())
    return jsonify(lis)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Retrieves a User object: GET /api/v1/users/<user_id>"""
    usr = storage.get(user.User, user_id)
    if usr:
        return jsonify(usr.to_dict())
    abort(404)

@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_user(user_id):
    """Deletes a User object:: DELETE /api/v1/users/<user_id>"""
    rduser = storage.get(user.User, user_id)
    if rduser:
        storage.delete(rduser)
        storage.save()
        return jsonify({}), 200
    abort(404)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def post_user():
    """Creates a User: POST /api/v1/users"""
    if not request.json:
        abort(400, "Not a JSON")
    elif 'name' not in request.json:
        abort(400, "Missing name")
    else:
        newuser = user.User(**request.json)
        storage.new(newuser)
        storage.save()
        return jsonify(newuser.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_state(user_id):
    """Updates a State object: PUT /api/v1/users/<state_id>"""
    data = storage.get(user.User, user_id)
    if not data:
        abort(404)
    if not request.json:
        abort(400, "Not a JSON")
    else:
        for key, value in request.json.items():
            if key not in ['id', 'email', 'created_at', 'updated_at']:
                data.key = value
        storage.save()
        return jsonify(data.to_dict()), 200
