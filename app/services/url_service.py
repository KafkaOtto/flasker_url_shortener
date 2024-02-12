# #!/usr/bin/env python3
import logging
import re

from models.url import Url
from dbconfig import db
from datetime import datetime, timedelta
from .id_hashing import INVALID_NUMBER, id_mapping

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
    long_url = body.get('value')
    if (long_url is None or is_valid_url(long_url)) is False:
        return None
    current_time = datetime.now()
    existing_entity = Url.query.filter_by(long_url=long_url).first()
    if existing_entity is not None:
        if existing_entity.expire_date < current_time:
            ten_years_later = current_time + timedelta(days=365 * 10)
            existing_entity.expire_date = ten_years_later
            db.session.commit()
        existing_entity.id = id_mapping.encode(existing_entity.id)
        return existing_entity.as_dict()
    expire_date = body.get('expire_date')
    if expire_date:
        expire_date = datetime.strptime(expire_date, '%Y-%m-%d %H:%M:%S')
    else:
        expire_date = datetime.strptime('2029-12-31 23:59:59', '%Y-%m-%d %H:%M:%S')

    url = Url(long_url=long_url, expire_date=expire_date)
    db.session.add(url)
    db.session.commit()
    url.id = id_mapping.encode(url.id)
    url = url.as_dict()
    return url

def update_entity_by_identifier(identifier, body):
    id = id_mapping.decode(identifier)
    if id == INVALID_NUMBER:
        return None
    entity = Url.query.filter_by(id=id).first()
    if entity is None:
        logging.info("identifier not found")
        return entity
    long_url = body.get('url')
    if long_url is None or is_valid_url(long_url) is False:
        raise Exception("illegal input")
    expire_date = body.get('expire_date')
    if expire_date:
        expire_date = datetime.strptime(expire_date, '%Y-%m-%d %H:%M:%S')
    else:
         ten_years_later = datetime.now() + timedelta(days=365 * 10)
         expire_date = ten_years_later

    entity.expire_date = expire_date
    entity.long_url = long_url
    db.session.commit()
    entity.id = id_mapping.encode(entity.id)
    entity = entity.as_dict()
    return entity

def get_url_by_identifier(identifier):
    id = id_mapping.decode(identifier)
    if id == INVALID_NUMBER:
        return None
    current_time = datetime.now()
    entity = Url.query.filter_by(id = id).first()
    if entity is None:
        return entity
    if entity.expire_date < current_time:
        logging.info("identifier expired for", identifier)
        return None
    return entity.long_url

def delete_by_identifier(identifier):
    id = id_mapping.decode(identifier)
    if id == INVALID_NUMBER:
        return None
    entity = Url.query.filter_by(id = id).first()
    if entity:
        db.session.delete(entity)
        db.session.commit()
        return True
    else:
        return False

def delete_all_urls():
    num_of_delete = db.session.query(Url).delete()
    db.session.commit()
    return {'number of deletion' : f'{num_of_delete}'}


url_regex = re.compile(r'(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))')

def is_valid_url(url):
    return url is not None and bool(url_regex.search(url))
