from flask import Flask
from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, PasswordField, BooleanField, validators, SelectField
from wtforms.validators import DataRequired, Length, Regexp

class AddUrlBookmark(Form):	
	title = TextField(u'Title', validators=[DataRequired()])
	url = TextField('Url', validators=[DataRequired()])
	category = SelectField(u'Category', choices=[('Success', 'Success'), ('Training', 'Training'), ('Operations', 'Operations'), ('Finance', 'Finance'), ('Recruitment', 'Recruitment'), ('Sales', 'Sales'), ('Marketing', 'Marketing')], validators=[DataRequired()])
	add = SubmitField('Add')
