from app import app
from flask import render_template


@app.route("/")
def index():
    return render_template('base_inicial.html')

@app.route("/funcionarios")
def funcionarios():
    return render_template('base_funcionarios.html')

@app.route("/missoes")
def missoes():
    return render_template('base_missoes.html')

@app.route("/armamento")
def armamento():
    return render_template('base_armamento.html')


