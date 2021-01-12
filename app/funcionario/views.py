from flask import Blueprint
from flask import render_template

funcionario = Blueprint('funcionario', __name__, template_folder='templates')

@funcionario.route("/funcionarios")
def funcionarios():
    return render_template('base_funcionarios.html')
