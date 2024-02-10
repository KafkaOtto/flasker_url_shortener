#!/usr/bin/env python3
from flask import Blueprint, jsonify, request
import services.url_service as url_service
# from models.url import Url
from werkzeug.exceptions import HTTPException
import json

api = Blueprint('users', 'users')


@api.route('/', methods=['GET']) # COMPLETED
def api_get_all_urls(): 
    ''' Get all entities'''
    urls = url_service.get_all_urls()
    return jsonify(urls)

@api.route('/', methods=['POST']) # COMPLETED
def api_create_new_url():
    ''' Create entity'''
    url = url_service.create_new_url(request.json)
    # return 
    return jsonify(url)

@api.route('/<string:identifier>', methods=['GET'])
def api_get_url_by_identifier(identifier):
    url = url_service.get_url_by_identifier(request.json)
    return jsonify(url)

@api.route('/<string:identifier>', methods=['DELETE'])
def api_delete_by_identifier(identifier):
    url = url_service.delete_by_identifier(request.json)
    return jsonify(url)

@api.route('/', methods=['DELETE'])
def api_delete_all_urls():
    url = url_service.delete_all_urls()
    return jsonify(url)



# Not yet in progresss

@api.route('/users/<string:id>', methods=['PUT'])
def api_put(id):
    ''' Update entity by id'''
    body = request.json
    body['id'] = id
    res = url_service.put(body)
    return jsonify(res.as_dict()) if isinstance(res, User) else jsonify(res)

@api.route('/users/<string:id>', methods=['DELETE'])
def api_delete(id):
    ''' Delete entity by id'''
    res = url_service.delete(id)
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