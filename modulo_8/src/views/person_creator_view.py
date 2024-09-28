from src.controller.person_creator_controller import PersonCreatorController
from .interfaces.view_interface import ViewInterface
from .http_types.http_response import HttpResponse
from .http_types.http_request import HttpRequest


class PersonCreatorView(ViewInterface):
    def __init__(self, controller: PersonCreatorController) -> None:
        self.__controller = controller

    def handle(self, request: HttpRequest) -> HttpResponse:
        person_info = request.body
        body_response = self.__controller.create_person(person_info)

        return HttpResponse(status=201, body=body_response)
