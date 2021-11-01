import datetime
from abc import ABC, abstractmethod

"""
You are given the following code:
class Order:
    morning_discount = 0.25
    def init(self, price):
        self.price = price
    def final_price(self):
        return self.price - self.price * self.morning_discount
Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy
Example of the result call:
def morning_discount(order):
    ...
def elder_discount(order):
    ...
order_1 = Order(100, morning_discount)
assert order_1.final_price() == 75
order_2 = Order(100, elder_discount)
assert order_2.final_price() == 10
"""


class Order:
    def __init__(self, price, strategy=None) -> None:
        self.price = price
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy) -> None:
        self._strategy = strategy

    def final_price(self) -> None:  # ???
        result = self._strategy.calculate(self.price)
        return result

    def __repr__(self):
        return f"{self.price=}, {self.final_price()=}, strategy={self.strategy}"


class Strategy(ABC):
    @abstractmethod
    def calculate(self, price):
        pass


class NoDiscount(Strategy):
    def calculate(self, price):
        return price


class BasicDiscount(Strategy):
    def __init__(self, discount):
        self.discount = discount

    def calculate(self, price):
        return price - price * self.discount


class DayDiscount(Strategy):
    def __init__(self, days_with_discount, discount):
        self.discount = discount
        self.days_with_discount = days_with_discount

    def calculate(self, price):
        if datetime.datetime.now().day in self.days_with_discount:
            return price - price * self.discount
        else:
            return price
