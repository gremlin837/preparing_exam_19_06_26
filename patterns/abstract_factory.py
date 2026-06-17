# Factory (Фабричный метод)
# Делегирует создание объектов подклассам.
# Базовый Creator объявляет фабричный метод,
# а конкретные создатели возвращают нужные продукты.
# Это отделяет клиентский код от конкретных классов продуктов.

class Product:
    def operation(self):
        raise NotImplementedError
class ConcreteProduct(Product):
    def operation(self):
        pass
class Creator:
    def factory_method(self):
        raise NotImplementedError
class ConcreteCreator(Creator):
    def factory_method(self):
        return ConcreteProduct()



