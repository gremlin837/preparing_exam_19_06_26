# Не нужно создавать заивимости в классе.
# Зависеть от 'абстракций', а не от реализации.

from abc import ABC, abstractmethod


# Абстракция (зависят все)
class MessageSender(ABC):
    """Абстракция - интерфейс для всех отправителей"""

    @abstractmethod
    def send(self, message: str) -> None:
        pass


# Конкретные реализации (зависят от абстракции)
class EmailSender(MessageSender):
    def send(self, message: str) -> None:
        print(f" Отправка email: {message}")


class SMSSender(MessageSender):
    def send(self, message: str) -> None:
        print(f" Отправка SMS: {message}")


class TelegramSender(MessageSender):
    def send(self, message: str) -> None:
        print(f" Отправка Telegram: {message}")


class WhatsAppSender(MessageSender):
    def send(self, message: str) -> None:
        print(f" Отправка WhatsApp: {message}")


# Высокоуровневый модуль (зависит от абстракции)
class NotificationService:
    """Зависит от абстракции MessageSender, а не от конкретных классов"""

    def __init__(self, sender: MessageSender):  # Инъекция зависимости
        self.sender = sender

    def notify(self, message: str) -> None:
        self.sender.send(message)


# Использование
if __name__ == "__main__":
    # Можно легко подставить любой отправитель
    email_service = NotificationService(EmailSender())
    sms_service = NotificationService(SMSSender())
    telegram_service = NotificationService(TelegramSender())

    email_service.notify("Сообщение по email")
    sms_service.notify("Сообщение по SMS")
    telegram_service.notify("Сообщение по Telegram")

    # Легко добавить новый тип без изменения NotificationService
    whatsapp_service = NotificationService(WhatsAppSender())
    whatsapp_service.notify("Сообщение по WhatsApp")