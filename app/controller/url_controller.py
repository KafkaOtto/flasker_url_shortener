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
    return jsonify(urls)

# create new identifier for long url
@api.route('/', methods=['POST'])
def api_create_new_url():
    ''' Create entity'''
    url = url_service.create_new_url(request.json)
    if url is None:
        return "invalid url", 400
    # return 
    return jsonify(url)

@api.route('/<string:identifier>', methods=['GET'])
def api_get_url_by_identifier(identifier):
    url = url_service.get_url_by_identifier(identifier)
    if url is None:
        return "", 404
    return url, 301

@api.route('/<string:identifier>', methods=['DELETE'])
def api_delete_by_identifier(identifier):
    if url_service.delete_by_identifier(identifier):
        return "delete success", 204
    return "identifier not found", 404

@api.route('/', methods=['DELETE'])
def api_delete_all_urls():
   return "identifier not specify", 404



# Not yet in progresss

# @api.route('/users/<string:id>', methods=['PUT'])
# def api_put(id):
#     ''' Update entity by id'''
#     body = request.json
#     body['id'] = id
#     res = url_service.put(body)
#     return jsonify(res.as_dict()) if isinstance(res, User) else jsonify(res)

# @api.route('/users/<string:id>', methods=['DELETE'])
# def api_delete(id):
#     ''' Delete entity by id'''
#     res = url_service.delete(id)
#     return jsonify(res)

@api.errorhandler(Exception)
def handle_exception(e):
    logging.error("request error:", e)
    return "error", 400
