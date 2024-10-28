from flask import Flask
from .routes import main_routes
from .auth import auth_routes
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register Blueprints
    app.register_blueprint(main_routes)
    app.register_blueprint(auth_routes)

    return app
