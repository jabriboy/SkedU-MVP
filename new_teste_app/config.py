from flask import (
    Blueprint,
    render_template,
    url_for,
    redirect,
    request,
    flash,
    jsonify
)
from flask_login import (
    login_required,
    current_user
)
from . import db

config = Blueprint('config', __name__)

@config.route('/', methods=['POST', 'GET'])
@login_required
def add_person():
    
    return render_template('manegement.html')

