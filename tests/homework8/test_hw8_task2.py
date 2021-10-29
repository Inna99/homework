from os import path

import pytest

from homework8.task2 import TableData

filename = path.join(path.dirname(__file__), "example.sqlite")
presidents = TableData(database_name=filename, table_name="presidents")


def test_table_data_like_dict():
    """checking that we can refer to the class as a dictionary"""
    assert presidents["Yeltsin"] == [("Yeltsin", 999, "Russia")]


def test_table_data_len():
    """checking that we can find the number of rows"""
    assert len(presidents) == 3


def test_table_data_is_collections():
    """checking that the object implements the iteration protocol"""
    assert [president for president in presidents] == [
            ("Yeltsin", 999, "Russia"),
            ("Trump", 1337, "US"),
            ("Big Man Tyrone", 101, "Kekistan"),
        ]


def test_table_data_is_operator():
    """checking "is" operator support"""
    assert "Yeltsin" in presidents


def test_table_data_key_error():
    """checking the KeyError exception call if there is no corresponding value for the key"""
    with pytest.raises(KeyError):
        presidents["Popov"]


def test_table_data_type_error():
    """checking for calling a TypeError exception if the key type is incorrect"""
    with pytest.raises(TypeError):
        presidents[5]
