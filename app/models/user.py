#!/usr/bin/env python3
from dbconfig import db


class User(db.Model):
    ''' The data model'''
    # table name
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    email = db.Column(db.String(200), nullable=False)
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}