from pymongo import MongoClient

class ConnectionHandler:
    def __init__(self, host, port):
        self.__connection_string = f"mongodb://{host}:{port}/"

    def get_client(self):
        return self.client

    def get_db(self, db_name):
        return self.client[db_name]