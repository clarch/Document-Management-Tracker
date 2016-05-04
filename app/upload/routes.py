from flask import Flask, render_template, session, request
from . import upload
from flask.ext.wtf import Form
from wtforms.ext.sqlalchemy.orm import model_form
from flask.ext.login import login_required
from ..models import Documents
from .forms import AddUrl


@upload.route('/upload')
def upload():
	form = AddUrl(request.form)
	return render_template('upload/upload.html', form=form)

# @login_required
# def add_bookmark(username):
#     """Add new bookmark to database."""
#     if username != g.user.username:
#         raise Forbidden
#     form = AddBookmarkForm()
#     if form.validate_on_submit():
#         try:
#             db.session.query(Bookmark).filter_by(url=form.url.data).one()
#             flash('Url already exists.', 'warning')
#         except NoResultFound:
#             img_name = get_url_thumbnail(form.url.data)
#             if img_name is None:
#                 img_name = 'default.png'
#             try:
#                 category = db.session.query(Category).filter_by(
#                     name=form.data.get('category', 'Uncategorized')).one()
#             except NoResultFound:
#                 category = Category(name=form.category.data)
#                 db.session.add(category)
#                 db.session.flush()
#             bookmark = Bookmark(title=form.title.data, url=form.url.data,
#                                 thumbnail=img_name, category_id=category._id,
#                                 user_id=g.user._id)
#             db.session.add(bookmark)
#             db.session.commit()
#             flash('Added!', 'success')
#     return render_template('add_bookmark.html', form=form)