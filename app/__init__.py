from flask import Flask, render_template
from dotenv import load_dotenv

def create_app():
    load_dotenv()
    app = Flask(__name__)
    
    # Import & Register Blueprints
    from app.routes.analyzer import analyzer_bp
    from app.routes.generator import generator_bp
    
    app.register_blueprint(analyzer_bp)
    app.register_blueprint(generator_bp)
    
    @app.route('/')
    def index():
        return render_template('index.html')
        
    return app