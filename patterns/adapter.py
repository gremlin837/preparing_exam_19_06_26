# Интерфейс который ожидает клиент
class NotificationService:
    def send_notification(self, message, recipient):
        raise NotImplementedError("Subclasses must implement this method")

# Класс, который нужно адаптировать (старая система)
class LegacyNotificationSystem:
    def send_legacy_notification(self, user_id, text):
        print(f"Старая система: Отправка уведомления '{text}' пользователю {user_id}")

# Адаптер
class NotificationAdapter(NotificationService):
    def __init__(self, legacy_system):
        self.legacy_system = legacy_system

    def send_notification(self, message, recipient):
        # Адаптируем интерфейс: преобразуем современный формат в старый
        self.legacy_system.send_legacy_notification(recipient, message)

# Клиентский код
class Client:
    def __init__(self, notification_service):
        self.notification_service = notification_service

    def send_message(self, message, recipient):
        self.notification_service.send_notification(message, recipient)

if __name__ == "__main__":
    # Создаем старую систему
    legacy_system = LegacyNotificationSystem()

    # Оборачиваем её в адаптер
    adapter = NotificationAdapter(legacy_system)

    # Клиент работает с современным интерфейсом
    client = Client(adapter)
    client.send_message("Добро пожаловать в наше приложение!", "user123")





# Adapter (Адаптер) – паттерн преобразует интерфейс класса к другому интерфейсу, на который рассчитан
# клиент. Адаптер обеспечивает совместную работу классов, невозможную в обычных условиях из-за
# несовместимости интерфейсов.
# Adapter позволяет классам с несовместимыми интерфейсами работать вместе. Выступает в роли
# переводчика, преобразуя интерфейс одного класса в интерфейс, который ожидает другой класс.