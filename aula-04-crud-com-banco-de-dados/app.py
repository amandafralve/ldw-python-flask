# Importando o flask e render responsável por renderizar páginas
from flask import Flask, render_template 
# Importando Controllerss
from controllers import routes
# Importando Models
from models.database import db
# Importando a biblioteca para manipulação da SO
import os

# Criando uma instância do flask
app = Flask(__name__, template_folder='views') # __name__ representa o nome da aplicação/arquivo sendo executado
routes.init_app(app)

# Extrair o diretório absoluto do projeto
dir = os.path.abspath(os.path.dirname(__file__))
# Criando o arquivo do banco
app.config['SQLALCHEMY+DATABASE_URI'] = 'sqlite:///'+ os.path.join(dir, 'models/games.sqlite3')

# Se for executado diretamente pelo interpretador, inicia servidor
if __name__ == '__main__':
    # Enviando o flask para o sqlAlchemy
    db.init_app(app=app)
    # Verificar no inicio da aplicação se o banco ja existe, se n ele cria
    with app.test_request_context():
        db.create_all()
    
    # Iniciando o servidor
    app.run(host="localhost", port=5000, debug=True)

