from flask import render_template, request, url_for, redirect

def init_app(app):
    
    
    @app.route('/')
    def home():
        return render_template('index.html')
    
    @app.route('/plants')
    def plants():
        return render_template('plants.html')
    
    @app.route('/new-plant')
    def newPlant():
        return render_template('newPlant.html')
    