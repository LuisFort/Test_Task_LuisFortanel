from flask import Blueprint
#The blueprint is created and the routes are called.
distance = Blueprint('distance', __name__)
from . import routes
