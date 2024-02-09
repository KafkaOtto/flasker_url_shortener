#!/usr/bin/env python3
from models.user import Url
from dbconfig import db
from werkzeug.exceptions import NotFound
import base64

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
    short_url = base64.b64encode(body['long_url'].encode())
    body.update({'short_url': short_url})
    body.update({'expire_date': None})
    
    url = Url(**body)
    url.short_url = str(base64.b64encode(body['long_url'].encode()))[2:-1]
    url.expire_date = '2024-12-31 23:59:59'

    # print(url['long_url'])
    # print(body)
    db.session.add(url)
    db.session.commit()
    print(Url.query.all())
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