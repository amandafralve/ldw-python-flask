# Importando o Flask no pacote API
from flask import Flask
#IMportando o Flask Restful
from flask_restful import Api
#Importando pymongo
from flask_pymongo import PyMongo
#Importando o flask marshmallow
from flask_marshmallow import Marshmallow
#Carregando o Flask na variável app
app = Flask(__name__)

#Carregando o pacote Api do Flask restful na variável api
api=Api(app)
#Setando endereço do banco mongodb
app.config["MONGO_URI"] = 'mongodb://localhost:27017/api-movies'
#Carregando o pymongo na variável mongo
mongo = PyMongo(app)
#Carregando marshmallow
marsh = Marshmallow(app)

#importando os recursos
from .resources import movie_resources