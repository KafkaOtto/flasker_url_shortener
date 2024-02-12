#!/usr/bin/env python3
from flask import Blueprint, jsonify, request
import services.url_service as url_service
# from models.url import Url
import json
import logging

api = Blueprint('url_mapping', 'url_mapping')

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
def api_create_new_url():
    ''' Create entity'''
    url = url_service.create_new_url(request.json)
    if url is None:
        return "invalid url", 400
    # return 
    return jsonify(url), 201

@api.route('/<string:identifier>', methods=['GET'])
def api_get_url_by_identifier(identifier):
    url = url_service.get_url_by_identifier(identifier)
    if url is None:
        return "", 404
    return {"value": url}, 301

@api.route('/<string:identifier>', methods=['PUT'])
def api_update_entity_by_identifier(identifier):
    data = json.loads(request.get_data())
    entity = url_service.update_entity_by_identifier(identifier, data)
    if entity is None:
        return "Identifier not found", 404
    return entity, 200

@api.route('/<string:identifier>', methods=['DELETE'])
def api_delete_by_identifier(identifier):
    if url_service.delete_by_identifier(identifier):
        return "delete success", 204
    return "identifier not found", 404

@api.route('/', methods=['DELETE'])
def api_delete_all_urls():
    url_service.delete_all_urls()
    return "identifier not specify", 404


@api.errorhandler(Exception)
def handle_exception(e):
    logging.error("request error:", e)
    return "error", 400
