from flask import render_template, redirect, request, url_for, flash
from sqlalchemy.orm import sessionmaker, scoped_session
from flask.ext.login import login_user, logout_user, login_required, current_user, LoginManager
from . import auth
from ..models import User, engine, metadata
from .forms import LoginForm, SignupForm


con = engine.connect()
Session = sessionmaker(bind=con)
session = scoped_session(Session)

# @login_manager.user_loader
# def load_user(id):
#     return User.get(id)

@auth.route('/login', methods=['GET', 'POST'])
def loginuser():
  form = LoginForm(request.form)
  # import ipdb; ipdb.set_trace()
  if request.method == 'POST':
    if form.validate_on_submit():
        user = session.query(User).filter_by(email=form.usermail.data).first()
        if user is not None:
            return redirect(url_for('bookmarks.urldata'))
        flash('Invalid username or password.')
    else:
      for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))
  return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required

def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('auth.loginuser'))


@auth.route('/signup', methods=['GET', 'POST'])
def signupuser():
  form = SignupForm(request.form)

  if request.method == 'POST':

    if form.validate() == False:
      return render_template('auth/signup.html', form=form)

    else:
      user = session.query(User).filter_by(email=form.email.data).first()
      if user is not None:
        flash('You have signed up successfuly')
        return redirect(url_for('bookmarks.urldata'))
      else:
        newuser = User()
        newuser.name = form.name.data
        newuser.email = form.email.data
        newuser.password = form.password.data
        session.add(newuser)
        session.commit()  

      return render_template('auth/login.html', form=form)
   
  elif request.method == 'GET':
    return render_template('auth/signup.html', form=form)

  else:
      for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))



