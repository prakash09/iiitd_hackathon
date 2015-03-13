from flask import Blueprint

hacks = Blueprint('hacks', __name__)

from . import routes

