from src.models.sqllite.interfaces.pets_repository import PetsRepositoryInterface
from .interfaces.pet_deleter_controller import PetDeleterControllerInterface

class PetDeleterController(PetDeleterControllerInterface):
    def __init__(self, pet_repository : PetsRepositoryInterface) -> None:
        self.pet_repository = pet_repository

    def delete_pet(self, name) -> None:
        return  self.pet_repository.delete_pet(name)
