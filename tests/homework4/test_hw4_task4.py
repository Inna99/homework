import pytest

from homework4.task4 import fizzbuzz


def test_fizzbuzz():
    assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]


def test_fizzbuzz_string():
    with pytest.raises(TypeError):
        fizzbuzz("5")
