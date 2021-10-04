from homework6.task1 import instances_counter


# тесты для проверки декоратора instances_counter для классов

# класс для проверки тестамм
@instances_counter
class Employee:
    """Базовый класс для всех сотрудников"""

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_employee(self):
        return f'Имя: {self.name}. Зарплата: {self.salary}'


# проверка методов get_created_instances, reset_instances_counter
def test_instances_counter() -> None:
    emp1 = Employee("Tom", 9000)
    emp2 = Employee("Bob", 12400)
    assert emp1.get_created_instances() == 2            # правильный подсчет

    emp3 = Employee("Alice", 11500)
    assert emp1.reset_instances_counter() == 3          # возвращение счетчика до сброса
    assert emp1.get_created_instances() == 0            # было ли обнуление?


# проверка на сохранение методов класса
def test_save_methods() -> None:
    emp1 = Employee("Tom", 9000)
    assert emp1.display_employee() == 'Имя: Tom. Зарплата: 9000'
