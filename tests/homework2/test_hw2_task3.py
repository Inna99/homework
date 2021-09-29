from homework2.task3 import combinations


def test_combinations_same_length():
    assert combinations([1, 2], [3, 4]) == [
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
    ]


def test_combinations_not_same_length():
    assert combinations([1, 2], [3, 4], [7]) == [
        [1, 3, 7],
        [1, 4, 7],
        [2, 3, 7],
        [2, 4, 7],
    ]
    assert combinations([1, 2, 5], [3, 4], [7]) == [
        [1, 3, 7],
        [1, 4, 7],
        [2, 3, 7],
        [2, 4, 7],
        [5, 3, 7],
        [5, 4, 7],
    ]


def test_combinations_one_list():
    assert combinations([1, 2]) == [[1], [2]]
