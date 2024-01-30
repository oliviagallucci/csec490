from flask import Blueprint

api_bp = Blueprint('api', __name__)

from .v1 import v1_bp

api_bp.register_blueprint(v1_bp, url_prefix='/v1')

