"""
TODO
"""

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from server.models import Lesson, Class, LessonVM
from server import db, redis_client, provider

bp = Blueprint("lesson_vm", __name__)


@bp.route("/", methods=["POST"])
@login_required
def bind_vm_to_lesson(class_id, lesson_id):
    """
    TODO
    """
    image = request.json["image"]
    flavor = request.json["flavor"]
    lesson = Lesson.query.filter_by(uuid=lesson_id).first()
    lesson.vm_image = image
    lesson.vm_flavor = flavor
    db.session.commit()
    return "Not Implemented", 400


@bp.route("/", methods=["DELETE"])
@login_required
def delete_vm_binding(class_id, lesson_id):
    """
    TODO
    """
    lesson = Lesson.query.filter_by(uuid=lesson_id).first()
    lesson.vm_image = None
    lesson.vm_flavor = None
    db.session.commit()
    return "Not Implemented", 400


@bp.route("/request", methods=["POST"])
@login_required
def request_vm(class_id, lesson_id):
    """
    TODO
    """
    class_data = Class.query.filter_by(uuid=class_id).first()
    lesson = Lesson.query.filter_by(uuid=lesson_id).first()
    vm = provider.create_vm(
        f"{class_data.slug}-{current_user.username}", lesson.vm_image, lesson.vm_flavor
    )
    vm_id = vm['server']['id']
    redis_client.setex(vm_id, 60 * 15, current_user.username)
    lesson_vm = LessonVM(lesson_id, vm_id, current_user.username)
    db.session.add(lesson_vm)
    db.session.commit()
    return "VM Created", 200


@bp.route("/renew", methods=["POST"])
@login_required
def renew_timer(class_id, lesson_id):
    """
    TODO
    """
    vm_id = str(LessonVM.query.filter_by(lesson_id=lesson_id, user=current_user.username).first().vm_id)
    redis_client.expire(vm_id, 60 * 15)
    return "Reset to 15 Minutes", 200


@bp.route("/console", methods=["POST"])
@login_required
def console(class_id, lesson_id):
    """
    TODO
    """
    vm_id = str(LessonVM.query.filter_by(lesson_id=lesson_id, user=current_user.username).first().vm_id)
    return provider.open_console(vm_id)


@bp.route("/teardown", methods=["POST"])
@login_required
def teardown_vm(class_id, lesson_id):
    """
    TODO
    """
    vm = LessonVM.query.filter_by(lesson_id=lesson_id, user=current_user.username).first()
    vm_id = str(vm.vm_id)
    redis_client.delete(vm_id)
    provider.delete_vm(vm_id)
    db.session.delete(vm)
    db.session.commit()
    return "VM Deleted", 200
