from os import path

from homework2.task1 import (count_non_ascii_chars, count_punctuation_chars,
                             get_longest_diverse_words,
                             get_most_common_non_ascii_char, get_rarest_char)

current_dir = path.dirname(__file__)
filename = path.join(current_dir, "test_data.txt")


def test_get_longest_diverse_words():
    """Checking that the data is a Fibonacci sequence"""
    assert get_longest_diverse_words(filename) == [
        "requestsgethttpsjsonplaceholdertypicodecomposts",
        "jsonplaceholder",
        "formatselfname",
        "следующим",
        "инициировать",
        "equivalent",
        "equivalent",
        "определяет",
        "выглядит",
        "Запустив",
    ]


def test_get_rarest_char():
    """Checking that the data is a Fibonacci sequence"""
    assert get_rarest_char(filename) == "шгющ<{}>ЭЗСъभारत网络NEקוםOMHஇந்தியா‘’k"


def test_count_punctuation_chars():
    """Checking that the data is a Fibonacci sequence"""
    assert count_punctuation_chars(filename) == 69


def test_count_non_ascii_chars():
    """Checking that the data is a Fibonacci sequence"""
    assert count_non_ascii_chars(filename) == 151


def test_get_most_common_non_ascii_char():
    """Checking that the data is a Fibonacci sequence"""
    assert get_most_common_non_ascii_char(filename) == "о"
