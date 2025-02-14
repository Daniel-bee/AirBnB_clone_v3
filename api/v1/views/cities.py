#!/usr/bin/python3
"""
create a new view for City objects
that handles all default RESTFul API actions:
"""
from flask import abort, jsonify, request
from api.v1.views import app_views
from models import storage, city, state


@app_views.route('/states/<state_id>/cities', methods=["GET"],
                 strict_slashes=False)
def get_state(state_id):
    """list of all City objects of a State:
    GET /api/v1/states/<state_id>/cities"""
    sta = storage.getCity(state_id)
    if sta:
        lis = []
        for dictvalue in sta:
            lis.append(dictvalue.to_dict())
        return jsonify(lis)
    abort(404)


@app_views.route('/cities/<city_id>', methods=["GET"],
                 strict_slashes=False)
def get_city(city_id):
    """list a city"""
    cit = storage.get(city.City, city_id)
    if cit:
        return jsonify(cit.to_dict())
    abort(404)


@app_views.route('/cities/<city_id>', methods=["DELETE"],
                 strict_slashes=False)
def del_city(city_id):
    """Deletes a City object: DELETE /api/v1/cities/<city_id>"""
    gcit = storage.get(city.City, city_id)
    if gcit:
        storage.delete(gcit)
        storage.save()
        return jsonify({}), 200
    abort(404)


@app_views.route('/states/<state_id>/cities', methods=["POST"],
                 strict_slashes=False)
def create_city(state_id):
    """Creates a City: POST /api/v1/states/<state_id>/cities"""
    cit = storage.get(state.State, state_id)
    if not cit:
        abort(404)
    if not request.json:
        return jsonify({'error': 'Not a JSON'}), 400
    elif "name" not in request.json:
        return jsonify({'error': 'Missing name'}), 400
    if cit:
        dict_ = {'state_id': state_id}
        for key, value in request.json.items():
            dict_[key] = value
        newcity = city.City(**dict_)
        storage.new(newcity)
        storage.save()
        return jsonify(newcity.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """Updates a City object: PUT /api/v1/cities/<city_id>"""
    data = storage.get(city.City, city_id)
    if not request.json:
        return jsonify({'error': 'Not a JSON'}), 400
    if data:
        for key, value in request.json.items():
            if key not in ['id', 'state_id', 'created_at', 'updated_at']:
                setattr(data, key, value)
        storage.save()
        return jsonify(data.to_dict()), 200
    abort(404)
