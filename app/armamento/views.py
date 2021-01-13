from flask import Blueprint
from flask import render_template, request, redirect, url_for
from app import db
from app.armamento.models import Armamento




armamento = Blueprint('armamento', __name__, template_folder='templates')

@armamento.route("/armamentos")
def armamentos():
    return render_template('base_armamentos.html')

@armamento.route('/cadastrar_arma',  methods=['GET','POST'])
def cadastrar_arma():
    if request.method == 'POST':
        nome_arma = request.form['nome_arma']
        tipo = request.form['tipo']
        valor  = request.form['valor']
        cartucho  = request.form['cartucho']
        penetrabilidade  = request.form['penetrabilidade']
        cadência_de_tiro = request.form['cadência_de_tiro']


        armamento = Armamento(nome_arma = nome_arma,
                              tipo = tipo,
                              valor = valor,
                              cartucho = cartucho,
                              penetrabilidade = penetrabilidade,
                              cadência_de_tiro = cadência_de_tiro)
        db.session.add(armamento)
        db.session.commit()

        return redirect(url_for('armamento.armamentos'))
    return render_template('form_armamentos.html')