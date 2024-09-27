from abc import ABC, abstractmethod

class PetDeleterController(ABC):
    @abstractmethod
    def delete_pet(self, pet_id: int):
        pass
    