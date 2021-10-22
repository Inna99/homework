from tempfile import NamedTemporaryFile

import pytest

from homework8.task1 import KeyValueStorage

tmp = NamedTemporaryFile()
with open(tmp.name, "w") as f:
    f.write("name=kek\nlast_name=top\npower=9001\nsong=shadilay\n1=something")
storage = KeyValueStorage(tmp.name)


def test_key_value_storage_equal():
    """checks that the value of the argument and the value of the key match"""
    assert storage["name"] == storage.name


def test_key_value_storage_isdigit():
    """checks that numeric values are stored as numbers"""
    assert storage["power"] + 1 == 9002


def test_key_value_storage_raises():
    """checks that an exception is being raised"""
    with open(tmp.name, "w") as f:
        f.write(
            "name=kek\nlast_name=top\npower=9001\nsong=shadilay\n1=something\nname=wrong"
        )
    with pytest.raises(ValueError):
        assert KeyValueStorage(tmp.name)
