from app import app, db

class Funcionario(db.Model):
    __tablename__ = "funcionario"
    
    id                  = db.Column(db.Integer, primary_key=True)
    nome                = db.Column(db.String(100), nullable=False)
    codinome            = db.Column(db.String(20))
    data_de_nascimento  = db.Column(db.String(11))
    cpf                 = db.Column(db.String(15))
    rg                  = db.Column(db.String(15))
    estado_civil        = db.Column(db.String(30))
    escolaridade        = db.Column(db.String(50))
    endereço            = db.Column(db.String(70))
    habilidades         = db.Column(db.String(60))
    celular             = db.Column(db.String(12))
    email               = db.Column(db.String(25))
    salario             = db.Column(db.String(20))
    
    missoes_presente    = db.Column(db.String(20))




