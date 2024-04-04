"""
TODO

Virtual Machine (VM) management
"""

from flask import Blueprint, request
from flask_login import login_required, current_user
from server import provider

bp = Blueprint("vm", __name__)


@bp.route("/", methods=["GET"])
def get_vm():
    """
    TODO
    """
    return "VM"


@bp.route("/images", methods=["GET"])
@login_required
def get_images():
    """
    TODO
    """
    return provider.get_images()


@bp.route("/flavors", methods=["GET"])
@login_required
def get_flavors():
    """
    TODO
    """
    return provider.get_flavors()
