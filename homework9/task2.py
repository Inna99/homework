"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
>>> with supressor(IndexError):
...    [][2]
"""
from contextlib import contextmanager


@contextmanager
def supressor(*args, **kwargs):
    """Custom generator context manager that suppresses passed exception"""
    ex = args[0]
    try:
        yield
    except ex:
        pass


class Supressor:
    """Custom class context manager that suppresses passed exception"""

    def __init__(self, exeption):
        self.ex = exeption

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return exc_type is self.ex
