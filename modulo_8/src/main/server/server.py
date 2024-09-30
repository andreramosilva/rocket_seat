from flask import Flask
from flask_cors import CORS
from src.models.sqllite.settings.connection import db_connection_handler
from src.main.server.routes import pets_routes


db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)
app.register_blueprint(pets_routes.pet_route_bp)
