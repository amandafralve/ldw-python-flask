from flask import render_template, request, redirect, url_for
import urllib, json

def init_app(app):
    # Definindo a rota principal da aplicação '/'


    @app.route('/')
    def home(): # Função que será executada ao acessar a rota
        return render_template('index.html')


    # Lista em Python (array)
    players = ['Yan', 'Ferrari', 'Valéria', 'Amanda']
    # Lista de Jogos
    gamelist = [{'Título': 'Hollow Knight', 'Ano':2015, 'Categoria': 'Plataforma'}]


    @app.route('/games', methods=['GET', 'POST'])
    def games():
        title = 'Tarisland'
        year = 2022
        category = 'MMORGP'
        
        #Tratando uma requisição POST com request
        if request.method == 'POST':
            # Coletando otexto do input 
            if request.form.get('player'): #Se a caixa player for != de vazio, a lista de jogadores será chamada
                players.append(request.form.get('player'))
                return redirect(url_for('games'))

        # Dicionário em Python (objeto)
        console = {'name': 'Playstation 5', 'manufacturer': 'Sony', 'year': 2020}
        return render_template('games.html', title=title, year=year, category=category, players=players, console=console)


    @app.route('/new-game', methods=['GET', 'POST'])
    def newgame():
        
        # Tratamento da requisição POST
        if request.method == 'POST':
            # Checagem de campos um por um
            if request.form.get('title') and request.form.get('year') and request.form.get('category'):
                gamelist.append({'Título': request.form.get('title'),'Ano': request.form.get('year'), 
                                'Categoria': request.form.get('category')})
                return redirect(url_for('newgame'))
        return render_template('newGame.html', gamelist=gamelist)
    
    
    @app.route('/apigames', methods=['GET', 'POST'])
    #Criando parâmetros para a rota
    @app.route('/apigames/<int:id>', methods=['GET', 'POST'])
    
    def apigames(id=None): # none torna parâmetro opcional
        url = 'https://www.freetogame.com/api/games'
        response = urllib.request.urlopen(url)
        data = response.read()
        gameslist = json.loads(data)
        
        
        # Verificando se o parâmetro foi ligado
        if id:
            gameInfo = []
            for game in gameslist:
                if game['id'] == id: #Comparando os IDs (se bate com o da lista)
                    gameInfo = game
                    break
            if gameInfo:
                return render_template('gameinfo.html', gameInfo=gameInfo)
            else:
                return f'Game com a ID {id} não foi encontrado.'
        else:
            return render_template('apigames.html', gameslist=gameslist)