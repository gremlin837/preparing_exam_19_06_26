from abc import ABC, abstractmethod
import random
import time
import logging

# Настраиваем логирование
logging.basicConfig(level=logging.INFO, format="%(message)s")

# Абстрактный наблюдаемый класс
class Observable(ABC):
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, vitals):
        for observer in self._observers:
            observer.update(self, vitals)

class Observer(ABC):
    @abstractmethod
    def update(self, observable, vitals):
        pass

"""Реализация"""
# Конкретный пациент
class Patient(Observable):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def update_vitals(self):
        vitals = {
            'temperature': round(36.0 + random.uniform(0,3), 1),
            'heart_rate': random.randint(50, 130),
            'blood_pressure': (random.randint(100, 160), random.randint(60,100)),
            'oxygen_level': random.randint(85, 100)
        }

        # Уведомляем всех наблюадтелей об изменениях
        self.notify_observers(vitals)
        return vitals
# -----------------------------------
# Конкретные наблюдатели
class TemperatureMonitor(Observer):
    def update(self, patient, vitals):
        temp = vitals['temperature']
        if temp > 38.0:
            logging.warning(f" Высокая температура: {temp}С у пациента {patient.name}")
        elif temp < 35.0:
            logging.warning(f" Низкая температура: {temp}С у пациента {patient.name}")
        else:
            logging.info(f" Температура в норме: {temp}C")

class HeartRateMonitor(Observer):
    def update(self, patient, vitals):
        hr = vitals["heart_rate"]
        if hr > 120:
            logging.warning(f" Тахикардия! Пульс: {hr} уд/мин у пациента {patient.name}")
        elif hr < 50:
            logging.warning(f" Брадикардия! Пульс: {hr} уд/мин у пациента {patient.name}")
        else:
            logging.info(f" Пульс в норме: {hr} уд/мин")

class EmergencyDoctor(Observer):
    def __init__(self):
        self.critical_cases = 0

    def update(self, patient, vitals):
        if (vitals['temperature'] > 39.0 or
            vitals['heart_rate'] > 130 or
            vitals['heart_rate'] < 40 or
            vitals['oxygen_level'] < 90):

            self.critical_cases += 1
            logging.critical(f" ВРАЧ НУЖЕН! Пациент: {patient.name}")
            logging.critical(f" Показатели: {vitals}")
            logging.critical(f" Всего критических случаев: {self.critical_cases}")

# Главная программа
if __name__ == "__main__":
    patient = Patient("Иван Петров")

    # Подписываем наблюдателей
    patient.add_observer(TemperatureMonitor())
    patient.add_observer(HeartRateMonitor())
    patient.add_observer(EmergencyDoctor())

    logging.info("Система мониторинга пациента запущена")
    logging.info("========================================")

    for i in range (1,6):
        logging.info(f"\n Цикл мониторинга #{i}")
        logging.info("-" * 30)
        patient.update_vitals()
        time.sleep(1)

    logging.info("\n========================================")
    logging.info("Мониторинг завершен")




# Observer (Наблюдатель) – определяет отношение «один ко многим» между объектами таким образом, что при
# изменении состояния одного объекта происходит автоматическое оповещение и обновление всех зависимых
# объектов.
# Пример: рассмотрим ситуацию, когда у нас есть пациент у которого нужно отслеживать температуру и пульс и
# отправлять информацию на основе полученных данных. Пациент — наш класс, у которого со временем меняются
# параметры (температура и пульс). Наблюдатели — блоки кода, которые выводят информацию в те моменты, когда
# меняются параметры.