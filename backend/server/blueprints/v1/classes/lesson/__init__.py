"""
TODO
"""

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from server import db
from server.models import Lesson
from .flag import bp as flag_bp
from .vm import bp as vm_bp

bp = Blueprint("lesson", __name__)


@bp.route("/", methods=["POST"])
@login_required
def create(class_id):
    """
    TODO
    """
    lesson_name = request.json["name"]
    if lesson_name:
        new_lesson = Lesson(lesson_name, class_id, "")
        db.session.add(new_lesson)
        db.session.commit()
        return jsonify(new_lesson.json()), 201
    return "Lesson Name Required", 400


@bp.route("/", methods=["GET"])
@login_required
def read(class_id):
    """
    TODO
    """
    id_filter = request.args.get("id")
    if id_filter:
        return jsonify([Lesson.query.get(id_filter).json()])
    return jsonify(list(map(lambda x: x.json(), Lesson.query.all())))


@bp.route("/<lesson_id>", methods=["PUT"])
@login_required
def update(class_id, lesson_id):
    """
    TODO
    """
    lesson_name = request.json["name"]
    lesson_config = request.json["config"]
    lesson_visible = request.json["visible"]
    lesson_to_update = Lesson.query.get(lesson_id)
    if not lesson_to_update:
        return "Lesson Not Found", 404
    lesson_to_update.name = lesson_name
    lesson_to_update.config = lesson_config
    lesson_to_update.visible = lesson_visible
    db.session.commit()
    return jsonify(lesson_to_update.json())


@bp.route("/<lesson_id>", methods=["DELETE"])
@login_required
def delete(class_id, lesson_id):
    """
    TODO
    """
    lesson_to_delete = Lesson.query.get(lesson_id)
    if not lesson_to_delete:
        return "Lesson Not Found", 404
    db.session.delete(lesson_to_delete)
    db.session.commit()
    return "Lesson Deleted", 200


bp.register_blueprint(flag_bp, url_prefix="/<lesson_id>/flag")
bp.register_blueprint(vm_bp, url_prefix="/<lesson_id>/vm")
