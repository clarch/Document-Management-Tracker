#Registering The routes, db, and bootstrap 
from flask import Flask, Blueprint, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager


db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object('config')
	
	from .bookmarks import bookmarks
	app.register_blueprint(bookmarks)

	bootstrap.init_app(app)

	login_manager.init_app(app)

	from auth import auth
	app.register_blueprint(auth)

	db.init_app(app)
	with app.app_context():
		db.create_all()

	return app
