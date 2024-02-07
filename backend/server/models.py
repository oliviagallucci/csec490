from server import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Organization(db.Model):
    __tablename__ = "organizations"

    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String)
    slug = db.Column(db.String)
    
    classes = db.relationship('Class', backref='organization', lazy=True)

    def __init__(self, name, slug):
        self.name = name
        self.slug = slug

    def __repr__(self):
        return '<Organization %r>' % self.name


class Class(db.Model):
    __tablename__ = "classes"

    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String)
    slug = db.Column(db.String)
    visible = db.Column(db.Boolean, default=True)

    organization_id = db.Column(UUID(as_uuid=True), db.ForeignKey('organizations.uuid'))
    lessons = db.relationship('Lesson', backref='class', lazy=True)

    def __init__(self, name, organization_id):
        self.name = name
        self.organization_id = organization_id

    def __repr__(self):
        return '<Class %r>' % self.name


class Lesson(db.Model):
    __tablename__ = "lessons"

    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String)
    visible = db.Column(db.Boolean, default=True)
    config = db.Column(db.String)

    class_id = db.Column(UUID(as_uuid=True), db.ForeignKey('classes.uuid'))
    flags = db.relationship('Flag', backref='lesson', lazy=True)

    def __init__(self, name, class_id, config):
        self.name = name
        self.class_id = class_id
        self.config = config

    def __repr__(self):
        return '<Lesson %r>' % self.name

class Flag(db.Model):
    __tablename__ = "flags"

    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    type = db.Column(db.String)
    config = db.Column(db.String)
    points = db.Column(db.Integer)
    
    lesson_id = db.Column(UUID(as_uuid=True), db.ForeignKey('lessons.uuid'))

    def __init__(self, type, config, points, lesson_id):
        self.type = type
        self.config = config
        self.points = points
        self.lesson_id = lesson_id

    def __repr__(self):
        return '<Flag %r>' % self.type

class User(db.Model):
    __tablename__ = "users"

    username = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)
    email = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)

    def __init__(self, username, password, email, first_name, last_name):
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return "<User %r>" % self.username

