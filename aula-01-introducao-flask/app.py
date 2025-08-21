# Importando o flask e render responsável por renderizar páginas
from flask import Flask, render_template 
from controllers import routes

# Criando uma instância do flask
app = Flask(__name__, template_folder='views') # __name__ representa o nome da aplicação/arquivo sendo executado
routes.init_app(app)


# Se for executado diretamente pelo interpretador, inicia servidor
if __name__ == '__main__':
    # Iniciando o servidor
    app.run(host="localhost", port=5000, debug=True)

