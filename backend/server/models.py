"""
Defines database models

Will convert into migrations
"""

import uuid
from passlib.hash import bcrypt
from slugify import slugify
from sqlalchemy.dialects.postgresql import UUID
from slugify import slugify
from server import db

# pylint: disable=too-few-public-methods


class Metadata(db.Model):
    """
    Organization metadata, should only be one row per instance
    """

    __tablename__ = "metadata"

    name = db.Column(db.String, primary_key=True)
    desc = db.Column(db.String)
    website = db.Column(db.String)

    def __init__(self, name, desc, website):
        self.name = name
        self.desc = desc
        self.website = website

    def __repr__(self):
        return f"<Metadata {self.name}>"


class Class(db.Model):
    """
    Classes in an organization
    Contains lessons
    """

    __tablename__ = "classes"

    # uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String)
    slug = db.Column(db.String, primary_key=True)
    visible = db.Column(db.Boolean, default=True)

    lessons = db.relationship("Lesson", backref="class", lazy=True)

    def json(self):
        """
        Convert to JSON
        """
        return {
            "id": self.uuid,
            "name": self.name,
            "slug": self.slug,
            "visible": self.visible,
        }

    def __init__(self, name):
        self.name = name
        self.slug = slugify(name)

    def __repr__(self):
        return f"<Class {self.name}>"


class Lesson(db.Model):
    """
    Lessons in a class
    Contains flags
    """

    __tablename__ = "lessons"

    # uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String)
    class_id = db.Column(db.String, db.ForeignKey("classes.slug"), primary_key=True)
    slug = db.Column(db.String, primary_key=True)
    visible = db.Column(db.Boolean, default=True)
    config = db.Column(db.String)
    visible = db.Column(db.Boolean, default=True)
    vm_image = db.Column(db.String)
    vm_flavor = db.Column(db.String)

    # class_id = db.Column(UUID(as_uuid=True), db.ForeignKey("classes.uuid"))
    flags = db.relationship("Flag", backref="lesson", lazy=True)

    def json(self):
        """
        Convert to JSON
        """
        return {
            "id": self.uuid,
            "name": self.name,
            "visible": self.visible,
            "config": self.config,
        }

    def __init__(self, name, class_id, config):
        self.name = name
        self.slug = slugify(name)
        self.class_id = class_id
        self.config = config

    def __repr__(self):
        return f"<Lesson {self.name}>"


class Flag(db.Model):
    """
    Flags in a lesson
    """

    __tablename__ = "flags"

    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    style = db.Column(db.String)
    config = db.Column(db.String)
    points = db.Column(db.Integer)

    class_id = db.Column(db.String, nullable=False)
    lesson_id = db.Column(db.String, nullable=False)

    __table_args__ = (
        db.ForeignKeyConstraint(['class_id', 'lesson_id'], ['lessons.class_id', 'lessons.slug'], name='fk_flag_lesson'),
    )

    def __init__(self, style, config, points, class_id, lesson_id):
        self.style = style
        self.config = config
        self.points = points
        self.class_id = class_id
        self.lesson_id = lesson_id

    def __repr__(self):
        return f"<Flag {self.uuid}>"

    def json(self):
        """
        Convert to JSON
        """
        return {
            "id": self.uuid,
            "style": self.style,
            "config": self.config,
            "points": self.points,
        }
<<<<<<< HEAD

    def __init__(self, style, config, points, lesson_id):
        self.style = style
        self.config = config
        self.points = points
        self.lesson_id = lesson_id

    def __repr__(self):
        return f"<Flag {self.uuid}>"


class LessonVM(db.Model):
    """
    VMs for lessons
    """

    __tablename__ = "lesson_vms"

    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    lesson_id = db.Column(UUID(as_uuid=True), db.ForeignKey("lessons.uuid"))
    vm_id = db.Column(UUID(as_uuid=True))
    user = db.Column(db.String, db.ForeignKey("users.username"))

    def __init__(self, lesson_id, vm_id, user):
        self.lesson_id = lesson_id
        self.vm_id = vm_id
        self.user = user

    def __repr__(self):
        return f"<LessonVM {self.uuid}>"


=======
      
>>>>>>> main
class User(db.Model):
    """
    Users in an organization
    """

    __tablename__ = "users"

    username = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)
    email = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    administrator = db.Column(db.Boolean)
    is_active = True
    is_authenticated = True

    permissions = db.relationship("Permissions", backref="user", lazy=True)

    def __init__(
        self, username, password, email, first_name, last_name
    ):  # pylint: disable=too-many-arguments
        self.username = username
        self.password = bcrypt.hash(password)
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.administrator = False

    def get_id(self):
        """
        Get user ID
        """
        return self.username

    def __repr__(self):
        return "<User {self.username}>"

    def has_permission(self, class_id, permission):
        """
        Check if user has given permissions in a class
        """
        return (
            Permissions.query.filter_by(username=self.username, class_id=class_id)
            .first()
            .bitmap()
            & permission.bitmap()
            == permission.bitmap()
        )


class Permissions(db.Model):
    # pylint: disable=too-many-instance-attributes
    """
    Permissions for users in classes
    """
    __tablename__ = "permissions"

    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String, db.ForeignKey("users.username"), nullable=False)
    class_id = db.Column(db.String, db.ForeignKey("classes.slug"), nullable=False)
    read_lessons = db.Column(db.Boolean)
    read_hidden_lessons = db.Column(db.Boolean)
    modify_lessons = db.Column(db.Boolean)
    read_user_info = db.Column(db.Boolean)
    modify_user_permissions = db.Column(db.Boolean)
    modify_class_data = db.Column(db.Boolean)

    def __init__(self, username, class_id, bitmap):
        self.username = username
        self.class_id = class_id
        self.read_lessons = bitmap & 0b100000
        self.read_hidden_lessons = bitmap & 0b010000
        self.modify_lessons = bitmap & 0b001000
        self.read_user_info = bitmap & 0b000100
        self.modify_user_permissions = bitmap & 0b000010
        self.modify_class_data = bitmap & 0b000001

    def __repr__(self):
        return "<Permission {self.uuid}>"

    def bitmap(self):
        """
        Convert permissions to bitmap
        """
        return int(
            self.read_lessons << 5
            | self.read_hidden_lessons << 4
            | self.modify_lessons << 3
            | self.read_user_info << 2
            | self.modify_user_permissions << 1
            | self.modify_class_data << 0
        )
