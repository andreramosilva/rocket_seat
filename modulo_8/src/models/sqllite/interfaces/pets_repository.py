from abc import ABC, abstractmethod
from typing import List
from src.models.sqllite.entities.pets import Pets

class PetsRepositoryInterface(ABC):
    @abstractmethod
    def delete_pet(self, pet_name: str) -> None:
        pass

    @abstractmethod
    def list_pets(self) -> List[Pets]:
        pass
