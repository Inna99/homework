from homework7.task2 import backspace_compare


def test_backspace_compare():
    """input test data with task"""
    assert not backspace_compare("a#c", "b")
    assert backspace_compare("ab#c", "ad#c")
    assert backspace_compare("a##c", "#a#c")
