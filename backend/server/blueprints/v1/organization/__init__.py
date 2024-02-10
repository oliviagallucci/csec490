from flask import Blueprint

bp = Blueprint('organization', __name__)

@bp.route('/')
def root():
    return "Organization"

@bp.route('/<organization_id>')
def get_org(organization_id):
    return f"{organization_id}"

from .classes import bp as class_bp

bp.register_blueprint(class_bp, url_prefix='/<organization_id>/class')