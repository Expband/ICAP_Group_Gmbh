from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class Register(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    surename = StringField('surename', validators=[DataRequired()])
    login = StringField('login', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
