"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


def find_occurrences(tree: dict, element: Any, count=0) -> int:
    """takes element and finds the number of occurrences of this element in the tree"""
    try:
        values = tree.values()
    except AttributeError:
        values = tree  # type: ignore
    for elem in values:
        if elem == element:
            count += 1
        elif isinstance(elem, dict):
            count = find_occurrences(elem, element, count=count)
        elif isinstance(elem, (list, tuple, set)):
            for el in elem:
                if isinstance(el, (list, tuple, set, dict)):
                    count = find_occurrences(el, element, count=count)  # type: ignore
            count += elem.count(element)  # type: ignore
    return count
