from flask import Blueprint

dept = Blueprint('dept', __name__, )

from . import view
