from homework3.task1 import cache


def test_cache_func(capsys):
    """Check that parameter is work"""
    @cache(times=2)
    def func(a, b):
        return (a ** b) ** 2

    for i in [1, 3, 1, 3, 1, 3]:
        print(func(i, i))
    captured = capsys.readouterr()
    with capsys.disabled():
        print(captured)
    assert captured.out == r'?\n[1, 2]\n?\n[729, 2]\n[1, 1]\n[729, 1]\n[1, 0]\n[729, 0]\n?\n[1, 2]\n?\n[729, 2]\n'


    # captured = capsys.readouterr()
    # assert captured.out == "hello\n"