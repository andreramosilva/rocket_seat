from src.controller.pet_lister_controller import PetListerController
from .interfaces.view_interface import ViewInterface
from .http_types.http_response import HttpResponse
from .http_types.http_request import HttpRequest


class PetListerView(ViewInterface):
    def __init__(self, controller: PetListerController) -> None:
        self.__controller = controller

    def handle(self, request: HttpRequest) -> HttpResponse:
        body_response = self.__controller.list_pets()
        return HttpResponse(status=201, body=body_response)
