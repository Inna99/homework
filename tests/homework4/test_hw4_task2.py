import homework4.task2
from homework4.task2 import count_dots_on_i
from unittest.mock import patch


def test_count_dots_on_i():
    @patch(homework4.task2.count_dots_on_i)
    def data_html():
        return
    assert count_dots_on_i("https://example.com/") == 59


