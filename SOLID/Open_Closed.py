
class Discount:
    def apply(self, price):
        raise NotImplementedError

class PercentageDiscount(Discount):
    def apply(self, price):
        pass

class FixedDiscount(Discount):
    def apply(self, price):
        pass






# •O - Open/Closed Principle (Принцип
# открытости/закрытости)
# •Программные сущности (классы, модули,
# функции) должны быть открыты для
# расширения, но закрыты для модификации