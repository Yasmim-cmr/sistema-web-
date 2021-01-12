from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


maneger = Manager(app)
maneger.add_command('db', MigrateCommand)
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