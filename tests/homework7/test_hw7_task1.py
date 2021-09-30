import pytest

from homework7.task1 import find_occurrences


def test_find_occurrences_with_list_in_list():
    """test data contains lists and dictionaries in lists"""
    example_tree = {
        "first": [["RED"], "BLUE"],
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
        "fifth": ("fourth", "RED"),
    }
    assert find_occurrences(example_tree, "RED") == 7


# def test_find_occurrences():
#     """test data provided"""
#     example_tree = {
#         "first": ["RED", "BLUE"],
#         "second": {
#             "simple_key": ["simple", "list", "of", "RED", "valued"],
#         },
#         "third": {
#             "abc": "BLUE",
#             "jhl": "RED",
#             "complex_key": {
#                 "key1": "value1",
#                 "key2": "RED",
#                 "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
#             }
#         },
#         "fourth": "RED",
#     }
#     assert find_occurrences(example_tree, "RED") == 6


def test_negativ():
    with pytest.raises(AttributeError):
        assert find_occurrences([], "")
