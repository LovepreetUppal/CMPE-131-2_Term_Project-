from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField

from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('User', validators=[DataRequired()])
    password = PasswordField('Password')
    remember_me = BooleanField('Remember Me')

    submit = SubmitField('Sign in')

class SignupForm(FlaskForm):
    username = StringField('User', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()], id='email')
    password = PasswordField('Password')
    remember_me = BooleanField('Remember Me')

    submit = SubmitField('Sign up')

