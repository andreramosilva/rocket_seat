from src.models.sqlite.repository.interfaces.products_repository import ProductsRepositoryInterface
from src.models.redis.repository.interfaces.redis_repository import RedisRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import  HttpResponse

class ProductCreator:
    def __init__(self, redis_repository: RedisRepositoryInterface
                 , products_repository: ProductsRepositoryInterface) -> None:
        self.__redis_repo = redis_repository
        self.__products_repo = products_repository

    def create(self, http_request: HttpRequest) -> HttpResponse:
        product_name = http_request.body.get('name')
        product_price = http_request.body.get('price')
        product_quantity = http_request.body.get('quantity')
        self.__insert_in_db(product_name, product_price, product_quantity)
        self.__insert_in_cache(product_name, product_price, product_quantity)
        return self.__format_response(product_name, product_price, product_quantity)

    def __insert_in_db(self, product_name: str, product_price: float,
                       product_quantity: int) -> None:
        self.__products_repo.insert_product(product_name, product_price,
                                             product_quantity)

    def __insert_in_cache(self, product_name: str, product_price: float,
                        product_quantity: int) -> None:
        value = f"{product_price},{product_quantity}"
        self.__redis_repo.insert_ex(product_name, value, 60)

    def __format_response(self, product_name: str, product_price: float,
                        product_quantity: int) -> HttpResponse:
        return HttpResponse(201,
                            body =
                            { "type": "product",
                             "count": 1,
                             "attributes":
                                {'name': product_name,
                                 'price': product_price, 
                                 'quantity': product_quantity
                                 }
                                 }
                            )
