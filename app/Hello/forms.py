from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class UserForm(FlaskForm):
    username = StringField('Nome do sócio', validators=[DataRequired(message='O nome é obrigatório')])
    submit = SubmitField()
    