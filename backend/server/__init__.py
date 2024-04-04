"""
Iniitlaize flask app
"""

# pylint: disable=cyclic-import
import os
from os import environ as env
from flask import Flask, send_from_directory, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import redis

app = Flask(__name__, static_folder=os.path.join(os.getcwd(), "static"))
app.url_map.strict_slashes = False

if os.path.exists(os.path.join(os.getcwd(), "config.py")):
    app.config.from_pyfile(os.path.join(os.getcwd(), "config.py"))
else:
    app.config.from_pyfile(os.path.join(os.getcwd(), "config.env.py"))

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
redis_client = redis.StrictRedis(host=app.config["REDIS_HOST"], port=6379, db=0)
redis_client.config_set("notify-keyspace-events", "Ex")
provider = None
if app.config["VM_PROVIDER"] == "openstack":
    from .providers.openstack import OpenStackProvider
    provider = OpenStackProvider()

# pylint: disable=wrong-import-position
from .blueprints import api_bp
from .models import *

app.register_blueprint(api_bp, url_prefix="/api")


@login_manager.user_loader
def load_user(username):
    # Replace this with your actual code to load a user from a database or other source
    return User.query.filter_by(username=username).first()

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
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


def loop_redis_expirations():
    """
    Updates when VM expire so they can be deleted
    """
    # Subscribe to expiration notifications
    pubsub = redis_client.pubsub()
    pubsub.psubscribe("__keyevent@0__:expired")

    # Listen for expiration events
    for message in pubsub.listen():
        if message["type"] == "pmessage":
            expired_vmid = message["data"].decode("utf-8")
            provider.delete_vm(expired_vmid)
