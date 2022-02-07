#!/usr/bin/python3
"""
create a new view for Amenity objects
that handles all default RESTFul API actions:
"""
from flask import abort, jsonify, request
from api.v1.views import app_views
from models import storage, amenity


@app_views.route('/amenities', methods=["GET"], strict_slashes=False)
def all_amenities():
    """ retrieves a list of all Amenity objects """
    amens = []
    for value in storage.all(amenity.Amenity).values():
        amens.append(value.to_dict())
    return jsonify(amens)


@app_views.route('/amenities/<amenity_id>', methods=["GET"],
                 strict_slashes=False)
def get_amenity(amenity_id):
    """display an Amenity object"""
    amen = storage.get(amenity.Amenity, amenity_id)
    if amen:
        return jsonify(amen.to_dict())
    else:
        abort(404)


@app_views.route('/amenities/<amenity_id>', methods=["DELETE"],
                 strict_slashes=False)
def del_amenity(amenity_id):
    """Deletes an Amenity object: DELETE /api/v1/amenities/<amenity_id>"""
    amen_obj = storage.get(amenity.Amenity, amenity_id)
    if amen_obj:
        storage.delete(amen_obj)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)


@app_views.route('/amenities', methods=["POST"],
                 strict_slashes=False)
def create_amenity():
    """Creates an Amenity: POST /api/v1/amenities"""
    if not request.json:
        abort(400, "Not a JSON")
    elif "name" not in request.json:
        abort(400, "Missing name")
    else:
        new_amen = amenity.Amenity(**request.json)
        storage.new(new_amen)
        storage.save()
        return jsonify(new_amen.to_dict()), 201

@app_views.route('/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def update_amenity(amenity_id):
    """Updates an Amenity object: PUT /api/v1/amenities/<amenity_id"""
    data = storage.get(amenity.Amenity, amenity_id)
    if data is None:
        abort(404)
    if not request.json:
        abort(400, "Not a JSON")
    else:
        for key, value in request.json.items():
            if key not in ['id', 'created_at', 'updated_at']:
                data.name = value
        storage.save()
        return jsonify(data.to_dict()), 200
