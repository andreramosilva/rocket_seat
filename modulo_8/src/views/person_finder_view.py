from src.controller.person_finder_controller import PersonFinderController
from .interfaces.view_interface import ViewInterface
from .http_types.http_response import HttpResponse
from .http_types.http_request import HttpRequest


class PersonFinderView(ViewInterface):
    def __init__(self, controller: PersonFinderController) -> None:
        self.__controller = controller

    def handle(self, request: HttpRequest) -> HttpResponse:
        person_id = request.param["person_id"]
        body_response = self.__controller.find(person_id)

        return HttpResponse(status=201, body=body_response)
