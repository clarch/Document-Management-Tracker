from flask import Flask
from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, PasswordField, BooleanField, validators, SelectField
from wtforms.validators import DataRequired, Length, Regexp

class AddUrl(Form):	
	title = TextField(u'Title', validators=[DataRequired()])
	url = TextField('Url', validators=[DataRequired()])
	category = SelectField(u'Category', choices=[('name', 'me'), ('one', 'of'), ('the', 'val')], validators=[DataRequired()])
	description = TextAreaField('Description')
	add = SubmitField('Add')