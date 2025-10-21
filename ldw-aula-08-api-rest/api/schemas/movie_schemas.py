# Importando o Marchmallow
from api import marsh
from marshmallow import fields

#Definindo os tipos de dados e quais sao obrigatorios (required=True)
class MovieSchema(marsh.Schema):
    _id = fields.Str()
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    year = fields.Int(required=True)
    duration = fields.Int(required=True)
    