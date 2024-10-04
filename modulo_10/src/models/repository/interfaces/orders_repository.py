from abc import ABC, abstractmethod

class OrdersRepositoryInterface(ABC):
    @abstractmethod
    def get_all(self) -> list:
        pass
    @abstractmethod
    def get_by_id(self, order_id) -> dict:
        pass
    @abstractmethod
    def insert_one(self, order) -> dict:
        pass
    @abstractmethod
    def insert_list_of_documents(self, orders_list: list) -> dict:
        pass
    @abstractmethod
    def update(self, order_id, order) -> dict:
        pass
    @abstractmethod
    def delete(self, order_id) -> dict:
        pass