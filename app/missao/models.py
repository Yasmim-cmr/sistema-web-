from app import app, db

class Missao(db.Model):
    __tablename__ = "missao"
    
    id                      = db.Column(db.Integer, primary_key=True)
    nome_missao             = db.Column(db.String(100), nullable=False)
    data                    = db.Column(db.String(20))
    local                   = db.Column(db.String(11))
    cliente                 = db.Column(db.String(15))
    status                  = db.Column(db.String(20))

    arsenal                 = db.Column(db.String(20))
    agentes_responsaveis    = db.Column(db.String(20))



 #(nome, data, local (com coordenadas) cliente, agente(s) responsável(eis) (deve-se poder criar sem agentes selecionados também), arsenal (deve-se poder criar sem arsenal selecionado também), status (completada, falhada, em aberto, em execução) e uma breve descrição)#