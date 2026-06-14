from abc import ABC, abstractmethod


# Элементы (фигуры)
class Shape(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor):
        return visitor.visit_circle(self)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def accept(self, visitor):
        return visitor.visit_rectangle(self)


# Посетители
class Visitor(ABC):
    @abstractmethod
    def visit_circle(self, circle):
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle):
        pass


class AreaCalculator(Visitor):
    def visit_circle(self, circle):
        return 3.14159 * circle.radius ** 2

    def visit_rectangle(self, rectangle):
        return rectangle.width * rectangle.height


class PerimeterCalculator(Visitor):
    def visit_circle(self, circle):
        return 2 * 3.14159 * circle.radius

    def visit_rectangle(self, rectangle):
        return 2 * (rectangle.width + rectangle.height)


# Использование
if __name__ == "__main__":
    shapes = [
        Circle(5),
        Rectangle(4, 6),
        Circle(3),
        Rectangle(2, 8)
    ]

    area_visitor = AreaCalculator()
    perimeter_visitor = PerimeterCalculator()

    print("Площади фигур:")
    for shape in shapes:
        area = shape.accept(area_visitor)
        print(f"{shape.__class__.__name__}: {area:.2f}")

    print("\nПериметры фигур:")
    for shape in shapes:
        perimeter = shape.accept(perimeter_visitor)
        print(f"{shape.__class__.__name__}: {perimeter:.2f}")



# Visitor (Посетитель)
# Суть: позволяет добавлять новые операции к объектам, не изменяя их классы. Операция выносится в отдельный класс-«посетитель».
# Когда использовать: обход дерева объектов, экспорт в разные форматы, подсчёт статистики по разнотипным объектам.

# Когда использовать Visitor:
# Нужно выполнить разные операции над объектами сложной структуры
#
# Классы объектов редко меняются, но операции над ними - часто
#
# Логика операций не должна засорять классы объектов
#
# Преимущества и недостатки:
# Плюсы:
#
# Упрощает добавление новых операций
#
# Объединяет родственные операции в одном классе
#
# Сохраняет принцип открытости/закрытости
#
# Минусы:
#
# Сложно добавлять новые типы элементов
#
# Нарушает инкапсуляцию (нужен доступ к внутренним данным)