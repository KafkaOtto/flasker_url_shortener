#!/usr/bin/env python3
import os
import yaml
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from cryptography.hazmat.primitives import serialization

app = Flask(__name__)

config_obj = yaml.load(open('dbconfig.yaml'), Loader=yaml.Loader)

db_username = os.getenv('DB_USERNAME') or config_obj.get('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD') or config_obj.get('DB_PASSWORD')
db_server = os.getenv('DB_SERVER') or config_obj.get('DB_SERVER')
db_name = os.getenv('DB_NAME') or config_obj.get('DB_NAME')

# override the environment variables
db_uri = 'mysql+pymysql://{username}:{password}@{server}:3306/{db_name}?charset=utf8mb4'
SQLALCHEMY_DATABASE_URI = db_uri.format(
    username=db_username,
    password=db_password,
    server=db_server,
    db_name=db_name
)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or config_obj.get('SECRET_KEY')


db = SQLAlchemy(app)
migrate = Migrate(app, db)

with open("public_key.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
    )
public_key_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)