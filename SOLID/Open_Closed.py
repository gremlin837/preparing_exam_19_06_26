from abc import ABC, abstractmethod


# Абстрактный базовый класс
class Shape(ABC):
    """Открыт для расширения через наследование"""

    @abstractmethod
    def calculate_area(self):
        """Закрыт для модификации - интерфейс не меняется"""
        pass


# Конкретные фигуры
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return self.base * self.height / 2


# Легко добавить новую фигуру без изменения существующего кода
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2


class AreaCalculator:
    """Закрыт для модификации - не нужно менять при добавлении фигур"""

    def calculate_area(self, shape: Shape):
        """Принимает любой объект, наследующий Shape"""
        return shape.calculate_area()


# Использование
if __name__ == "__main__":
    calculator = AreaCalculator()

    shapes = [
        Circle(5),
        Rectangle(4, 6),
        Triangle(3, 4),
        Square(5)  # Новая фигура работает без изменения AreaCalculator
    ]

    for shape in shapes:
        area = calculator.calculate_area(shape)
        print(f"{shape.__class__.__name__}: {area:.2f}")







# •O - Open/Closed Principle (Принцип
# открытости/закрытости)
# •Программные сущности (классы, модули,
# функции) должны быть открыты для
# расширения, но закрыты для модификации