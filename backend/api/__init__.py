from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.url_map.strict_slashes = False

if os.path.exists(os.path.join(os.getcwd(), "config.py")):
    app.config.from_pyfile(os.path.join(os.getcwd(), "config.py"))
else:
    app.config.from_pyfile(os.path.join(os.getcwd(), "config.env.py"))

db = SQLAlchemy(app)

from .blueprints import api_bp

app.register_blueprint(api_bp, url_prefix='/api')

@app.errorhandler(404)
def not_found(err):
    return "Page Not Found"

