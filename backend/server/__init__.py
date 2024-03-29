"""
Iniitlaize flask app
"""
 # pylint: disable=cyclic-import
import os
from flask import Flask, send_from_directory, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, static_folder=os.path.join(os.getcwd(), "static"))
app.url_map.strict_slashes = False

if os.path.exists(os.path.join(os.getcwd(), "config.py")):
    app.config.from_pyfile(os.path.join(os.getcwd(), "config.py"))
else:
    app.config.from_pyfile(os.path.join(os.getcwd(), "config.env.py"))

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# pylint: disable=wrong-import-position
from .blueprints import api_bp
from .models import *

app.register_blueprint(api_bp, url_prefix="/api")

@app.route("/", defaults={"_path": ""})
@app.route("/<path:_path>")
def index(_path):
    """
    Default serve frontend
    """
    return send_file(os.path.join(os.getcwd(), "200.html"))


@app.route("/favicon.png")
def favicon():
    """
    Serve favicon
    """
    return send_file(os.path.join(os.getcwd(), "favicon.png"))


@app.errorhandler(404)
def not_found(_err):
    """
    404 handler
    """
    return "Page Not Found"
