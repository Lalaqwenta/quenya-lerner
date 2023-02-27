from flask import render_template
from flask import Blueprint

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')
    