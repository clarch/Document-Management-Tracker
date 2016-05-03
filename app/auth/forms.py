from flask import Flask
from flask.ext.wtf import Form, TextField, TextAreaField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired

class LoginForm(Form):
	username = TextField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired])
	submit = SubmitField('Log In')