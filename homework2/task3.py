"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.
You may assume that that every list contain at least one element
Example:
assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import Any, List


def product(list_lists):
    if not list_lists:
        yield []
    else:
        for a in list_lists[0]:
            for prod in product(list_lists[1:]):
                yield [a] + prod


def combinations(*args: List[Any]) -> List[List]:
    list_lists = list(product(args))
    return list_lists


print(combinations([1, 2, 5], [3, 4], [7]))
