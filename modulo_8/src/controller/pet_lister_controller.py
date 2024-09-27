from typing import Dict, List
from src.models.sqllite.interfaces.pets_repository import PetsRepositoryInterface
from src.models.sqllite.entities.pets import Pets


class PetListerController:
    def __init__(self, pet_repository: PetsRepositoryInterface) -> None:
        self.__pet_repository = pet_repository

    def list(self) -> List[Dict]:
        pets = self.__get_pets_from_db()
        response = self.__format_response(pets)
        return response

    def __get_pets_from_db(self) -> List[Pets]:
        pets = self.__pet_repository.list_pets()
        return pets

    def __format_response(self, pets: List[Pets]) -> Dict:
        return {
            "data": {
                "type": "pets",
                "count": len(pets),
                "attributes": [
                    {
                        "name": pet.name,
                        "type": pet.type
                    } for pet in pets
                ]
            }
        }
