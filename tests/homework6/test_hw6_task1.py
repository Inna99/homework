from homework6.task1 import instances_counter


@instances_counter
class Employee:
    """Base class for all employees"""

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_employee(self):
        return f"Name: {self.name}. Salary: {self.salary}"


def test_instances_counter() -> None:
    """Check methods get_created_instances, reset_instances_counter"""
    emp1 = Employee("Tom", 9000)
    Employee("Bob", 12400)
    assert emp1.get_created_instances() == 2  # type: ignore

    Employee("Alice", 11500)
    assert emp1.reset_instances_counter() == 3  # type: ignore
    assert emp1.get_created_instances() == 0  # type: ignore


def test_save_methods() -> None:
    """checking for saving class methods"""
    emp1 = Employee("Tom", 9000)
    assert emp1.display_employee() == "Name: Tom. Salary: 9000"
