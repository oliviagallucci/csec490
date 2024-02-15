"""
TODO
"""
from flask import Blueprint
from .flag import bp as flag_bp

bp = Blueprint("lesson", __name__)


@bp.route("/")
def root():
    """
    TODO
    """
    return "Lesson"


@bp.route("/<lesson_id>")
def get_flag(organization_id, class_id, lesson_id):
    """
    TODO
    """
    return f"{organization_id} {class_id} {lesson_id}"

bp.register_blueprint(flag_bp, url_prefix="/<lesson_id>/flag")
