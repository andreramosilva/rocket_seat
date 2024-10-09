from abc import ABC, abstractmethod

class RedisRepositoryInterface(ABC):
    @abstractmethod
    def insert(self, key: str, value: any) -> None:
        pass
    @abstractmethod
    def get_key(self, key: str) -> str:
        pass
    @abstractmethod
    def delete_key(self, key: str) -> None:
        pass
    @abstractmethod
    def insert_hash(self, key: str, field: str, value: any) -> None:
        pass
    @abstractmethod
    def get_hash(self, key: str, field: str) -> str:
        pass
    @abstractmethod
    def delete_hash(self, key: str, field: str) -> None:
        pass
    @abstractmethod
    def key_exists(self, key: str) -> bool:
        pass
    @abstractmethod
    def insert_ex(self, key: str,value:any, time: int) -> None:
        pass
    @abstractmethod
    def insert_hash_ex(self, key: str, field: str, value: any, time: int) -> None:
        pass
