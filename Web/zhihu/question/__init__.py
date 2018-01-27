from flask import Blueprint

question = Blueprint('dept', __name__, )

from . import view
