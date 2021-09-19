from homework3.task1 import cache


def test_cache_func(capsys):
    """Check that parameter is work"""

    @cache(times=2)
    def func(a, b):
        return (a ** b) ** 2

    for i in [1, 3, 1, 3, 1, 3]:
        print(func(i, i)[0])
    captured = capsys.readouterr()
    assert captured.out == "?\n1\n?\n729\n1\n729\n1\n729\n"
