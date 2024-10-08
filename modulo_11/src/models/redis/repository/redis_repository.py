from redis import Redis

class RedisRepository:
    def __init__(self, redis_conn: Redis)-> None:
        self.redis_conn = redis_conn

    def insert(self, key: str, value: any) -> None:
        self.redis_conn.set(key, value)

    def get_key(self, key: str) -> str:
        value = self.redis_conn.get(key)
        return value.decode("utf-8") if value else None

    def delete_key(self, key: str) -> None:
        self.redis_conn.delete(key)

    def insert_hash(self, key: str, field: str, value: any) -> None:
        self.redis_conn.hset(key, field, value)

    def get_hash(self, key: str, field: str) -> str:
        value = self.redis_conn.hget(key, field)
        return value.decode("utf-8") if value else None

    def delete_hash(self, key: str, field: str) -> None:
        self.redis_conn.hdel(key, field)

    def key_exists(self, key: str) -> bool:
        return self.redis_conn.exists(key)

    def insert_ex(self, key: str,value:any, time: int) -> None:
        self.redis_conn.set(key, value ,time)

    def insert_hash_ex(self, key: str, field: str, value: any, time: int) -> None:
        self.redis_conn.hset(key, field, value)
        self.redis_conn.expire(key, time)
