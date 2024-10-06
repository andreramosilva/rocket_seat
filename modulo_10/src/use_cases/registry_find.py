from src.models.interfaces.orders.repository.orders_repository_interface import OrdersRepositoryInterface
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.validators.registry_order_validator import registry_order_validator
from src.errors.error_handler import error_handler

class RegistryFinder:
    def __init__(self, orders_repository: OrdersRepositoryInterface):
        self.__orders_repository = orders_repository

    def find(self, http_request: HttpRequest) -> HttpResponse:
        try:
            body = http_request.body
            self.__validate_body(body)

            order = self.__find_order(body)
            return self.__format_response(order)
        except Exception as e:
            return error_handler(e)