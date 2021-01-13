import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
app.config['SECRET_KEY'] = "senhafoda"

########################################
###############BANCO DE DADOS###########
########################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)



########################################
###############BLUEPRINTS###############
########################################
from app.missao.views import missao
from app.funcionario.views import funcionario
from app.armamento.views import armamento
from app.principal.views import principal

app.register_blueprint(principal)
app.register_blueprint(funcionario, url_prefix="/funcionario")
app.register_blueprint(missao, url_prefix="/missao")
app.register_blueprint(armamento, url_prefix="/armamento")
