from flask import Blueprint

bp = Blueprint('lesson', __name__)

@bp.route('/')
def root():
    return "Lesson"

@bp.route('/<lesson_id>')
def get_flag(organization_id, class_id, lesson_id):
    return f"{organization_id} {class_id} {lesson_id}"

from .flag import bp as flag_bp

bp.register_blueprint(flag_bp, url_prefix='/<lesson_id>/flag')