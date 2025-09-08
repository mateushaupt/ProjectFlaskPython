from flask import Blueprint, render_template, request, redirect
from ..models import User, db
hello_bp = Blueprint('hello', __name__)

@hello_bp.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@hello_bp.route('/newUser', methods=['POST'])
def newUser():
    username = request.form['username']

    newUser = User(username=username)
    db.session.add(newUser)
    db.session.commit()

    return redirect('/')



@hello_bp.route('/sobre')
def about():
    return "Olá, Gremista nato!"