class Computer:
    def __init__(self):
        self.processor = None
        self.ram = None
        self.storage = None
        self.graphics_card = None

    def __str__(self):
        return (f"Компьютер: \n"
                f" Процессор: {self.processor}\n"
                f" Оперативная память: {self.ram}\n"
                f" Накопитель: {self.storage}\n"
                f" Видеокарта: {self.graphics_card}")

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_processor(self, processor):
        self.computer.processor = processor
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def set_graphics_card(self, graphics_card):
        self.computer.graphics_card = graphics_card
        return self

    def build(self):
        return self.computer

# Использование
builder = ComputerBuilder()

# Создаём игровой компьютер
gaming_pc = (builder
        .set_processor("Intel Core i9")
        .set_ram("32 GB DDR5")
        .set_storage("2 TB SSD")
        .set_graphics_card("NVIDIA RTX 4080")
        .build())

print("Игровой компьютер")
print(gaming_pc)








# Builder – позволяет создавать сложные объекты поэтапно через цепочку методов. Каждый метод устанавливает
# определённый параметр объекта и возвращает самого себя для последующих вызовов. Финальный метод build()
# возвращает полностью сконфигурированный готовый объект.

#Пример процесса:
# 1. Создаётся экземпляр строителя (ComputerBuilder);
# 2. Вызываются методы настройки (set_processor, set_ram и т.д.), каждый из которых
# возвращает this;
# 3. Цепочка завершается вызовом build(), который возвращает готовый объект
# (Computer).
# Преимущества:
# • Упрощает создание объектов со множеством параметров;
# • Позволяет создавать разные конфигурации объекта;
# • Улучшает читаемость кода за счёт fluent interface;
# • Соблюдает принцип единой ответственности (строитель отвечает только за конструирование)