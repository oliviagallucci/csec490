from flask import Blueprint

v1_bp = Blueprint('v1', __name__)

from .hello import hello_bp

v1_bp.register_blueprint(hello_bp, url_prefix='/hello')

