"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from collections import Counter
from string import printable, punctuation
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    """Find 10 longest words consisting from largest amount of unique symbols"""
    with open(file_path) as fi:
        text = fi.read()
    punctuation_chars = dict.fromkeys(list(punctuation), "")
    my_table = " ".maketrans(punctuation_chars)  # type: ignore
    text = text.translate(my_table)
    list_x = text.split()
    word_count = list()
    for word in list_x:
        word_count.append((len(set(word)), word))
    word_count.sort(reverse=True)
    answer = [i[1] for i in word_count[:10]]
    return answer


def get_rarest_char(file_path: str) -> str:
    """Find rarest symbol for document"""
    with open(file_path) as f:
        text = f.read()
    counter = Counter(text)
    result = []
    frequency_occurrence = counter.most_common()
    amount_rarest_symbol = counter.most_common()[-1][1]
    for elem, number in frequency_occurrence:
        if number == amount_rarest_symbol:
            result.append(elem)
    return "".join(result)


def count_punctuation_chars(file_path: str) -> int:
    """Count every punctuation char"""
    punctuation_chars = Counter(dict.fromkeys(list(punctuation), 1000000))  # type: ignore
    with open(file_path) as fi:
        text = fi.read()
    counter = Counter(text)
    return sum((punctuation_chars & counter).values())


def count_non_ascii_chars(file_path: str) -> int:
    """Count every non ascii char"""
    with open(file_path) as fi:
        text = fi.read()
    counter = Counter(text)
    max_common = counter.most_common()[0][1]
    ascii_chars = Counter(dict.fromkeys(list(printable), max_common))  # переделать
    return sum((counter - ascii_chars).values())


def get_most_common_non_ascii_char(file_path: str) -> str:
    """Find most common non ascii char for document"""
    with open(file_path) as fi:
        text = fi.read()
    counter = Counter(text)
    max_common = counter.most_common()[0][1]
    ascii_chars = Counter(dict.fromkeys(list(printable), max_common))  # переделать
    return (counter - ascii_chars).most_common()[0][0]
