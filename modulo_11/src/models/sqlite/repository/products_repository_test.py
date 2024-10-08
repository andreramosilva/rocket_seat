import pytest
from src.models.sqlite.settings.connection import SqliteConnectionHandler
from .products_repository import ProductsRepository

conn_handler = SqliteConnectionHandler()
conn = conn_handler.connect()

@pytest.mark.skip(reason="interacao com bd")
def test_insert_product():
    repo = ProductsRepository(conn)
    name = 'test_product'
    price = 10.0
    quantity = 10
    repo.insert_product(name, price, quantity)
    product = repo.find_product_by_name(name)
    print(product)
