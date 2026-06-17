class Target:
    def request(self):
        raise NotImplementedError
class Adaptee:
    def specific_request(self):
        pass
class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee
    def request(self):
        self.adaptee.specific_request()



# Adapter (Адаптер) – паттерн преобразует интерфейс класса к другому интерфейсу, на который рассчитан
# клиент. Адаптер обеспечивает совместную работу классов, невозможную в обычных условиях из-за
# несовместимости интерфейсов.
# Adapter позволяет классам с несовместимыми интерфейсами работать вместе. Выступает в роли
# переводчика, преобразуя интерфейс одного класса в интерфейс, который ожидает другой класс.