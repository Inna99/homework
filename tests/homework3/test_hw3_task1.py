from homework3.task1 import cache


def test_cache_func():
    """checks that the 'times' times function is cached"""

    @cache(times=1)
    def test():
        return list()

    reference_1 = test()
    reference_2 = test()
    reference_3 = test()
    assert reference_1 is reference_2
    assert reference_2 is not reference_3


def test_result():
    """checks that the return values of the function and the function under the decorator are equal"""

    def test():
        return list()

    decorated = cache(1)(test)
    assert decorated() == test()
