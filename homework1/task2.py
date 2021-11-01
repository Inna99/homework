from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    """
    Given a cell with "it's a fib sequence" from slideshow,
        please write function "check_fib", which accepts a Sequence of integers, and
        returns if the given sequence is a Fibonacci sequence
    We guarantee, that the given sequence contain >= 0 integers inside.
    """
    print(data)
    length = len(data)
    if length == 0:
        return data == []
    elif length == 1:
        return data == [0]
    elif length == 2:
        return data == [0, 1]
    elif data[0] == 0 and data[1] == 1:
        a = 0
        b = 1
        for i in range(2, length):
            a, b = b, a + b
            if data[i] != b:
                return False
        return True
    else:
        return False
