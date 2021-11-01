"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""
from itertools import zip_longest


def backspace_compare(first: str, second: str) -> bool:
    """Given two strings. Return if they are equal when both are typed into empty text editors."""
    first_, second_ = [], []
    for char_f, char_s in zip_longest(first, second):
        if char_f != "#":
            if char_f:
                first_.append(char_f)
        elif len(first_) > 0:
            first_.pop()
        if char_s != "#":
            if char_s:
                second_.append(char_s)
        elif len(second_) > 0:
            second_.pop()
    return first_ == second_
