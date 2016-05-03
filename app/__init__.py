from flask import Flask, Blueprint, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from app.upload import upload
from app.auth import auth

app = Flask(__name__)

app.config.from_object('config')
db = SQLAlchemy(app)
app.register_blueprint(upload)
app.register_blueprint(auth)

