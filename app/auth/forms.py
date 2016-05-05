from flask import Flask
from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, PasswordField, BooleanField, validators
from wtforms.validators import DataRequired, Length, Regexp


class LoginForm(Form):
	username = TextField('Email Address', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Keep me signed in')
	submit = SubmitField('Log In')

class SignupForm(Form):

	name = TextField('Name', validators=[DataRequired(), Length(1, 64), 
		Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
			'Usernames must have only letters, '
			'numbers, dots or underscores')])
	username = TextField('Email Address', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired(), validators.EqualTo('confirm', message="Passwords must match")])
	confirm = PasswordField('Repeat Password', validators=[DataRequired()])
	submit = SubmitField('Log In')

	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already exists.')
