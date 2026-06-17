# Не нужно создавать заивимости в классе.
# Зависеть от 'абстракций', а не от реализации.

class MessageSender:
    def send(self, message):
        raise NotImplementedError
class EmailSender(MessageSender):
    def send(self, message):
        pass
class NotificationService:
    def __init__(self, sender: MessageSender):
        self.sender = sender
    def notify(self, message):
        self.sender.send(message)

# Пример: NotificationService зависит от абстракции MessageSender, а не от конкретного EmailSender.
# Конкретный отправитель внедряется извне.
# Соответствие: Модуль верхнего уровня не зависит от деталей нижнего уровня;
# оба зависят от абстракции, что позволяет легко заменять реализации (например, на SmsSender).

