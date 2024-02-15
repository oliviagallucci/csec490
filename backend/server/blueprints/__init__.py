"""
Define all sub-routes for /api
"""
from flask import Blueprint
from .v1 import v1_bp

api_bp = Blueprint("api", __name__)

api_bp.register_blueprint(v1_bp, url_prefix="/v1")
