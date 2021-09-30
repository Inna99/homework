"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}
count = 0


def find_occurrences_in_list(lst: list, element: Any) -> int:
    """takes element and finds the number of occurrences of this element in the дшые"""
    global count
    for elem in lst:
        if isinstance(elem, (list, tuple)):
            count += elem.count(element)
            for elem_list in elem:
                if isinstance(elem_list, dict):
                    find_occurrences(elem_list, element)
                elif isinstance(elem_list, (list, tuple)):
                    find_occurrences_in_list(elem_list, element)
        elif isinstance(elem, (int, str)):
            if elem == element:
                count += 1
        elif isinstance(elem, dict):
            find_occurrences(elem, element)
        elif isinstance(elem, bool) and elem == element:
            count += 1
    return count


def find_occurrences(tree: dict, element: Any) -> int:
    """takes element and finds the number of occurrences of this element in the tree"""
    return find_occurrences_in_list(list(tree.values()), element)


if __name__ == "__main__":
    print(find_occurrences(example_tree, "RED"))  # 6
