from flask import Blueprint

bp = Blueprint('hello', __name__)

@bp.route('/')
def root():
    return "Hello World!"