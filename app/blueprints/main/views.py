from flask import Blueprint, render_template

bp = Blueprint('main', __name__, template_folder='templates')


@bp.route('/')
def index():
    return render_template('index.html')


from .views_pages import *
