#!/usr/bin/env python3
from flask import Blueprint, jsonify, request, abort
import services.url_service as url_service
import services.user_service as user_service
# from models.url import Url
import json
import logging

api = Blueprint('url_mapping', 'url_mapping')

# asdasd

# request all the identifiers

@api.route('/users', methods=['POST'])
def api_create_new_user():
    new_user = user_service.create_new_user(request.json)
    if new_user == None:
        return 'duplicate', 409
    else:
        return jsonify(new_user), 201

@api.route('/users', methods=['GET'])
def api_get_all_users():
    users = user_service.get_all_users()
    if users == []:
        return jsonify({'message': 'no users'})
    return jsonify(users)

@api.route('/users', methods=['PUT'])
def api_reset_password():
    result = user_service.reset_passwords(request.json)
    if not result:
        return jsonify({'message': 'Old password incorrect'}), 403
    return jsonify({'message': 'successfully updated'}), 200

@api.route('/users/login', methods=['POST'])
def api_user_login():
    JWT = user_service.user_login(request.json)
    if not JWT:
        return jsonify({'message': 'forbidden'}), 403
    else:
        return JWT, 200

@api.route('/', methods=['GET'])
def api_get_all_urls(): 
    ''' Get all entities'''
    JWT_resolve = user_service.JWT_verification(request.headers.get('Authorization'))
    if JWT_resolve <= -1:
        return "forbidden", 403
    
    urls = url_service.get_all_urls(JWT_resolve)
    if urls == []:
        return jsonify({'message': ''})
    return jsonify(urls)

# create new identifier for long url
@api.route('/', methods=['POST'])
def api_create_new_url():
    ''' Create entity'''
    JWT_resolve = user_service.JWT_verification(request.headers.get('Authorization'))
    if JWT_resolve <= -1:
        return "forbidden", 403
    
    url = url_service.create_new_url(JWT_resolve, request.json)
    if url is None:
        return "invalid url", 400
    # elif url['message'] is not None:
    #     return 'forbidden', 403
    return jsonify(url), 201

@api.route('/<string:identifier>', methods=['GET'])
def api_get_url_by_identifier(identifier):
    url = url_service.get_url_by_identifier(identifier)
    if url is None:
        return "", 404
    return {"value": url}, 301

@api.route('/<string:identifier>', methods=['PUT'])
def api_update_entity_by_identifier(identifier):
    JWT_resolve = user_service.JWT_verification(request.headers.get('Authorization'))
    if JWT_resolve <= -1:
        return "forbidden", 403
    
    data = json.loads(request.get_data())
    entity = url_service.update_entity_by_identifier(identifier, data)
    if entity is None:
        return "Identifier not found", 404
    return entity, 200

@api.route('/<string:identifier>', methods=['DELETE'])
def api_delete_by_identifier(identifier):
    JWT_resolve = user_service.JWT_verification(request.headers.get('Authorization'))
    if JWT_resolve <= -1:
        return "forbidden", 403
    
    if url_service.delete_by_identifier(identifier):
        return "\delete success", 204
    return "identifier not found", 404

@api.route('/', methods=['DELETE'])
def api_delete_all_urls():
    JWT_resolve = user_service.JWT_verification(request.headers.get('Authorization'))
    if JWT_resolve <= -1:
        return "forbidden", 403
    
    url_service.delete_all_urls(JWT_resolve)
    return "deleted", 404


@api.errorhandler(Exception)
def handle_exception(e):
    logging.error("request error:", e)
    return "error", 400
