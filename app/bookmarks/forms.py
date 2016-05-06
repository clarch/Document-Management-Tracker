from flask import Flask
from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, PasswordField, BooleanField, validators, SelectField
from wtforms.validators import DataRequired, Length, Regexp
from wtforms.pewee import CharField

#Add a url to the database
class AddUrlBookmark(Form):	
	title = TextField(u'Title', validators=[DataRequired()])
	url = TextField('Url', validators=[DataRequired()])
	category = SelectField(u'Category', choices=[('Success', 'Success'), ('Training', 'Training'), ('Operations', 'Operations'), ('Finance', 'Finance'), ('Recruitment', 'Recruitment'), ('Sales', 'Sales'), ('Marketing', 'Marketing')], validators=[DataRequired()])
	slug = CharField(unique=True)

	