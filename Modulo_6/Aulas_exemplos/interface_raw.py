from abc import ABC, abstractmethod

class NotificationSender(ABC):

    @abstractmethod
    def send_notification(self, message : str) -> None:
        pass

class EmailNotificationSender(NotificationSender):
    def send_notification(self,message:str)->None:
        print(f"Sending email with message: {message}")

class Notificator:
    def __init__(self, notification_sender: NotificationSender)->None:
        self.__notification_sender = notification_sender

    def send(self, message:str)->None:
        #validacao
        self.__notification_sender.send_notification(message)

obj = Notificator()
obj.send_notification("Hello") # This will