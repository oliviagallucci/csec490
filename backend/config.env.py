"""
Assign config options from environment variables
If you want to hard code your config, you can do so in config.py (it's not tracked by git)
"""
from os import environ

SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI", "")
