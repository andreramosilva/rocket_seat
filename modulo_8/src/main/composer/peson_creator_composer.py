from src.models.sqllite.repositories.people_repository import PeopleRepository
from src.models.sqllite.settings.connection import db_connection_handler
from src.controller.person_creator_controller import PersonCreatorController
from src.views.person_creator_view import PersonCreatorView

def person_creator_composer():
    model = PeopleRepository(db_connection_handler)
    controller = PersonCreatorController(model)
    view = PersonCreatorView(controller)
    return view