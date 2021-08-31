"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    print("Hi")
    a = list()
    with open(file_path) as fi:
        for line in fi:
            a.append(line.rstrip())
    x = ' '.join(a)
    my_table = ' '.maketrans({'.': '', ',': '', '-': '', ';': '', ':': ''})
    x = x.translate(my_table)
    list_x = x.split()
    set_x = set(list_x)
    list_x = list(set_x)
    list_x.sort(reverse=True, key=lambda z: len(z))
    print(list_x)


def get_rarest_char(file_path: str) -> str:
    ...


def count_punctuation_chars(file_path: str) -> int:
    ...


def count_non_ascii_chars(file_path: str) -> int:
    ...


def get_most_common_non_ascii_char(file_path: str) -> str:
    ...


get_longest_diverse_words("data.txt")
