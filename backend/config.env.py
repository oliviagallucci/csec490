"""
Assign config options from environment variables
If you want to hard code your config, you can do so in config.py (it's not tracked by git)
"""

from os import environ

SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI", "")
REDIS_HOST = environ.get("REDIS_HOST", "")

VM_PROVIDER = environ.get("VM_PROVIDER", "")
SECRET_KEY = environ.get("SECRET_KEY", "super_secret_key")