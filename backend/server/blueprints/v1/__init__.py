"""
Defines sub-routes of /api/v1
"""

from flask import Blueprint
from .auth import auth_bp
from .classes import bp as class_bp
from .vm import bp as vm_bp

v1_bp = Blueprint("v1", __name__)

v1_bp.register_blueprint(class_bp, url_prefix="/class")
v1_bp.register_blueprint(vm_bp, url_prefix="/vm")
v1_bp.register_blueprint(auth_bp)
