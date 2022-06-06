"""
Customers can buy and sell BTC on our platform. We want to help them know what taxable gains and/or losses they have to
help them file taxes. When BTC is purchased, we note the time and value in dollars known as the cost basis.
When BTC is sold, at least one of these earlier purchases are fully or partially consumed.
The resulting difference in the dollar value when sold (the proceeds) and the cost basis is the gain (or a loss if negative).

We'd like to get an output of the gain/loss data that includes
the date of sale, date of acquisition, cost basis, proceeds, gains, and amount of BTC.
We'd also like to be able to see the current positions (date, amount and cost basis) left at any time
"""

from collections import deque
from enum import Enum


class Direction(Enum):
    BUY = 0
    SELL = 1


class Order:
    def __init__(self, time, direction, price, amount):
        self.time = time
        self.direction = direction
        self.price = price
        self.amount = amount


class Transaction:
    def __init__(self):
        self.btc_amount = 0
        self.cost_basis = 0
        self.avg_cost = -1
        self.positions = deque([])

    def buy_order(self, order: Order):
        if order.direction == Direction.BUY:
            self.btc_amount += order.amount
            self.cost_basis += order.amount * order.price
            self.avg_cost = self.cost_basis / self.btc_amount
            self.positions.append(order)
            return
        raise ValueError("Not a buy order")

    def sell_order(self, order: Order):
        """
        return date of sale, date of acquisition, cost basis, proceeds, gains, and amount of BTC.
        :param order:
        :return:
        """
        if order.direction == Direction.SELL:
            sell_amount = order.amount
            sell_price = order.price
            sell_date = order.time
            gain, cost = 0, 0
            acq_dates = '|'
            origin_amount = sell_amount
            while sell_amount > 0 and len(self.positions):
                buy_order: Order = self.positions.popleft()
                if buy_order.amount >= sell_amount:
                    gain += sell_amount * sell_price
                    cost += buy_order.amount * buy_order.price
                    acq_dates += str(buy_order.time) + '|'
                    if buy_order.amount - sell_amount > 0:
                        buy_order.amount -= sell_amount
                        self.positions.appendleft(buy_order)
                    sell_amount = 0
                else:
                    gain += buy_order.amount * sell_price
                    cost += buy_order.amount * buy_order.price
                    acq_dates += str(buy_order.time) + '|'
                    sell_amount -= buy_order.amount
            sold_amount = origin_amount - sell_amount
            self.btc_amount -= sold_amount
            self.cost_basis = self.btc_amount * self.avg_cost
            print('sell date', sell_date, 'acquisition date', acq_dates, 'cost', cost, 'total gain', gain, 'sold', sold_amount)
            return
        raise ValueError("Not a sell transaction")

    def display_positions(self):
        print("BTC amount", self.btc_amount)
        print("cost basis", self.cost_basis)
        print("avg cost", self.avg_cost)


if __name__ == '__main__':
    t = Transaction()
    order = Order(1, Direction.BUY, 12, 3)
    t.buy_order(order)
    order = Order(2, Direction.BUY, 11, 2)
    t.buy_order(order)
    order = Order(3, Direction.SELL, 20, 4)
    t.sell_order(order)
    t.display_positions()

    order = Order(4, Direction.SELL, 13, 2)
    t.sell_order(order)
    t.display_positions()

