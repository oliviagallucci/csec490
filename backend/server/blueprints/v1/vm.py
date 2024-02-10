from flask import Blueprint

bp = Blueprint('vm', __name__)

@bp.route('/')
def root():
    return "VM"

