from flask import Blueprint
from flask import render_template, request, redirect, url_for
from app import db
from app.funcionario.models import Funcionario




funcionario = Blueprint('funcionario', __name__, template_folder='templates')

@funcionario.route("/")
def index():
    funcionarios = Funcionario.query.all()
    return render_template('base_funcionarios.html', funcionarios_front  = funcionarios)

@funcionario.route('/cadastrar_funcionario', methods=['GET','POST'])
def cadastrar_funcionario():
    if request.method =='POST':
        nome = request.form['nome']
        codinome = request.form['codinome']
        data_de_nascimento = request.form['data_de_nascimento']
        cpf = request.form['cpf']
        rg = request.form['rg']
        estado_civil = request.form['estado_civil']
        escolaridade = request.form['escolaridade']
        endereço = request.form['endereço']
        habilidades = request.form['habilidades']
        celular = request.form['celular']
        email = request.form['email']
        salario = request.form['salario']

        
        
        funcionario = Funcionario(nome = nome,
                                  codinome = codinome,
                                  data_de_nascimento = 
                                  data_de_nascimento,
                                  cpf = cpf,
                                  rg = rg,
                                  estado_civil = estado_civil,
                                  escolaridade = escolaridade,
                                  endereço = endereço,
                                  habilidades = habilidades,
                                  celular = celular,
                                  email = email,
                                  salario = salario)
        db.session.add(funcionario)
        db.session.commit()

        return redirect(url_for('funcionario.index'))            
    return render_template('form_funcionarios.html')

@funcionario.route('/perfil/<_id>', methods=['GET'])
def perfil(_id):
    funcionario = Funcionario.query.get_or_404(_id)

    return render_template('info_funcionarios.html', funcionario = funcionario)




    