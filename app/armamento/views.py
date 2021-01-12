from flask import Blueprint
from flask import render_template

armamento = Blueprint('armamento', __name__, template_folder='templates')

@armamento.route("/armamentos")
def armamentos():
    return render_template('base_armamentos.html')
