from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nomeCientifico = db.Column(db.String(150))
    nomePop = db.Column(db.String(150))
    luz = db.Column(db.String(150))
    rega = db.Column(db.String(150))
    adubacao = db.Column(db.String(150))
    
    def __init__(self, nomeCientifico, nomePop, luz, rega, adubacao):
        self.nomeCientifico = nomeCientifico
        self.nomePop = nomePop
        self.luz = luz
        self.rega = rega
        self.adubacao = adubacao
        
class Receipt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    