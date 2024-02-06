from flask import Blueprint

bp = Blueprint('user', __name__)

@bp.route('/')
def root():
    return "User"