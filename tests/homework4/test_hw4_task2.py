from unittest import TestCase
from unittest.mock import patch

import pytest
import requests
from requests.exceptions import ConnectionError, ConnectTimeout, HTTPError

from homework4.task2 import count_dots_on_i

url = "https://example.com/"


class MockResponse(TestCase):
    def __init__(self, status_code):
        super().__init__()
        self.status_code = status_code
        self.content = ""
        if status_code in range(200, 300):
            self.text = "font-family: Arial, Helvetica, sans-serif;"
        else:
            self.text = 0

    def raise_for_status(self):
        if self.status_code not in range(200, 300):
            raise HTTPError


def test_count_dots_on_i_counted_correctly():
    """check that the number of letters was counted correctly"""
    with patch.object(requests, "get") as mock_method:
        mock_method.return_value = MockResponse(200)
        assert count_dots_on_i(url) == 4


def test_count_dots_on_i_bed_request():
    """check that return bad request 400"""
    with patch.object(requests, "get") as mock_method:
        mock_method.return_value = MockResponse(400)
        assert count_dots_on_i(url) == 0


def test_count_dots_on_i_connection_error():
    """we check that when the ConnectionError error is triggered, ValueError is triggered"""
    with patch.object(requests, "get") as mock_method:
        mock_method.side_effect = ConnectionError
        with pytest.raises(ValueError):
            count_dots_on_i(url)


def test_count_dots_on_i_connect_timeout():
    """we check that when the ConnectTimeout error is triggered, ValueError is triggered"""
    with patch.object(requests, "get") as mock_method:
        mock_method.side_effect = ConnectTimeout
        with pytest.raises(ValueError):
            count_dots_on_i(url)
