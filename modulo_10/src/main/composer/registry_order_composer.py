from src.use_cases.registry_order import RegistryOrder
from src.models.repository.orders_repository import OrdersRepository
from src.models.connections.mongodb_connection import db_connection

def registry_order_composer() -> RegistryOrder:
    conn = db_connection.get_client()
    model = OrdersRepository(conn)
    use_case = RegistryOrder(model)
    return use_case