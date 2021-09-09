"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
"""
from typing import List


def custom_range(collection, *args) -> List:
    defaults = [collection[0], collection[-1], 1]
    if len(args) == 3:
        defaults = list(args)
    elif len(args) == 2:
        defaults[0], defaults[1] = args[0], args[1]
    else:
        defaults[1] = args[0]
    start, stop, step = defaults
    answer = []
    if step < 1:
        collection = collection[::-1]
    step_start = collection.find(start)
    for i, elem in enumerate(collection):
        if i >= step_start:
            if elem != stop:
                if (i - step_start) % step == 0:
                    answer.append(elem)
            else:
                break
    return answer
