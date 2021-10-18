import pytest

from homework9.task2 import Supressor, supressor


def test_supressor_suppressed():
    """checks that the intended error is suppressed"""
    lst = [1, 2]
    with supressor(IndexError):
        lst[5]


def test_supressor_raised():
    """checks that another error is being raised"""
    with pytest.raises(IndexError):
        with supressor(RuntimeError):
            [][2]


def test_Supressor_suppressed():
    """checks that the intended error is suppressed"""
    lst = [1, 2]
    with Supressor(IndexError):
        lst[5]


def test_Supressor_raised():
    """checks that another error is being raised"""
    with pytest.raises(IndexError):
        with Supressor(RuntimeError):
            [][2]
