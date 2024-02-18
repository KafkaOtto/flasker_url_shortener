#!/usr/bin/env python3
import os
import yaml
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

config_obj = yaml.load(open('dbconfig.yaml'), Loader=yaml.Loader)

# override the environment variables
database_url = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_DATABASE_URI'] = config_obj['SQLALCHEMY_DATABASE_URI'] if database_url is None else database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

secret_key = os.getenv('SECRET_KEY')
app.config['SECRET_KEY'] = config_obj['SECRET_KEY'] if secret_key is None else secret_key

migrate = Migrate(app, db)