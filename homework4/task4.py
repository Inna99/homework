"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command
You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]
* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    Given two integers, return the sum.

    :param n: int
    :return: list

    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']
    """
    answer = []
    for i in range(1, n + 1):
        if i % 5 == 0:
            answer.append("buzz")
        elif i % 3 == 0:
            answer.append("fizz")
        else:
            answer.append(str(i))
    return answer
