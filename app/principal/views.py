from flask import Blueprint
from flask import render_template

principal = Blueprint('principal', __name__)

@principal.route("/")
def index():
    return render_template('base_inicial.html')


