import pytest

from homework9.task2 import Suppressor, suppressor


def test_suppressor_func_suppressed():
    """checks that the intended error is suppressed"""
    lst = [1, 2]
    with suppressor(IndexError):
        lst[5]


def test_suppressor_func_raised():
    """checks that another error is being raised"""
    with pytest.raises(IndexError):
        with suppressor(RuntimeError):
            [][2]


def test_suppressor_func_not_error():
    """checks that it work without error"""
    lst = [1, 2]
    with Suppressor(IndexError):
        lst[1]


def test_suppressor_class_suppressed():
    """checks that the intended error is suppressed"""
    lst = [1, 2]
    with Suppressor(IndexError):
        lst[5]


def test_suppressor_class_raised():
    """checks that another error is being raised"""
    with pytest.raises(IndexError):
        with Suppressor(RuntimeError):
            [][2]


def test_suppressor_class_not_error():
    """checks that it work without error"""
    lst = [1, 2]
    with Suppressor(IndexError):
        lst[1]
