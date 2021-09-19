from unittest import mock

import pytest

from homework4 import task2


def test_count_dots_on_i_return_value():
    """Checks that the number of letters i is correct"""
    with mock.patch("homework4.task2.count_dots_on_i") as mock_object:
        mock_object.return_value = 10
        assert task2.count_dots_on_i("https://example.com/") == 10


def test_count_dots_on_i_side_effect():
    """Checks when the url does not exist"""
    with mock.patch("homework4.task2.count_dots_on_i") as mock_object:
        mock_object.side_effect = Exception
        with pytest.raises(Exception):
            task2.count_dots_on_i("https://example.com/")
