import sqlite3
from sqlite3 import Connection as SqliteConnection

class SqliteConnectionHandler:
    def __init__(self):
        self.__connection_string = "storage.db"
        self.__conn = None
    def connect(self)-> SqliteConnection:
        self.__conn = sqlite3.connect(self.__connection_string, check_same_thread=False)
        return self.get_connection()
    def get_connection(self)-> SqliteConnection:
        return self.__conn