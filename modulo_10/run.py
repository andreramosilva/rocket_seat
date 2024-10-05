from src.main.server.server import app
from src.models.connections.mongodb_connection import db_connection

if __name__ == '__main__':
    db_connection.connect()
    app.run(host="0.0.0.0",port=3000,debug=True)