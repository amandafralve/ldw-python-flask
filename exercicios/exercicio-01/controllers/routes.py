from flask import render_template, request, url_for, redirect

def init_app(app):
    
    
    @app.route('/')
    def home():
        return render_template('index.html')

    especies = ['Calathea', 'Pothus']
    plantsList = [
        {
            'Nome Cientifico': 'Monstera Deliciosa',
            'Nome Popular': 'Costela de Adão',
            'Luminosidade': 'Meia-Sombra',
            'Rega': '2 vezes por semana',
            'Adubação': 'Intervalo de 90 dias'
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
        receitasAdubo = {'receita': 1, 'descricao': '300ml de água, ½ colher de cúrcuma, ½ colher de canela em pó'}
        
        return render_template('plants.html', receitasAdubo=receitasAdubo, plantsList=plantsList, nomeCientifico=nomeCientifico, nomePop=nomePop, luz=luz, rega=rega, adubacao=adubacao, especies=especies)
    
    
    @app.route('/new-plant', methods=['GET','POST'])
    def newPlant():
        
        if request.method == 'POST':
            if request.form.get('nomeCientifico') and request.form.get('nomePop') and request.form.get('luz') and request.form.get('rega') and request.form.get('adubacao'):
                plantsList.append({'Nome Científico:': request.form.get('nomeCientifico:'), 'Nome Popular:': request.form.get('nomePop'), 'Luminosidade:': request.form.get('luz'),
                                'Rega:': request.form.get('rega'), 'Adubação:':request.form.get('adubacao')})
            return redirect(url_for('newPlant'))
        return render_template('newPlant.html', plantsList=plantsList)
    