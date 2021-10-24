import logging
from unittest import mock, TestCase
from unittest.mock import MagicMock, patch

import pytest
import requests
from requests.exceptions import ConnectionError, ConnectTimeout, HTTPError

from homework4.task2 import count_dots_on_i

url = "https://example.com/"
# нужно. мокаешь реквестс чтоб в интернетики не ходил. мало ли там чо изменится,
# сайт пропадет или наоборот появится а ты чисто случайно прям такое же прекрасное имя задала orihwivhwohr.com
#
# мокаешь requests.get чтоб возвращал объект с полем текст.
# язык не типизированный так что можно прям вот так вот сурово делать
# r = object() r.text = 'otklaadr' ну или замутить какойнить классик типо MockResponse, даже лучше будет.
# с полями status_code и text и методом raise_for_status который райзит httpError если статускод не какойто из 200
#
# вот собственно получается 3 теста
#
# мокаем requests.get на ретурн вэлью MockResponse 200 и какаято строчка и проверяем что правильно посчиталось
#
# мокаем requests.get на ретурн вэлью MockResponse 400 и bad request и проверяем что залогалось то что надо и вернулся нон
#
# мокаем requests.get на сайдэффект raise ConnectTimeout и проверяем что вылетел вэлью эррор и чето залогалось
#
# можно даже последний разделить что бы проверить точно ли ConnectTimeout ловит оба эксепшена и написать два теста один где сайдэффект райзит таймаут а другой где райзит коннекшн эррор


class MockResponse(TestCase):
    def __init__(self, status_code):
        super().__init__()
        self.status_code = status_code
        self.text = 'font-family: Arial, Helvetica, sans-serif;'

    def raise_for_status(self):
        if self.status_code not in range(200, 300):
            raise HTTPError


# мокаем requests.get на ретурн вэлью MockResponse 200 и какаято строчка и проверяем что правильно посчиталось
def test_count_dots_on_i():
    with patch.object(count_dots_on_i, 'requests.get') as mock_method:
        # mock_method.return_value = MockResponse(200)
        mock_method.return_value = 5
