from abc import ABC, abstractmethod

class PersonCreatorController(ABC):
    @abstractmethod
    def create_person(self, person: dict):
        pass