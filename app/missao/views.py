from flask import Blueprint
from flask import render_template, request, redirect, url_for
from app import db
from app.missao.models import Missao


missao = Blueprint('missao', __name__, template_folder='templates')

@missao.route("/")
def index():
    return render_template('base_missoes.html')

@missao.route('/cadastrar_missao', methods=['GET','POST'])
def cadastrar_missao():
    if request.method == 'POST':
        nome_missao             = request.form['nome_missao']
        data                    = request.form['data']
        local                   = request.form['local']
        cliente                 = request.form['cliente']
        status                  = request.form['status']
        arsenal                 = request.form['arsenal']
        agentes_responsaveis    = request.form['']

        missao = Missao(nome_missao = nome_missao,
                        data = data,
                        local = local,
                        cliente = cliente,
                        status = status,
                        arsenal = arsenal,
                        agentes_responsaveis = agentes_responsaveis)
        db.session.add(missao)
        db.session.commit()
        
        return redirect(url_for('missao.index'))
    return render_template('form_missoes.html')


