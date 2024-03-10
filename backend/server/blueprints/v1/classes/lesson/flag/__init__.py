"""
TODO
"""
from flask import Blueprint, request, jsonify
from server.models import Flag
from server import db

bp = Blueprint("flag", __name__)


@bp.route("/", methods=["POST"])
def create(class_id, lesson_id):
    """
    TODO
    """
    flag_name = request.json["name"]
    if flag_name:
        new_flag = Flag("", "", 0, lesson_id)
        db.session.add(new_flag)
        db.session.commit()
        return jsonify(new_flag.json()), 201
    return "Flag Name Required", 400

@bp.route("/", methods=["GET"])
def read(class_id, lesson_id):
    """
    TODO
    """
    id_filter = request.args.get("id")
    if id_filter:
        return jsonify([Flag.query.get(id_filter).json()])
    return jsonify(list(map(lambda x: x.json(), Flag.query.all())))

@bp.route("/<flag_id>", methods=["PUT"])
def update(class_id, lesson_id, flag_id):
    """
    TODO
    """
    flag_style = request.json["style"]
    flag_config = request.json["config"]
    flag_points = request.json["points"]
    
    flag_to_update = Flag.query.get(flag_id)
    if not flag_to_update:
        return "Flag Not Found", 404
    flag_to_update.style = flag_style
    flag_to_update.config = flag_config
    flag_to_update.points = flag_points
    db.session.commit()
    return jsonify(flag_to_update.json())

@bp.route("/<flag_id>", methods=["DELETE"])
def delete(class_id, lesson_id, flag_id):
    """
    TODO
    """
    flag_to_delete = Flag.query.get(flag_id)
    if not flag_to_delete:
        return "Flag Not Found", 404
    db.session.delete(flag_to_delete)
    db.session.commit()
    return "Flag Deleted", 200
