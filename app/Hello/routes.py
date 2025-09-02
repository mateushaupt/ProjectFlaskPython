from flask import Blueprint, render_template
from ..models import User, db
hello_bp = Blueprint('hello', __name__)

@hello_bp.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@hello_bp.route('/sobre')
def about():
    return "Olá, Mateus"