from flask import render_template
from . import auth
from forms import LoginForm
from app.models import User

@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	form = LoginForm(request.form)
	if request.method == 'POST':
		user = User.query.filter_by(request.form['username']).first()
		if user is not None and user.verify_password(form.password.data):
			session['logged_in']
			return log_the_user_in(request.form['username'])
		else:
			error = 'Invalid username or password'

	return render_template('index.html', form=form, error=error)

@app.route('/register' , methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('signup.html')
    user = User(request.form['username'] , request.form['password'],request.form['email'])
    db.session.add(user)
    db.session.commit()

