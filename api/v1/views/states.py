#!/usr/bin/python3
"""
    view for State objects that handles
    all default RESTFul API actions
"""
from flask import abort, jsonify, request
from api.v1.views import app_views
from models import storage, state


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """get all states and convert object into a valid JSON"""
    list_ = []
    for value in storage.all(state.State).values():
        list_.append(value.to_dict())
    return jsonify(list_)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state_byid(state_id):
    """If the state_id is not linked to any State object, raise a 404 error"""
    sta = storage.get(state.State, state_id)
    if sta:
        return jsonify(sta.to_dict())
    else:
        abort(404)


@app_views.route('/states/<state_id>',
                 methods=['DELETE'], strict_slashes=False)
def del_state_object(state_id):
    """If the state_id is not linked to any State object, raise a 404 error"""
    obj = storage.get(state.State, state_id)
    if not obj:
        abort(404)
    else:
        storage.delete(obj)
        storage.save()
        return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def post_state():
    """Creates a State: POST /api/v1/states"""
    if not request.get_json:
        abort(400, "Not a JSON")
    elif 'name' not in request.get_json:
        abort(400, "Missing name")
    else:
        newstate = state.State(**request.get_json)
        storage.new(newstate)
        storage.save()
        return jsonify(newstate.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """Updates a State object: PUT /api/v1/states/<state_id>"""
    data = storage.get(state.State, state_id)
    if not data:
        abort(404)
    if not request.get_json:
        abort(400, "Not a JSON")
    else:
        for key, value in request.get_json.items():
            if key not in ['id', 'created_at', 'updated_at']:
                data.name = value
        storage.save()
        return jsonify(data.to_dict()), 200
