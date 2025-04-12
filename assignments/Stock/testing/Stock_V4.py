class stock_manager:

    # item definining stocks
    class _Stock:
        # limit attribute to only these two
        __slots__ = '_price', '_quantity'

        def __init__(self, price, quantity):    # defines
            self._price = price
            self._quantity = quantity

        def __lt__(self, other):   # less than operator for sorting (used when inserting into queue)
            return self._price < other._price

    def __init__(self):
        self.stock_register = {}       # [stock_id, recent trade price]
        self.sell_queue = {}           # [stock_id, _Stock(price, quantity)]    - ex: {1, [100, 10], [200, 5]}
        self.buy_queue = {}            # [stock_id, _Stock(price, quantity)]

    def register_stock(self, stock_id):
        if stock_id not in self.stock_register:
            self.stock_register[stock_id] = 0
            # prepare que for each stock_id instead of just stacking all orders in one queue
            self.sell_queue[stock_id] = []  # min-price: ascending
            self.buy_queue[stock_id] = []   # max-price: descending

    def place_buy_order(self, stock_id, quantity, max_price):
        # initialize / call sell queue for stock_id
        sell_q = self.sell_queue[stock_id]

        # while 
        #   1) sell_q is not empty (empty = no one selling stock),
        #   2) still need to buy stock, 
        #   3) current price of sell order < max_price
        while sell_q and quantity > 0 and sell_q[0]._price <= max_price:
            # extract sell order from queue
            best_sell = sell_q[0] # get first order in queue
            sell_price, sell_quantity = best_sell._price, best_sell._quantity # save price and quantity to local variables to avoid multiple lookups

            # if - can buy all stock from seller
            if sell_quantity > quantity:
                best_sell._quantity -= quantity # update quantity of seller
                self.stock_register[stock_id] = sell_price # update stock register with price
                return
            else:
                # if - only fullfill part of buy order
                sell_q.pop(0)   # remove order from queue
                quantity -= sell_quantity # update buy quantity
                self.stock_register[stock_id] = sell_price  # update stock register with price
            # update stock register with price is not here bcause of return if order is fullfilled

        # Not fulfilled: insert into buy queue (sorted by descending price)
        new_order = self._Stock(max_price, quantity)    # create new order object
        index = len(self.buy_queue[stock_id])   # get length of buy queue for stock_id

        # find right index to insert new order
        # while
        #   1) index is greater than 0 (goes from end to 0)
        #   2) the price of order at buy queue(with same stock_id) < price of new order
        # == start from most expensive order and go down until find cheaper order
        while index > 0 and self.buy_queue[stock_id][index - 1]._price < new_order._price:
            index -= 1
        # insert new order into buy queue at index
        self.buy_queue[stock_id].insert(index, new_order)



    # same as buy order but reversed
    def place_sell_order(self, stock_id, quantity, min_price):
        buy_q = self.buy_queue[stock_id]

        # Match with the highest available buy orders
        while buy_q and quantity > 0 and buy_q[0]._price >= min_price:
            best_buy = buy_q[0]
            buy_price, buy_quantity = best_buy._price, best_buy._quantity

            if buy_quantity > quantity:
                best_buy._quantity -= quantity
                self.stock_register[stock_id] = buy_price
                return
            else:
                buy_q.pop(0)
                quantity -= buy_quantity
                self.stock_register[stock_id] = buy_price

        new_order = self._Stock(min_price, quantity)
        index = len(self.sell_queue[stock_id])
        while index > 0 and new_order < self.sell_queue[stock_id][index - 1]:
            index -= 1
        self.sell_queue[stock_id].insert(index, new_order)



    def print_all_stocks(self):
        # sort stock register by price (descending)
        stock_list = sorted(self.stock_register.items(), key=lambda x: x[1], reverse=True)
        print(stock_list)




# Fast CLI interface
def main():
    sm = stock_manager()
    import sys
    for line in sys.stdin:
        args = line.strip().split()
        if not args:
            continue

        cmd = args[0]
        if cmd == "register_stock":
            sm.register_stock(int(args[1]))
        elif cmd == "place_buy_order":
            sm.place_buy_order(int(args[1]), int(args[2]), int(args[3]))
        elif cmd == "place_sell_order":
            sm.place_sell_order(int(args[1]), int(args[2]), int(args[3]))
        elif cmd == "print_all_stocks":
            sm.print_all_stocks()
            break

if __name__ == "__main__":
    main()