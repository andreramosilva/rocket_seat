from src.models.sqllite.repositories.people_repository import PeopleRepository
from src.models.sqllite.settings.connection import db_connection_handler
from src.controller.person_finder_controller import PersonFinderController
from src.views.person_finder_view import PersonFinderView

def person_finder_composer():
    model = PeopleRepository(db_connection_handler)
    controller = PersonFinderController(model)
    view = PersonFinderView(controller)
    return view
