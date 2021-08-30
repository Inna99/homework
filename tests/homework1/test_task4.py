from homework1.task4 import check_sum_of_four


def test_positive_case():
    assert check_sum_of_four([0], [0], [0], [0]) == 1
    assert check_sum_of_four([0, 5, 0], [0, 2, 3], [0, 5, 6], [0, 5, 8]) == 2
