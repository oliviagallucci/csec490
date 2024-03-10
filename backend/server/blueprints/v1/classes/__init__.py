"""
TODO
"""
from flask import Blueprint, request, jsonify
from .lesson import bp as lesson_bp
from server.models import Class
from server import db

bp = Blueprint("classes", __name__)

@bp.route("/", methods=["POST"])
def create():
    """
    TODO
    """
    class_name = request.json["name"]
    if class_name:
        new_class = Class(class_name)
        db.session.add(new_class)
        db.session.commit()
        return jsonify(new_class.json())
    return "Class Name Required", 400

@bp.route("/", methods=["GET"])
def read():
    """
    TODO
    """
    id_filter = request.args.get("id")
    if id_filter:
        return jsonify(Class.query.get(id_filter).json())
    return jsonify(list(map(lambda x: x.json(), Class.query.all())))

@bp.route("/<class_id>", methods=["PUT"])
def update(class_id):
    """
    TODO
    """
    class_name = request.json["name"]
    class_visible = request.json["visible"]
    class_to_update = Class.query.get(class_id)
    if not class_to_update:
        return "Class Not Found", 404
    class_to_update.name = class_name
    class_to_update.visible = class_visible
    db.session.commit()
    return jsonify(class_to_update.json())

@bp.route("/<class_id>", methods=["DELETE"])
def delete(class_id):
    """
    TODO
    """
    class_to_delete = Class.query.get(class_id)
    if not class_to_delete:
        return "Class Not Found", 404
    db.session.delete(class_to_delete)
    db.session.commit()
    return "Class Deleted", 200

bp.register_blueprint(lesson_bp, url_prefix="/<class_id>/lesson")
