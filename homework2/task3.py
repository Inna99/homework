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
from functools import reduce
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    lens_lists = [len(args[i]) for i in range(len(args))]
    new_len = reduce(lambda x, y: x * y, lens_lists)
    list_lists: List[List] = [[]] * new_len
    print(list_lists)
    for i, lst in enumerate(args):
        for j, elem in enumerate(lst):
            list_lists[i].append(elem)
    return []
