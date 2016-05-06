#Blueprint for the routes for boomarks manipulation
from flask import Blueprint

bookmarks = Blueprint('bookmarks', __name__)

from . import routes

