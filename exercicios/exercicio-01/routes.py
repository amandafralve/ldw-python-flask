from flask import render_template, request, url_for, redirect

def init_app(app):
    
    
    @app.route('/')
    def home():
        return render_template('')