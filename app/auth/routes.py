from flask import render_template, redirect, request, url_for, flash
from sqlalchemy.orm import sessionmaker, scoped_session
from flask.ext.login import login_user, logout_user, login_required
from . import auth
from ..models import User, engine, metadata
from .forms import LoginForm, SignupForm
from flask_login import LoginManager

login_manager = LoginManager()

con = engine.connect()
Session = sessionmaker(bind=con)
session = scoped_session(Session)

@login_manager.user_loader
def load_user(id):
    return User.get(id)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember.data)
            return redirect(url_for('bookmark.bookmark'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('auth.login'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignupForm()

  if request.method == 'POST':

    if form.validate() == False:
      return render_template('auth/signup.html', form=form)

    else:

      newuser = User()
      newuser.name = form.name.data
      newuser.username = form.email.data
      newuser.password = form.password.data
      session.add(newuser)
      session.commit()  

      return render_template('auth/login.html')
   
  elif request.method == 'GET':
    return render_template('auth/signup.html', form=form)

# @auth.before_request
# def load_user():
#     if session["username"]:
#         user = User.query.filter_by(username=session["username"]).first()
#     else:
#         user = anonymous  # Make it better, use an anonymous User instead

#     g.user = user

