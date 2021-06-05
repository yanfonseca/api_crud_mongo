from sanic import Sanic
from sanic.response import json
from app.routes import database_bp

def create_app(name):
    app = Sanic(name=name)
    app.blueprint(database_bp)
    return app