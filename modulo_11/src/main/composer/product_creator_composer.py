from src.main.server.server_settings import redis_conn_handler, sqlite_conn_handler
from src.models.redis.repository.redis_repository import RedisRepository
from src.models.sqlite.repository.products_repository import ProductsRepository
from src.data.product_creator import ProductCreator



def product_creator_composer():
    redis_con = redis_conn_handler.get_connection()
    sqlite_con = sqlite_conn_handler.get_connection()

    redis_repo = RedisRepository(redis_con)
    products_repo = ProductsRepository(sqlite_con)

    return ProductCreator(redis_repo, products_repo)
