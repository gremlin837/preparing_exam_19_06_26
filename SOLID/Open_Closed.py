
class Discount:
    def apply(self, price):
        raise NotImplementedError
class PercentageDiscount(Discount):
    def apply(self, price):
        pass
class FixedDiscount(Discount):
    def apply(self, price):
        pass



# Базовый класс Discount объявляет метод apply(),
# а конкретные скидки (PercentageDiscount, FixedDiscount) реализуют его по-своему.
# Соответствие: Для добавления новой скидки достаточно создать новый подкласс,
# не трогая уже существующие классы — расширение без модификации.


# •O - Open/Closed Principle (Принцип
# открытости/закрытости)
# •Программные сущности (классы, модули,
# функции) должны быть открыты для
# расширения, но закрыты для модификации