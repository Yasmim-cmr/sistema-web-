from flask import Blueprint
from flask import render_template

missao = Blueprint('missao', __name__, template_folder='templates')

@missao.route("/missoes")
def missoes():
    return render_template('base_missoes.html')
