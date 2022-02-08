#!/usr/bin/python3
"""
    view for User objects that handles
    all default RESTFul API actions
"""
from flask import abort, jsonify, request
from api.v1.views import app_views
from models import storage, user


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_user():
    """get all Users and convert object into a valid JSON"""
    list_ = []
    for value in storage.all(user.User).values():
        list_.append(value.to_dict())
    return jsonify(list_)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user_byid(user_id):
    """If the user_id is none, raise a 404 error"""
    usr = storage.get(user.User, user_id)
    if usr:
        return jsonify(usr.to_dict())
    abort(404)


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_user_object(user_id):
    """If the User's id is none, raise a 404 error"""
    usr = storage.get(user.User, user_id)
    if not usr:
        abort(404)
    else:
        storage.delete(usr)
        storage.save()
        return jsonify({}), 200


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def post_user():
    """Creates a new User"""
    if not request.json:
        abort(400, "Not a JSON")
    elif 'email' not in request.json:
        abort(400, "Missing email")
    elif 'password' not in request.json:
        abort(400, "Missing password")
    else:
        new_user = user.User(**request.json)
        storage.new(new_user)
        storage.save()
        return jsonify(new_user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """Updates a User object based on id"""
    data = storage.get(user.User, user_id)
    if not data:
        abort(404)
    if not request.json:
        abort(400, "Not a JSON")
    else:
        for key, value in request.json.items():
            if key not in ['id', 'email', 'created_at', 'updated_at']:
                data[key] = value
        storage.save()
        return jsonify(data.to_dict()), 200
