import unittest.mock
from os import path
from unittest.mock import patch

from homework2.task1 import (count_non_ascii_chars, count_punctuation_chars,
                             get_longest_diverse_words,
                             get_most_common_non_ascii_char, get_rarest_char)

current_dir = path.dirname(__file__)
filename = path.join(current_dir, "test_data.txt")

data = "аабббббб аабббаабаа абвб вбвба бвавбв бвабваб аб аб аб аб аб аб аб аб"


def test_function_that_opens_file_mock():
    """Check longest diverse words"""
    mock_on = unittest.mock.mock_open(read_data=data)
    with patch("builtins.open", mock_on):
        result = get_longest_diverse_words(path.join(current_dir, "test_mock.txt"))
        assert result == [
            "абвб",
            "вбвба",
            "бвавбв",
            "бвабваб",
            "аабббаабаа",
            "аабббббб",
            "аб",
            "аб",
            "аб",
            "аб",
        ]


def test_get_rarest_char():
    """Checking find rarest symbol for document"""
    dat = (
        "Es handelt sich um eine Kernfrage unserer Zeit, das hei\u00dft, "
        "um eine Frage, die auf alle F\u00e4lle Gef\u00e4hrdung mit sich bringt."
    )
    mock_on = unittest.mock.mock_open(read_data=dat)
    with patch("builtins.open", mock_on):
        result = get_rarest_char(path.join(current_dir, "test_mock.txt"))
        assert result == "EKZßGb."


def test_count_punctuation_chars():
    """Checking count every punctuation char"""
    assert count_punctuation_chars(filename) == 19


def test_count_non_ascii_chars():
    """Checking count every non ascii char"""
    assert count_non_ascii_chars(filename) == 42


def test_get_most_common_non_ascii_char():
    """Checking find most common non ascii char for document"""
    assert get_most_common_non_ascii_char(filename) == "à"
