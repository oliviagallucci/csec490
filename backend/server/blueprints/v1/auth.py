"""
This module contains the authentication routes
"""

from flask import Blueprint, request
from flask_login import login_user, logout_user, login_required, current_user
from passlib.hash import bcrypt
from server.models import User


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login_post():
    """
    Authenticate user
    """
    username = request.form.get("username")
    password = request.form.get("password")

    acct = User.query.filter_by(username=username).first()

    if not acct or not bcrypt.verify(password, acct.password):
        return "Invalid username or password", 403
    login_user(acct)
    return "Login Successful", 200


@auth_bp.route("/logout")
@login_required
def logout():
    """
    Logout user
    """
    logout_user()
    return "Logout Complete", 200
