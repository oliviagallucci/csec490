"""
TODO

Virtual Machien (VM) management
"""
from flask import Blueprint

bp = Blueprint("vm", __name__)


@bp.route("/")
def root():
    """
    TODO
    """
    return "VM"
