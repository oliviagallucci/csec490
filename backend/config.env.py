from os import environ

SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI', '')
