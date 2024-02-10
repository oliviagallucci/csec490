from flask import Blueprint

bp = Blueprint('classes', __name__)

@bp.route('/')
def root():
    return "Classes"

@bp.route('/<class_id>')
def get_class(organization_id, class_id):
    return f"{organization_id} {class_id}"

from .lesson import bp as lesson_bp

bp.register_blueprint(lesson_bp, url_prefix='/<class_id>/lesson')