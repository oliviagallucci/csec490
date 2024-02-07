from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate

app = Flask(__name__, static_folder=os.path.join(os.getcwd(), "static"))
app.url_map.strict_slashes = False

if os.path.exists(os.path.join(os.getcwd(), "config.py")):
    app.config.from_pyfile(os.path.join(os.getcwd(), "config.py"))
else:
    app.config.from_pyfile(os.path.join(os.getcwd(), "config.env.py"))

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .blueprints import api_bp
from .models import *

app.register_blueprint(api_bp, url_prefix='/api')

@app.route('/')
def index():
    return app.send_static_file('200.html')

@app.route('/<path>')
def not_index(path):
    return app.send_static_file('200.html')

@app.route('/static/<path:filename>')
def static_file(filename):
    return send_from_directory(os.path.join(os.getcwd(), "static"), filename)

@app.errorhandler(404)
def not_found(err):
    return "Page Not Found"


