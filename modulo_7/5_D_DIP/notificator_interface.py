from abc import ABC, abstractmethod

class NotificatorInterface(ABC):
    
    @abstractmethod
    def send_notitication(self):
        pass