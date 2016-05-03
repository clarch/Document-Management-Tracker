from flask import Flask, render_template, request
from models import *


app = Flask(__name__)
wsgi_app = app.wsgi_app

@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if valid_login(request.form['username'],
						request.form['password']):
			return log_the_user_in(request.form['username'])
		else:
			error = 'Invalid username or password'

	return render_template('index.html', error=error)

# @app.signup('/signup', methods=['GET', 'POST'])
# def signup():
# 	pass


@app.route('/home')
def home():
	return render_template('home.html')


if __name__ == '__main__':
	app.run()
