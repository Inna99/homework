from homework1.task3 import find_maximum_and_minimum


def test_positive_case():
    """Checking that the minimum and maximum are found"""
    assert find_maximum_and_minimum("tests/homework1/task3_cases/task3_test_case1.txt") == (6, 1)
    assert find_maximum_and_minimum("tests/homework1/task3_cases/task3_test_case2.txt") == (0, 0)
    assert find_maximum_and_minimum("tests/homework1/task3_cases/task3_test_case3.txt") == (45, 1)


def test_negative_case():
    """Checking that the minimum and maximum are not found"""
    assert not find_maximum_and_minimum("tests/homework1/task3_cases/task3_test_case3.txt") == (1, 45)


def test_is_tuple():
    """  Cheking that function return tuple"""
    assert isinstance(find_maximum_and_minimum("tests/homework1/task3_cases/task3_test_case3.txt"), tuple)
