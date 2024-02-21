#!/usr/bin/env python3
import logging

from flask import Blueprint, jsonify, request, make_response
import services.user_service as user_service
from services.jwt_service import jwt
from appconfig import app
from functools import wraps


user_api = Blueprint('users', 'users')

# Authentication decorator
def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        # ensure the jwt-token is passed with the headers
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if not token: # throw error if no token provided
            return {"message": "A valid token is missing!"}, 403
        try:
           # decode the token to obtain user name
            username = jwt.decode(token, app.config['SECRET_KEY'])
        except Exception as e:
            logging.error("invalid token", e)
            return {"message": "Invalid token!"}, 403
         # Return the user information attached to the token
        return f(username, *args, **kwargs)
    return decorator


@user_api.route('/users', methods=['POST'])
def api_create_new_user():
    new_user = user_service.create_new_user(request.json)
    if new_user == None:
        return jsonify({'detail': 'duplicate'}), 409
    else:
        return jsonify(new_user), 201

@user_api.route('/users', methods=['GET'])
def api_get_all_users():
    users = user_service.get_all_users()
    if users == []:
        return jsonify({'message': 'no users'})
    return jsonify(users)

@user_api.route('/users', methods=['PUT'])
# @token_required
def api_reset_password():
    result = user_service.reset_passwords(request.json)
    if not result:
        return jsonify({'detail': 'forbidden'}), 403
    return jsonify({'message': 'successfully updated'}), 200

@user_api.route('/users/login', methods=['POST'])
def api_user_login():
    user = user_service.user_login(request.json)
    if not user:
        return jsonify({'detail': 'forbidden'}), 403
    else:
        token = jwt.encode(user['username'], app.config['SECRET_KEY'])
        # print(token)
        return jsonify({'token': token}), 200

@user_api.route('/users/all', methods=['DELETE'])
def api_delete_all_users():
    res = user_service.delete_all_users()
    if res == 1:
        return jsonify({'msg': 'success'}), 200
    else:
        return jsonify({'msg': 'fail'}), 400

@user_api.route('/auth', methods=['GET'])
@token_required
def api_auth(username):
    response = make_response("success", 200)
    response.set_cookie('username', username)
    return response
