from abc import ABC, abstractmethod

class Elevator:
    def __init__(self, state):
        self._state = None
        self.set_elevator_state(state)

    def set_elevator_state(self, state):
        self._state = state
        self._state.elevator = self

    def present_state(self):
        print(f"Лифт находится в состоянии: {type(self._state).__name__}")

    def push_down_btn(self):
        self._state.push_down_btn()

    def push_up_btn(self):
        self._state.push_up_btn()

class State(ABC):
    @property
    def elevator(self):
        return self._elevator

    @elevator.setter
    def elevator(self, elevator):
        self._elevator = elevator

    @abstractmethod
    def push_up_btn(self):
        pass

class FirstFloor(State):
    def push_down_btn(self):
        print("Уже на первом этаже")

    def push_up_btn(self):
        print("Лифт поднимается на второй этаж")
        self.elevator.set_elevator_state(SecondFloor())

class SecondFloor(State):
    def push_down_btn(self):
        print("Лифт опускается на первый этаж")
        self.elevator.set_elevator_state(FirstFloor())

    def push_up_btn(self):
        print("Уже на втором этаже")

if __name__ == "__main__":
    my_elevator = Elevator(FirstFloor())
    my_elevator.present_state()

    my_elevator.push_up_btn()
    my_elevator.present_state()

    my_elevator.push_down_btn()
    my_elevator.present_state()




# State (Состояние) – управляет изменением поведения объекта при изменении его внутреннего состояния. При
# реализации это выглядит так, словно объект меняет свой класс.
# State (Состояние) реализует структуру, в которой при изменении какого-то параметра объекта меняется то, как
# он будет обрабатывать поступающие в него запросы.