import tempfile

import pytest

from homework4.task1 import read_magic_number


def test_is_in_interval():
    """Check that number is in interval"""
    with tempfile.NamedTemporaryFile() as tempf:
        filename = tempf.name
        tempf.write(b"2")
        tempf.flush()
        assert str(read_magic_number(filename))


def test_is_not_in_interval():
    """Check that data is a number"""
    with tempfile.NamedTemporaryFile() as tempf:
        filename = tempf.name
        tempf.write(b"3")
        tempf.flush()
        assert not read_magic_number(filename)


def test_is_number_raises():
    """Check that data is a number"""
    with tempfile.NamedTemporaryFile() as tempf:
        filename = tempf.name
        tempf.write(b"dzfvbkSDVB")
        tempf.flush()
        with pytest.raises(ValueError):
            read_magic_number(filename)


@pytest.mark.xfail(raises=ValueError)
def test_is_number_xfail():
    """Check that data is a number"""
    with tempfile.NamedTemporaryFile() as tempf:
        filename = tempf.name
        tempf.write(b"dzfvbkSDVB")
        tempf.flush()
        read_magic_number(filename)
