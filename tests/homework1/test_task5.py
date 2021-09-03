from homework1.task5 import find_maximal_subarray_sum


def test_example_case():
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16


def test_shorter_than_k_case():
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3], 3) == 8


def test_other_k_case():
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 4) == 21
