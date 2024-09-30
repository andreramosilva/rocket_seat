from src.controller.pet_deleter_controller import PetDeleterController
from .interfaces.view_interface import ViewInterface
from .http_types.http_response import HttpResponse
from .http_types.http_request import HttpRequest


class PetDeleterView(ViewInterface):
    def __init__(self, controller: PetDeleterController) -> None:
        self.__controller = controller

    def handle(self, request: HttpRequest) -> HttpResponse:
        name = request.param["name"]
        self.__controller.delete_pet(name)
        return HttpResponse(status=204, body=None)
