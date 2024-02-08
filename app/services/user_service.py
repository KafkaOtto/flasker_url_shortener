#!/usr/bin/env python3
from models.user import Url
from dbconfig import db
from werkzeug.exceptions import NotFound

def get_all_urls():
    '''
    Get all entities
    :returns: all entity
    '''
    return Url.query.all()

def get_url_by_short():
    
    return 

def create_new_url(body):
    '''
    Create entity with body
    :param body: request body
    :returns: the created entity
    '''
    url = Url(**body)
    print(body['long_url'])
    # db.session.add(user)
    # db.session.commit()
    return url

# def update_shorturl(body):
#     '''
#     Update entity by id
#     :param body: request body
#     :returns: the updated entity
#     '''
#     user = User.query.get(body['id'])
#     if user:
#         user = User(**body)
#         db.session.merge(user)
#         db.session.flush()
#         db.session.commit()
#         return user
#     raise NotFound('no such entity found with id=' + str(body['id']))

# def delete_shorturl(id):
#     '''
#     Delete entity by id
#     :param id: the entity id
#     :returns: the response
#     '''
#     user = User.query.get(id)
#     if user:
#         db.session.delete(user)
#         db.session.commit()
#         return {'success': True}
#     raise NotFound('no such entity found with id=' + str(id))

def delete_all_urls():
    
    return