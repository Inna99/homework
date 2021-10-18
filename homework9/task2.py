"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
>>> with supressor(IndexError):
...    [][2]
"""
import logging
from contextlib import contextmanager

logging.basicConfig(level=logging.DEBUG)


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
        if not exc_type:
            logging.info(f"The exception was not raised")
            return True
        elif exc_type is self.ex:
            logging.info(f"Exception {exc_type} has been handled")
            return True


if __name__ == "__main__":  # pragma: no cover
    pass
