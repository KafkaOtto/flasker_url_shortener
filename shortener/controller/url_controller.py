#!/usr/bin/env python3
from flask import Blueprint, jsonify, request
import services.url_service as url_service
from functools import wraps
import json
import logging
import sys

api = Blueprint('url_mapping', 'url_mapping')

def login_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        # # Print cookies
        # print(f"Cookies: {request.cookies}", file=sys.stderr)
        #
        # # Print headers
        # print(f"Headers: {request.headers}", file=sys.stderr)
        #
        # # Correct logging syntax with f-strings for better readability
        # logging.debug(f"Cookies: {request.cookies}")
        # logging.debug(f"Headers: {request.headers}")
        username = request.cookies.get('username')
        if not username: # throw error if no token provided
            return {"message": "You need to login!"}, 403
        return f(username, *args, **kwargs)
    return decorator

# request all the identifiers
@api.route('/', methods=['GET'])
def api_get_all_urls():
    ''' Get all entities'''
    urls = url_service.get_all_urls()
    if urls == []:
        return jsonify({'message': ''})
    return jsonify(urls)

# create new identifier for long url
@api.route('/', methods=['POST'])
@login_required
def api_create_new_url(username):
    ''' Create entity'''
    url = url_service.create_new_url(username, request.json)
    if url is None:
        return "invalid url", 400
    # return
    return jsonify(url), 201

@api.route('/<string:identifier>', methods=['GET'])
@login_required
def api_get_url_by_identifier(username, identifier):
    url = url_service.get_url_by_identifier(username, identifier)
    if url is None:
        return "", 404
    return {"value": url}, 301

@api.route('/<string:identifier>', methods=['PUT'])
@login_required
def api_update_entity_by_identifier(username, identifier):
    data = json.loads(request.get_data())
    entity = url_service.update_entity_by_identifier(username, identifier, data)
    if entity is None:
        return "Identifier not found", 404
    return entity, 200

@api.route('/<string:identifier>', methods=['DELETE'])
@login_required
def api_delete_by_identifier(username, identifier):
    if url_service.delete_by_identifier(username, identifier):
        return "delete success", 204
    return "identifier not found", 404

@api.route('/', methods=['DELETE'])
@login_required
def api_delete_all_urls(username):
    url_service.delete_all_urls()
    return "identifier not specify", 404


@api.errorhandler(Exception)
def handle_exception(e):
    logging.error("request error:", e)
    return "error", 400