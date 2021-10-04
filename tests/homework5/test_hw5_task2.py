from homework5.task2 import custom_sum


def test_custom_sum__doc__():
    """checks that the method returns the data of the original function"""
    assert custom_sum.__doc__ == "This function can sum any objects which have __add___"


def test_custom_sum__name__():
    """checks that the method returns the data of the original function"""
    assert custom_sum.__name__ == "custom_sum"


def test_custom_sum__original_func():
    """checks that the custom method __original_func is working"""
    assert str(custom_sum.__original_func).startswith("<function custom_sum at")
