from abc import ABC, abstractmethod

class ClienteInterface(ABC):

    @abstractmethod
    def create(self, **kwargs):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def extrato(self):
        pass