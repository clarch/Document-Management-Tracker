from flask import Flask, render_template, request
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from app import app

# @app.route('/', methods=['GET', 'POST'])
# def login():
# 	error = None
# 	if request.method == 'POST':
# 		if valid_login(request.form['username'],
# 						request.form['password']):
# 			return log_the_user_in(request.form['username'])
# 		else:
# 			error = 'Invalid username or password'

# 	return render_template('index.html', error=error)

