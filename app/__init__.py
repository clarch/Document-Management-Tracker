from flask import Flask, Blueprint, render_template
from app.upload import upload
from app.auth import auth

app = Flask(__name__)

app.register_blueprint(upload)
app.register_blueprint(auth)

