# Разделение ответственности

class Report:
    def get_data(self):
        pass

class ReportPrinter:
    def print_report(self, report: Report):
        pass


# •S - Single Responsibility Principle (Принцип единственной ответственности)
# •Класс должен решать лишь одну конкретную задачу. Он должен быть
# ответственен только за одну часть функциональности, и эта ответственность
# должна быть полностью инкапсулирована в класс.