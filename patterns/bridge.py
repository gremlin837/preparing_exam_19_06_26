from abc import ABC, abstractmethod


# Реализации (цвета)
class Color(ABC):
    @abstractmethod
    def fill(self):
        pass


class Red(Color):
    def fill(self):
        return "красным"


class Blue(Color):
    def fill(self):
        return "синим"


class Green(Color):
    def fill(self):
        return "зелёным"


# Абстракции (фигуры)
class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        return f"Рисуем круг {self.color.fill()} цветом"


class Square(Shape):
    def draw(self):
        return f"Рисуем квадрат {self.color.fill()} цветом"


class Triangle(Shape):
    def draw(self):
        return f"Рисуем треугольник {self.color.fill()} цветом"


# Использование
if __name__ == "__main__":
    # Создаём разные комбинации фигур и цветов
    shapes = [
        Circle(Red()),
        Square(Blue()),
        Triangle(Green()),
        Circle(Blue()),
        Square(Red())
    ]

    for shape in shapes:
        print(shape.draw())






# bridge (Мост)
# Что делает: разделяет абстракцию и реализацию, чтобы они могли изменяться независимо.
# Когда применять: когда нужно менять реализацию без изменения интерфейса (например, разные способы отрисовки).
# Особенности применения в Python : разделение через интерфейсы/абстрактные базовые классы (abc) и композицию