from flask import Flask
from src.models.redis.settings.connection import RedisConnectionHandler
from src.models.sqlite.settings.connection import SqliteConnectionHandler
from src.main.routes.products_routes import products_routes_bp

redis_conn_handler = RedisConnectionHandler()
sqlite_conn_handler = SqliteConnectionHandler()

redis_conn_handler.connect('localhost', 6379, 0)
sqlite_conn_handler.connect()

app = Flask(__name__)

app.register_blueprint(products_routes_bp)
