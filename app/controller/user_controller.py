#!/usr/bin/env python3
from flask import Blueprint, jsonify, request
import services.user_service as user_service
from models.user import Url
from werkzeug.exceptions import HTTPException
import json

api = Blueprint('users', 'users')


@api.route('/', methods=['GET'])
def api_get_all_urls():
    ''' Get all entities'''
    users = user_service.get_all_urls()
    return jsonify([user.as_dict() for user in users])

@api.route('/', methods=['POST'])
def api_create_new_url():
    ''' Create entity'''
    user = user_service.create_new_url(request.json)
    # return 
    return jsonify(user.as_dict())

@api.route('/users/<string:id>', methods=['PUT'])
def api_put(id):
    ''' Update entity by id'''
    body = request.json
    body['id'] = id
    res = user_service.put(body)
    return jsonify(res.as_dict()) if isinstance(res, User) else jsonify(res)

@api.route('/users/<string:id>', methods=['DELETE'])
def api_delete(id):
    ''' Delete entity by id'''
    res = user_service.delete(id)
    return jsonify(res)

@api.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON format for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        'success': False,
        "message": e.description
    })
    response.content_type = "application/json"
    return response