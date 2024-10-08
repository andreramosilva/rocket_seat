from redis import Redis

class RedisConnectionHandler:
    def __init__(self):
        self.redis_conn = None

    def connect(self, host, port, db) -> Redis:
        self.redis_conn = Redis(host=host, port=port, db=db)
        return self.get_connection()

    def get_connection(self) -> Redis:
        return self.redis_conn

redis_connection_handler = RedisConnectionHandler()
redis_connection_handler.connect('localhost', 6379, 0)