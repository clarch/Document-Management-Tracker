from flask import Flask, Blueprint, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask_script import Manager

db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object('config')
	
	from .upload import upload
	app.register_blueprint(upload)

	bootstrap.init_app(app)

	from auth import auth
	app.register_blueprint(auth)

	db.init_app(app)
	with app.app_context():
		db.create_all()

	return app
