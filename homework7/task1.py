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
    values = tree.values() if getattr(tree, "values", None) else tree
    for elem in values:
        if elem == element:
            count += 1
        elif isinstance(elem, (list, tuple, set, dict)):
            count = find_occurrences(elem, element, count=count)  # type: ignore
    return count
