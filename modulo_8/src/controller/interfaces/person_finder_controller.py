from abc import ABC, abstractmethod

class PersonFinderController(ABC):
    @abstractmethod
    def find_person(self, person_id: int):
        pass
    