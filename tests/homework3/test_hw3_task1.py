from homework3.task1 import func


def test_cache_func():
    """Check that funcs are equal"""
    reference_1 = func(1, 1)
    reference_2 = func(1, 1)
    assert reference_1 is reference_2


def test_cache_func_negativ():
    """Check that funcs are not equal"""
    one, two, three, four = (  # noqa
        func(1, 1),
        func(1, 1),
        func(1, 1),
        func(1, 1)
    )
    assert id(one) == id(four)
