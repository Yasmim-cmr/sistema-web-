from app import app, db

class Auxiliar(db.Model):
    __tablename__ = "auxiliar"
    
    id                  = db.Column(db.Integer, primary_key=True)
    nome                = db.Column(db.String(100), nullable=False)
    descrição           = db.Column(db.String(50))
    



