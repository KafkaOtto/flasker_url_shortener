#!/usr/bin/env python3
from appconfig import db


class Url(db.Model):
    ''' The data model'''
    # table name
    __tablename__ = 'url_mapping'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    long_url = db.Column(db.String(128), nullable=False)
    # short_url = db.Column(db.String(64), nullable=False)
    expire_date = db.Column(db.DateTime, nullable=True)
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
   
   
