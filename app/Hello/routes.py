from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models import User, db
from .forms import UserForm

hello_bp = Blueprint('hello', __name__)

@hello_bp.route('/')
def index():
    users = User.query.all()
    form = UserForm()
    return render_template('index.html', users=users, form=form)

@hello_bp.route('/newUser', methods=['POST'])
def newUser():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data

        newUser = User(username=username)
        db.session.add(newUser)
        db.session.commit()
        flash('Usuário criado com sucesso!', 'success')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'Erro no campo ({getattr(form,field).label.text}): {error}', 'danger')

    return redirect(url_for('hello.index'))

@hello_bp.route('/deleteUser/<int:userId>', methods=['POST'])
def deleteUser(userId):
    user = User.query.get_or_404(userId)

    if user:
        db.session.delete(user)
        db.session.commit()
        flash('Usuário removido com sucesso!', 'success')
    
    return redirect(url_for('hello.index'))

@hello_bp.route('/editUser/<int:userId>', methods=['POST'])
def editUser(userId):
    user = User.query.get_or_404(userId)
    form = UserForm()
    if form.validate_on_submit():
        user.username = form.username.data
        db.session.commit()
        flash('Usuário atualizado com sucesso!', 'success')

    return redirect(url_for('hello.index'))



@hello_bp.route('/sobre')
def about():
    return "Olá, Gremista nato!"