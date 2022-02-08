#!/usr/bin/python3
"""
create a new view for Place objects
that handles all default RESTFul API actions:
"""
from flask import abort, jsonify, request
from api.v1.views import app_views
from models import storage, city, place, user


@app_views.route('/cities/<city_id>/places', methods=["GET"],
                 strict_slashes=False)
def get_place(city_id):
    """list of all Place objects of a State"""
    cty = storage.getPlace(city_id)
    if cty:
        lis = []
        for x in cty:
            lis.append(x.to_dict())
        return jsonify(lis)
    abort(404)


@app_views.route('/places/<place_id>', methods=["GET"],
                 strict_slashes=False)
def get_place(place_id):
    """list a place"""
    plc = storage.get(place.Place, place_id)
    if plc:
        return jsonify(plc.to_dict())
    abort(404)


@app_views.route('/places/<place_id>', methods=["DELETE"],
                 strict_slashes=False)
def del_place(place_id):
    """Deletes a Place object"""
    gplc = storage.get(place.Place, place_id)
    if gplc:
        storage.delete(gplc)
        storage.save()
        return jsonify({}), 200
    abort(404)


@app_views.route('/cities/<city_id>/places', methods=["POST"],
                 strict_slashes=False)
def create_place(city_id):
    """Creates a PLace Instance"""
    plc = storage.get(city.City, city_id)
    if not plc:
        abort(404)
    if not request.json:
        return jsonify({'error': 'Not a JSON'}), 400
    elif "name" not in request.json:
        return jsonify({'error': 'Missing name'}), 400
    elif "user_id" not in request.json:
        return jsonify({'error': 'Missing user_id'}), 400
    if not storage.get(user.User, user_id):
        abort(404)
    if plc:
        dict_ = {'city_id': city_id}
        for key, value in request.json.items():
            dict_[key] = value
        new_place = place.Place(**dict_)
        storage.new(new_place)
        storage.save()
        return jsonify(new_place.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    """Updates a Place object"""
    data = storage.get(place.Place, place_id)
    if not request.json:
        return jsonify({'error': 'Not a JSON'}), 400
    if data:
        for key, value in request.json.items():
            if key not in ['id', 'place_id', 'created_at', 'updated_at']:
                data.name = value
        storage.save()
        return jsonify(data.to_dict()), 200
    abort(404)
