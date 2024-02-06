from flask import Blueprint

bp = Blueprint('flag', __name__)

@bp.route('/')
def root():
    return "Flag"

@bp.route('/<flag_id>')
def get_flag(organization_id, class_id, lesson_id, flag_id):
    return f"Flag {organization_id} {class_id} {lesson_id} {flag_id}"