from homework3.task3 import Filter, make_filter, sample_data


def test_make_filter_list():
    """"""
    positive_even = Filter(
        (lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int))
    )
    assert positive_even.apply(range(10)) == [2, 4, 6, 8]


def test_make_filter_dict():
    """"""
    assert make_filter(name="polly", type="bird").apply(sample_data) == [
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"}
    ]


def test_filter():
    """do I need to test the class"""
