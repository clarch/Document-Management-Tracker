from flask import Flask, render_template, session, request, g, flash, redirect
from . import bookmarks
from flask.ext.wtf import Form
from wtforms.ext.sqlalchemy.orm import model_form
from flask.ext.login import login_user, logout_user, login_required
from ..models import Documents
from .forms import AddUrlBookmark
from .. import db
from app.auth.routes import session

@bookmarks.route('/bookmarks', methods=['GET', 'POST'])
# @login_required
def addurl():
	form = AddUrlBookmark(request.form)
	if form.validate_on_submit():
		result = session.query(Documents).filter_by(url==form.url.data).first()
		if result:
			flash('Url already exists.', 'warning')
		else:
			bookmark = Documents(form.title.data, form.url.data, form.category.data)
			session.add(bookmark)
			session.commit()
			flash('Added!', 'success')
			return redirect('/urldata')
	return render_template('bookmarks/bookmarks.html', form=form)


@bookmarks.route('/urldata', methods=['GET', 'POST'])
# @login_required
def urldata():
	form = AddUrlBookmark(request.form)
	urldata = session.query(Documents).all()
	return render_template('bookmarks/bookmarks.html', urldata=urldata, form=form)  