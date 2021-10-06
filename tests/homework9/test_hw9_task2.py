import pytest

from homework9.task2 import Supressor, supressor


def test_supressor():
    with pytest.raises(IndexError) as excinfo:
        raise IndexError
    assert "index out of range" in str(excinfo.value)

# def test_recursion_depth():
#     with pytest.raises(RuntimeError) as excinfo:
#         def f():
#             f()
#
#         f()
#     assert "maximum recursion" in str(excinfo.value)
#
# def test_Supressor():
#     assert