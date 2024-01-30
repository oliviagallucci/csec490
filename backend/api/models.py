from api import db

class Organization(db.Model):
    __tablename__ = "organizations"

    id = db.Column(db.Integer, primary_key=True)
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

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id'))
    lessons = db.relationship('Lesson', backref='class', lazy=True)

    def __init__(self, name, organization_id):
        self.name = name
        self.organization_id = organization_id

    def __repr__(self):
        return '<Class %r>' % self.name


class Lesson(db.Model):
    __tablename__ = "lessons"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'))


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
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

