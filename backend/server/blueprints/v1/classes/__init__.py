"""
TODO
"""
from flask import Blueprint
from .lesson import bp as lesson_bp

bp = Blueprint("classes", __name__)


@bp.route("/")
def root():
    """
    TODO
    """
    return "Classes"


@bp.route("/<class_id>")
def get_class(organization_id, class_id):
    """
    TODO
    """
    return f"{organization_id} {class_id}"

bp.register_blueprint(lesson_bp, url_prefix="/<class_id>/lesson")
