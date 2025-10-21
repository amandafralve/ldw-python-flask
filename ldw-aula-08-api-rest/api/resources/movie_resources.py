# Importando classe resource do Flask Restful
from flask_restful import Resource
#Importando a variavel api do pacote api
from api import api

#importando pacotes
from flask import make_response, jsonify
#Importando schemas
from ..schemas import movie_schemas
# Imp model
from ..models import movie_model
#Imp services
from ..services import movie_service

#Criando os recursos de filme
class MoviesList(Resource):
    # MÉTODO GET: listar
    def get(self):
        movies = movie_service.get_movies()
        movieSchema = movie_schemas.MovieSchema(many=True)
        return make_response(movieSchema.jsonify)
    

api.add_resource(MoviesList, '/movies')
