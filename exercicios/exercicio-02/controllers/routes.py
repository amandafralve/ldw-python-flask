from flask import render_template, request, url_for, redirect
import urllib, json
import requests, os
from dotenv import load_dotenv

# Carregando arquivo .env 
load_dotenv()
# Acessando a variável
api_key = os.getenv("API_KEY")

def init_app(app):
    
    
    @app.route('/')
    def home():
        return render_template('index.html')

    especies = ['Calathea', 'Pothus']
    plantsList = [
        {
            'nomeCientifico': 'Monstera deliciosa',
            'nomePop': 'Costela de Adão',
            'luz': 'Meia-sombra',
            'rega': '2 vezes por semana',
            'adubacao': 'Intervalo de 90 dias'
        }
    ]
    
    
    @app.route('/plants', methods=['GET','POST'])
    def plants():
        nomeCientifico = 'Monstera Deliciosa'
        nomePop = 'Costela de Adão'
        luz = 'Meia-Sombra'
        rega = '2 vezes por semana'
        adubacao = 'Intervalo de 90 dias'
        
        # Requisição POST com request
        if request.method == 'POST':
            if request.form.get('especie'):
                especies.append(request.form.get('especie'))
                return redirect(url_for('plants'))
            
        #Dicionário
        receitasAdubo = {'Receita': 1, 'Descrição': '300ml de água, ½ colher de cúrcuma, ½ colher de canela em pó'}
        
        return render_template('plants.html', receitasAdubo=receitasAdubo, plantsList=plantsList, nomeCientifico=nomeCientifico, nomePop=nomePop, luz=luz, rega=rega, adubacao=adubacao, especies=especies)
    
    
    @app.route('/new-plant', methods=['GET','POST'])
    def newPlant():
        
        if request.method == 'POST':
            if request.form.get('nomeCientifico') and request.form.get('nomePop') and request.form.get('luz') and request.form.get('rega') and request.form.get('adubacao'):
                plantsList.append({
                        'nomeCientifico': request.form.get('nomeCientifico'),
                        'nomePop': request.form.get('nomePop'),
                        'luz': request.form.get('luz'),
                        'rega': request.form.get('rega'),
                        'adubacao': request.form.get('adubacao')
                    })
            return redirect(url_for('newPlant'))
        return render_template('newPlant.html', plantsList=plantsList)
    
    @app.route('/apiplants', methods=['GET', 'POST'])
    def apiPlants():
        print("Rota /apiplants chamada!")  
        #url = 'https://perenual.com/api/species-care-guide-list'
        url = f'https://perenual.com/api/species-list?key={api_key}'
        
        response = requests.get(url)
        
        print(f"Status code da requisição: {response.status_code}")

        data = response.json()
        plants = data.get("data", [])
    
        return render_template('apiplants.html', plantsjson=plants)