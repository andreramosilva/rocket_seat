from src.models.sqllite.settings.connection import db_connection_handler
from src.models.sqllite.repositories.pets_repository import PetsRepository
from src.controller.pet_lister_controller import PetListerController
from src.views.pet_lister_view import PetListerView

def pet_lister_composer():
    model = PetsRepository(db_connection_handler)
    controller = PetListerController(model)
    view = PetListerView(controller)
    return view
