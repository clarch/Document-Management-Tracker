from flask import render_template, redirect, request, url_for, flash, session
from flask.ext.login import login_user, logout_user, login_required
from . import auth
from .. import db
from ..models import User
from .forms import LoginForm, SignupForm
from flask_login import LoginManager

login_manager = LoginManager()

@login_manager.user_loader
def load_user(id):
    return User.get(id)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember.data)
            return redirect(url_for('auth.login'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)


# @auth.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     flash('You have been logged out.')
#     return redirect(url_for('issue.index'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignupForm()

  if request.method == 'POST':
    if form.validate() == False:
      return render_template('auth/signup.html', form=form)
    else:
      newuser = User()
      newuser.name = form.name.data
      newuser.username = form.username.data
      newuser.password = form.password.data
      db.session.add(newuser)
      db.session.commit()
       
      return render_template(url_for('auth.login'))
   
  elif request.method == 'GET':
    return render_template('auth/signup.html', form=form)

# @auth.before_request
# def load_user():
#     if session["username"]:
#         user = User.query.filter_by(username=session["username"]).first()
#     else:
#         user = anonymous  # Make it better, use an anonymous User instead

#     g.user = user

