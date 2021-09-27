import logging
from unittest import mock

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

def test_count_dots_on_i():
    with mock.patch('homework4.task2.count_dots_on_i') as mock_object:
        mock_object.return_value = 10
        from homework4.task2 import count_dots_on_i
        print(count_dots_on_i("https://example.com/"))
        assert count_dots_on_i("https://example.com/") == 10


# def test_logging(caplog):
#     """Check that logging work when HTTPError error raise"""
#     response = requests.get(url)
#     response.raise_for_status()
#     logging.getLogger().info("boo %s", "arg")
#
#     assert caplog.record_tuples == [("root", logging.INFO, "boo arg")]
#     # assert captured.startswith("status_code")


# from homework4.task2 import count_dots_on_i
#
#
# def test_count_dots_on_i_return_value():
#     with mock.patch("homework4.task2.count_dots_on_i") as mock_object:
#         mock_object.return_value = 10
#         assert count_dots_on_i("https://example.com/") == 10


# def test_count_dots_on_i():
#     with mock.patch('homework4.task2.count_dots_on_i') as mock_object:
#         mock_object.return_value = 10
#         from homework4.task2 import count_dots_on_i
#         print(count_dots_on_i("https://example.com/"))
#         assert count_dots_on_i("https://example.com/") == 10


# def test_count_dots_on_i_side_effect():
#     """Checks when the url does not exist"""
#     with mock.patch("homework4.task2.count_dots_on_i") as mock_object:
#         mock_object.side_effect = Exception
#         with pytest.raises(Exception):
#             count_dots_on_i("https://example.com/")
