from homework1.task2 import check_fibonacci


def test_positive_case():
    """Checking that the data is a Fibonacci sequence"""
    assert check_fibonacci([])
    assert check_fibonacci([0, 1])
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8])


def test_negative_case():
    """Checking that the data is not a Fibonacci sequence"""
    assert not check_fibonacci([0, 2])
