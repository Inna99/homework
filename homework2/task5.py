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
import string
from typing import List


def custom_range(collection, *args) -> List:
    if len(args) == 3:
        start, stop, step = args
    elif len(args) == 2:
        start, stop = args
        step = 1
    else:
        start = collection[0]
        stop = args[0]
        step = 1
    print(start, stop, step)
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


print(custom_range(string.ascii_lowercase, "g"))
