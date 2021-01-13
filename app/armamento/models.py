from app import app, db

class Armamento(db.Model):
    __tablename__ = "armamento"
    
    id                  = db.Column(db.Integer, primary_key=True)
    nome                = db.Column(db.String(100), nullable=False)
    tipo                = db.Column(db.String(20))
    valor               = db.Column(db.String(11))
    cartucho            = db.Column(db.String(15))
    penetrabilidade     = db.Column(db.String(15))
    cadência_de_tiro    = db.Column(db.String(30))
    