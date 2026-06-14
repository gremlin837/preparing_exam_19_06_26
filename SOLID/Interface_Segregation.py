class Shape:
    def draw(self):
        raise NotImplementedError

class Circle(Shape):
    def draw(self):
        pass

class Square(Shape):
    def draw(self):
        pass


# лучше много специализированных интерфейсов, чем один общего назначения
# клиент не должен реализовывать интерфейс который он не собирается использовать
