from flask import Flask, render_template, session, request, g, flash
from . import upload
from flask.ext.wtf import Form
from wtforms.ext.sqlalchemy.orm import model_form
from flask.ext.login import login_required
from ..models import Documents
from .forms import AddUrlBookmark
from .. import db
from app.auth.routes import session


@upload.route('/upload', methods=['GET', 'POST'])
def upload():
	form = AddUrlBookmark(request.form)
	if form.validate_on_submit():
		result = session.query(Documents).filter_by(url=form.url.data).first()
		if result:
			flash('Url already exists.', 'warning')
		else:
			bookmark = Documents(form.email.data, form.category.data, form.url.data, form.category.data)
			session.add(bookmark)
			session.commit()
			flash('Added!', 'success')
			render_template('upload/upload.html', form=form)
	return render_template('upload/upload.html', form=form)

# # @upload.route('/add_bookmark')
# # @login_required
# def add_bookmark(username):
#     """Add new bookmark to database."""
#     # import ipdb; ipdb.set_trace()
#     