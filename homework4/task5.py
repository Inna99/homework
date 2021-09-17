"""
doctest
This task is optional.
Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.
Definition of done:
 - function is created
 - function is properly formatted
 - function has tests
 list(fizzbuzz(5))
["1", "2", "fizz", "4", "buzz"]
* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
from typing import Generator


def fizzbuzz(n: int) -> Generator:
    """
    Return the generator object
    """
    tmp = 1
    while tmp <= n:
        if tmp % 5 == 0:
            yield "buzz"
        elif tmp % 3 == 0:
            yield "fizz"
        else:
            yield str(tmp)
        tmp += 1
