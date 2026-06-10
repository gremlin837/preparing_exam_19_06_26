from abc import ABC, abstractmethod

# Абстрактная фабрика
class EnergyFactory(ABC):
    @abstractmethod
    def create_generator(self):
        pass

    @abstractmethod
    def create_battery(self):
        pass

# Конкретные фабрики
class HomeEnergyFactory(EnergyFactory):
    def create_generator(self):
        return "Домашний генератор 5 кВт"

    def create_battery(self):
        return "Домашний аккумулятор 500 кВт * ч"

class IndustrialEnergyFactory(EnergyFactory):
    def create_generator(self):
        return "Промышленный генератор 5 кВт"
    def create_battery(self):
        return "Промышленный аккумулятор 500 кВт * ч"

def create_energy_system(factory):
    generator = factory.create_generator()
    battery = factory.create_battery()
    print(f"Генератор: {generator}")
    print(f"Аккумулятор: {battery}")
    print()

# Создаем домашнюю энергосистему
home_factory = HomeEnergyFactory()
print("Домашняя энергосистема:")
create_energy_system(home_factory)

# Создаем промышленную энергосистему
industrial_factory = IndustrialEnergyFactory()
print("Промышленная энергосистема:")
create_energy_system(industrial_factory)
