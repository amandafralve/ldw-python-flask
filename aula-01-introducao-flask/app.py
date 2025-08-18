# Importando o flask e render responsável por renderizar páginas
from flask import Flask, render_template 

# Criando uma instância do flask
app = Flask(__name__, template_folder='views') # __name__ representa o nome da aplicação/arquivo sendo executado

# Definindo a rota principal da aplicação '/'


@app.route('/')
def home(): # Função que será executada ao acessar a rota
        return render_template('index.html')


@app.route('/games')
def home():
        return render_template('games.html')

# Se for executado diretamente pelo interpretador, inicia servidor
if __name__ == '__main__':
    # Iniciando o servidor
    app.run(host="localhost", port=5000, debug=True)
