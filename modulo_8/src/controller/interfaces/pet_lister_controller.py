from abc import ABC, abstractmethod

class PetListerController(ABC):
    @abstractmethod
    def list(self):
        pass