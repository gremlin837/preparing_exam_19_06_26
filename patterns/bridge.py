class Implementor:
    def operation_impl(self):
        raise NotImplementedError
class ConcreteImplementorA(Implementor):
    def operation_impl(self):
        pass
class Abstraction:
    def __init__(self, implementor):
        self.implementor = implementor
    def operation(self):
        self.implementor.operation_impl()

# Bridge (Мост)
# Разделяет абстракцию и реализацию, позволяя им меняться независимо.
# Абстракция содержит ссылку на объект-реализатор, который выполняет низкоуровневые операции.

# bridge (Мост)
# Что делает: разделяет абстракцию и реализацию, чтобы они могли изменяться независимо.
# Когда применять: когда нужно менять реализацию без изменения интерфейса (например, разные способы отрисовки).
# Особенности применения в Python : разделение через интерфейсы/абстрактные базовые классы (abc) и композицию