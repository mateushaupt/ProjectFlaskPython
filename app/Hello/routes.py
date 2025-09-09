from flask import Blueprint, render_template, request, redirect, url_for
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

@hello_bp.route('/deleteUser/<int:userId>', methods=['POST'])
def deleteUser(userId):
    user = User.query.get(userId)

    if user:
        db.session.delete(user)
        db.session.commit()

    return redirect(url_for('hello.index'))

@hello_bp.route('/editUser/<int:userId>', methods=['POST'])
def editUser(userId):
    user = User.query.get(userId)

    if user:
        user.username = request.form['newUsername']
        db.session.commit()

    return redirect(url_for('hello.index'))



@hello_bp.route('/sobre')
def about():
    return "Olá, Gremista nato!"