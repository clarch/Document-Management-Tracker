from flask import Flask, Blueprint, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

db = SQLAlchemy()

def create_app():
	app = Flask(__name__)
	app.config.from_object('config')
	
	migrate = Migrate(app, db)
	manager = Manager(app)
	manager.add_command('db', MigrateCommand)

	from .upload import upload
	app.register_blueprint(upload)

	from auth import auth
	app.register_blueprint(auth)

	db.init_app(app)
	
	return app
