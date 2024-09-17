from notificator_interface import NotificatorInterface


class NotificatorEmail(NotificatorInterface):
    def send_notification(self, mensagem):
        print(f'Enviando email para {self.email}: {mensagem}')