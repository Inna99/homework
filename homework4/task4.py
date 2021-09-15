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
    def gen_fizzbuzz(n):
        while n > 0:
            if n % 5 == 0:
                yield "buzz"
            elif n % 3 == 0:
                yield "fizz"
            else:
                yield n
            n -= 1
    return list(gen_fizzbuzz(n))[::-1]


print(fizzbuzz("5"))
