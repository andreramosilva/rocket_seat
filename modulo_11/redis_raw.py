import redis

redis_con = redis.Redis(host='localhost', port=6379, db=0)

redis_con.set('name', 'Alice')
print(redis_con.get('name'))  # b'Alice'
redis_con.set('name', 'Bob')
print(redis_con.get('name'))  # b'Bob'





redis_con.hset("meu_hash", "nome" ,"Joao")
redis_con.hset("meu_hash", "idade", 30)
redis_con.hset("meu_hash", "cidade", "Rio de Janeiro")

val = redis_con.hget("meu_hash", "nome").decode("utf-8")  # b'Joao'

redis_con.hdel("meu_hash", "cidade")

## busca por existencia
existe= redis_con.exists("name")  # True
print(existe)

redis_con.set("chave_del", "idade", 30)
redis_con.expire("meu_hash",10)