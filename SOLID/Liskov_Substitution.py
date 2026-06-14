# Ф-ции которые 'используют базовый тип'
# должны иметь возможность 'использовать подтипы'
# базового типа, не зная об этом

class Vehicle:
    def __init__(self, name: str, speed: float):
        self.name = name
        self.speed = speed

    def get_name(self) -> str:
        return f"The vehicle name {self.name}"

    def get_speed(self) -> str:
        return f"The vehicle speed {self.speed}"

class VehicleWithoutEngine(Vehicle):
    def start_moving(self):
        raise NotImplementedError

class VehicleWithEngine(Vehicle):
    def engine(self):
        pass

    def start_engine(self):
        self.engine()

class Car(VehicleWithEngine):
    def start_engine(self):
        pass

class Bicycle(VehicleWithoutEngine):
    def start_moving(self):
        pass

# Принцип подстановки Лисков (Liskov Substitution Principle - LSP)
# Принцип: Объекты в программе должны быть заменяемы на экземпляры их
# подтипов без изменения правильности выполнения программы.
# если подставить наследника вместо родительского класса, ничего не сломается
# Дочерний класс должен дополнять, а не заменять поведение родительского.