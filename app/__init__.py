from flask import *
from .Hello.routes import hello_bp
from .models import db
import os

def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.register_blueprint(hello_bp)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app