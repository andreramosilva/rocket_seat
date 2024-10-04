from datetime import datetime
from src.models.repository.interfaces.orders_repository import OrdersRepositoryInterface
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

class RegistryOrder:
    '''doc xpto '''
    def __init__(self, order_repository : OrdersRepositoryInterface) -> None:
        self.__order_repository = order_repository

    def registry(self,  http_request :HttpRequest) -> dict:
        try:
            body = http_request.body
            new_order = self.__format_new_order(body)
            self.__registry_order(new_order)
            return self.__format_response()
        except Exception as e:
            return HttpResponse(
                body = {
                    "error": str(e)
                },
                status_code=500)


    def __format_new_order(self, body: dict) -> dict:
        new_order = body["data"]
        new_order= { **new_order, "created_at": datetime.now()}
        return new_order

    def __registry_order(self, new_order: dict) -> dict:
        self.__order_repository.insert_one(new_order)

    def __format_response(self) -> HttpResponse:
        return HttpResponse(
            body = {
                "data":{
                    "type": "order",
                    "count": 1,
                    "registry" : True
                }
            },
            status_code=201)
