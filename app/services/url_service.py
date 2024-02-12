#!/usr/bin/env python3
from models.url import Url
from dbconfig import db
from werkzeug.exceptions import NotFound
import base64

def get_all_urls():
    '''
    Get all entities
    :returns: all entity
    '''
    urls = Url.query.all()
    urls = [url.as_dict() for url in urls]
    return urls

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

    db.session.add(url)
    db.session.commit()
    url = url.as_dict()
    return url

<<<<<<< Updated upstream
def get_url_by_identifier(body):
    # get the corresponding entity by short url, if not exist then return None
    # url = Url(**body)
    try:
        identifier = body['short_url']
        entity = Url.query.filter_by(short_url = identifier).first()
        
    except Exception: 
        identifier = body['long_url']
        entity = Url.query.filter_by(long_url = identifier).first()
        
    finally:
        if entity:
            return entity.as_dict()
        else:
            return {'error': "this identifier cannot be found"}

=======
def update_entity_by_identifier(identifier, body):
    id = hashids.decode(identifier)
    if id == ():
        return None
    entity = Url.query.filter_by(id=id).first()
    if entity is None:
        logging.info("identifier not found")
        return entity
    if body is None or body.get('long_url') is None or is_valid_url(body.get('long_url')) is False:
        raise Exception("illegal input")
    expire_date = body.get('expire_date')
    if expire_date:
        expire_date = datetime.strptime(expire_date, '%Y-%m-%d %H:%M:%S')
    else:
         ten_years_later = datetime.now() + timedelta(days=365 * 10)
         expire_date = ten_years_later

    entity.expire_date = expire_date
    entity.long_url = body.get('long_url')
    db.session.commit()
    entity.id = hashids.encode(entity.id)
    entity = entity.as_dict()
    return entity

def get_url_by_identifier(identifier):
    id = hashids.decode(identifier)
    print("----------")
    print(id)
    if id == ():
        return None
    current_time = datetime.now()
    entity = Url.query.filter_by(id = id)
    if entity is None:
        return entity
    entity = entity.first()
    if entity.expire_date < current_time:
        logging.info("identifier expired for", identifier)
        return None
    return entity.long_url

def delete_by_identifier(identifier):
    id = hashids.decode(identifier)
    entity = Url.query.filter_by(id = id).first()
    if entity:
        db.session.delete(entity)
        db.session.commit()
        return True
    else:
        return False
>>>>>>> Stashed changes

def delete_by_identifier(body):
    try:
        identifier = body['short_url']
        entity = Url.query.filter_by(short_url = identifier).first()
        
    except Exception: 
        identifier = body['long_url']
        entity = Url.query.filter_by(long_url = identifier).first()
        
    finally:
        if entity:
            db.session.delete(entity)
            db.session.commit()
            return {'message': 'successfully deleted'}
        else:
            return {'error': "this identifier cannot be found"}
        
def delete_all_urls():
    num_of_delete = db.session.query(Url).delete()
    db.session.commit()
    return {'number of deletion' : f'{num_of_delete}'}

# def get_url_by_long(body):
#     # get the corresponding entity by short url, if not exist then return None
#     # url = Url(**body)
#     long_url = body['long_url']
#     entity = Url.query.filter_by(long_url = long_url).first()
    
#     if entity:
#         entity = entity.as_dict()
#         print(type(entity))
#         return entity
#     else:
#         return {'error': "404 not found"}

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

