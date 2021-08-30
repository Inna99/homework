from homework1.task5 import find_maximal_subarray_sum


def test_positive_case():
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3], 3) == 5
