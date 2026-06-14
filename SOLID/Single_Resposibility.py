# Разделение ответственности

class HeatExchangerData:
    """Только хранит данные теплообменника"""

    def __init__(self, Q, delta_t, k):
        self.Q = Q  # Тепловая нагрузка, Вт
        self.delta_t = delta_t  # Температурный напор, К
        self.k = k  # Коэффициент теплопередачи


class HeatExchangerCalculator:
    """Отвечает только за расчеты"""

    @staticmethod
    def calculate_area(heat_exchanger):
        """Рассчитать площадь теплообмена"""
        return heat_exchanger.Q / (heat_exchanger.k * heat_exchanger.delta_t)


class DataValidator:
    """Отвечает только за проверку данных"""

    @staticmethod
    def validate_positive_numbers(Q, delta_t, k):
        if Q <= 0 or delta_t <= 0 or k <= 0:
            raise ValueError("Все параметры должны быть положительными")
        return True


class DatabaseSaver:
    """Отвечает только за сохранение в БД"""

    @staticmethod
    def save_result(area, params):
        print(f"Сохранение в БД: площадь = {area:.2f} м²")
        print(f"Параметры: Q={params.Q} Вт, Δt={params.delta_t} К, k={params.k}")
        # Логика работы с БД


# Использование
if __name__ == "__main__":
    # Данные
    exchanger = HeatExchangerData(Q=50000, delta_t=25, k=250)

    # Валидация
    DataValidator.validate_positive_numbers(
        exchanger.Q, exchanger.delta_t, exchanger.k
    )

    # Расчет
    area = HeatExchangerCalculator.calculate_area(exchanger)
    print(f"Рассчитанная площадь: {area:.2f} м²")

    # Сохранение
    DatabaseSaver.save_result(area, exchanger)


# •S - Single Responsibility Principle (Принцип единственной ответственности)
# •Класс должен решать лишь одну конкретную задачу. Он должен быть
# ответственен только за одну часть функциональности, и эта ответственность
# должна быть полностью инкапсулирована в класс.