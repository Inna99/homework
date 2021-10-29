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

from homework11.strategy import BasicDiscount, DayDiscount, NoDiscount, Order

if __name__ == "__main__":  # pragma: no cover
    orders = [
        Order(100, NoDiscount()),
        Order(100, BasicDiscount(0.20)),
        Order(100, DayDiscount([i for i in range(0, 32)], 0.20)),
    ]
    for order in orders:
        print(order)
