import logging
import re

from models.url import Url
from models.user import User
from appconfig import db
from datetime import datetime, timedelta
from .id_hashing import INVALID_NUMBER, id_mapping

def password_hash(pswd):
    # please implement hash here...
    return pswd

def JWT_generator(input):
    # please implement generator here...
    return "userid-"+str(input)

def create_new_user(body):
    username = body['username']
    password = password_hash(body['password'])
    
    # if username is None or password is None:
    #     raise Exception("Incomplete/invalid input")
    
    existing_user = User.query.filter_by(username = username).first()
    if existing_user:
        return None
    
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return new_user.as_dict()

def get_all_users():
    users = User.query.all()
    users = [user.as_dict() for user in users]
    return users

def reset_passwords(body):
    username = body['username']
    old_password = password_hash(body['old-password'])
    new_password = password_hash(body['new-password'])

    user = User.query.filter_by(username=username).first()
    if user is None:
        raise Exception("User doesn't exist")
    
    if user.password != old_password:
        return False
    else:
        user.password = new_password
        db.session.commit()
        return True
        
def user_login(body):
    username = body['username']
    password = password_hash(body['password'])
    
    user = User.query.filter_by(username=username).first()
    if user.password != password:
        return None
    else:
        JWT = JWT_generator(user.userid)
        return JWT
    
    