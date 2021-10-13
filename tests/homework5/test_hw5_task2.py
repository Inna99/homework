from functools import reduce
from typing import Any

import pytest

from homework5.task2 import print_result


def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return reduce(lambda x, y: x + y, args)


@pytest.mark.parametrize(
    "args, result",
    [
        ([[1, 2, 3], [4, 5]], [1, 2, 3, 4, 5]),
        ([1, 3, 5], 9),
        (["afdf", "3kmddwDEF", "fx33in"], "afdf3kmddwDEFfx33in"),
        pytest.param([1, -34], 949, marks=pytest.mark.xfail),
    ],
)
def test_result_custom_sum(args: Any, result: Any) -> None:
    """checking the correctness of the result"""
    assert custom_sum(*args) == print_result(custom_sum)(*args) == result


def test_attr_name_custom_sum() -> None:
    """checking the saving of name attributes"""
    assert custom_sum.__name__ == "custom_sum"


def test_attr_doc_custom_sum() -> None:
    """checking to save the function documentation"""
    assert custom_sum.__doc__ == "This function can sum any objects which have __add___"


def test_attr_original_func_custom_sum() -> None:
    """checks that the custom method __original_func is working"""
    assert print_result(custom_sum).__original_func is custom_sum


@pytest.mark.parametrize(
    "args, result",
    [
        ([[1, 2, 3], [4, 5]], [1, 2, 3, 4, 5]),
        ([1, 3, 5], 9),
        (["afdf", "3kmddwDEF", "fx33in"], "afdf3kmddwDEFfx33in"),
        pytest.param([1, -34], 949, marks=pytest.mark.xfail),
    ],
)
def test_stdout(args: Any, result: Any, capsys):
    """checking the output to the console"""
    print_result(custom_sum)(*args)
    captured = capsys.readouterr()
    assert captured.out.rstrip() == str(result)
