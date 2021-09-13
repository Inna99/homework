"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from collections import Counter, defaultdict
from string import printable, punctuation
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    """Find 10 longest words consisting from largest amount of unique symbols"""
    with open(file_path, encoding="unicode_escape") as fi:
        text = fi.read()
    print(text)
    translate_table = text.maketrans("", "", punctuation)  # type: ignore
    text = text.translate(translate_table)
    list_words = text.split()
    sort_by_frequency = defaultdict(list)
    for word in list_words:
        amount = len(set(word))
        sort_by_frequency[amount].append(word)
    max_amount = max(sort_by_frequency.keys())
    answer = []
    count = 10
    while count > 0:
        len_ = len(sort_by_frequency[max_amount])
        if len_ <= count and len != 0:
            answer.extend(sort_by_frequency[max_amount])
            count -= len_
            max_amount -= 1
        else:
            sorted_on_len = sorted(
                sort_by_frequency[max_amount], reverse=True, key=lambda x: len(x)
            )
            answer.extend(sorted_on_len[:count])
            break
    return answer


def get_rarest_char(file_path: str) -> str:
    """Find rarest symbol for document"""
    with open(file_path, encoding="unicode_escape") as f:
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
    with open(file_path, encoding="unicode_escape") as fi:
        text = fi.read()
    counter = Counter(text)
    return sum((punctuation_chars & counter).values())


def count_non_ascii_chars(file_path: str) -> int:
    """Count every non ascii char"""
    with open(file_path, encoding="unicode_escape") as fi:
        text = fi.read()
    counter = Counter(text)
    max_common = counter.most_common()[0][1]
    ascii_chars = Counter(dict.fromkeys(list(printable), max_common))
    return sum((counter - ascii_chars).values())


def get_most_common_non_ascii_char(file_path: str) -> str:
    """Find most common non ascii char for document"""
    with open(file_path, encoding="unicode_escape") as fi:
        text = fi.read()
    counter = Counter(text)
    max_common = counter.most_common()[0][1]
    ascii_chars = Counter(dict.fromkeys(list(printable), max_common))
    return (counter - ascii_chars).most_common()[0][0]
