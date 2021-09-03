from homework1.calc import check_power_of_2


def test_positive_case():
    """Testing that actual powers of 2 give True"""
    assert check_power_of_2(65536)
    assert check_power_of_2(1)
    assert check_power_of_2(2)


def test_negative_case():
    """Testing that non-powers of 2 give False"""
    assert not check_power_of_2(12)
    assert not check_power_of_2(0)


def test_positive_negative():
    """Testing that non-powers of 2 give False"""
    assert check_power_of_2(-8)
