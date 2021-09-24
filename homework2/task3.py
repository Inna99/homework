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


def gen_comb(n):
    i = 0
    while i < 2 ** n:
        yield bin(i)[2:].zfill(n)
        i += 1


def combinations(*args: List[Any]) -> List[List]:
    list_lists = []
    for comb in gen_comb(len(args)):
        print(comb)
        x = []
        try:
            for index, elem in enumerate(comb):
                x.append(args[index][int(elem)])
        except IndexError:
            continue
        list_lists.append(x)
    return list_lists
