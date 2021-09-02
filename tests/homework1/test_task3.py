from os import path

from homework1.task3 import find_maximum_and_minimum


def test_positive_case():
    current_dir = path.dirname(__file__)
    filename = path.join(current_dir, "task3_cases/task3_test_case1.txt")
    """Checking that the minimum and maximum are found"""
    assert find_maximum_and_minimum(filename) == (6, 1)
    filename = path.join(current_dir, "task3_cases/task3_test_case2.txt")
    assert find_maximum_and_minimum(filename) == (0, 0)
    current_dir = path.dirname(__file__)
    filename = path.join(current_dir, "task3_cases/task3_test_case3.txt")
    assert find_maximum_and_minimum(filename) == (45, 1)


def test_negative_case():
    """Checking that the minimum and maximum are not found"""
    current_dir = path.dirname(__file__)
    filename = path.join(current_dir, "task3_cases/task3_test_case3.txt")
    assert not find_maximum_and_minimum(filename) == (1, 45)


def test_is_tuple():
    """Cheking that function return tuple"""
    current_dir = path.dirname(__file__)
    filename = path.join(current_dir, "task3_cases/task3_test_case3.txt")
    assert isinstance(find_maximum_and_minimum(filename), tuple)
