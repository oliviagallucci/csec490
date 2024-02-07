from flask import Blueprint

v1_bp = Blueprint('v1', __name__)

from .hello import bp as hello_bp

from .organization import bp as organization_bp
from .vm import bp as vm_bp

v1_bp.register_blueprint(organization_bp, url_prefix='/organization')
v1_bp.register_blueprint(hello_bp, url_prefix='/hello')
v1_bp.register_blueprint(vm_bp, url_prefix='/vm')