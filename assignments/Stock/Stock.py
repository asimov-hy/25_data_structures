# Design a real-time stock trading system that accommodates the buying and selling of stocks.
# The system should support high-volume transactions efficiently, ensuring that buy and sell orders are matched optimally.



# Implement the StockTradingSystem class with the following methods:
#   - register_stock(stock_id): 
#           Adds a stock with the specified stock_id to the system. 
#           This method is called once for each stock at the system's initiation.
#           The initial price of the stock is 0.

#   - place_buy_order(stock_id, quantity, max_price): 
#           Places a buy order, attempting to buy a specified quantity of a stock at a price not exceeding max_price. 
#           The system should match the order with the lowest available sell orders. 
#           Orders that cannot be matched immediately are placed in a queue until they can be matched with future orders.

#   - place_sell_order(stock_id, quantity, min_price): 
#           Places a sell order, attempting to sell a specified quantity of a stock at a price not below than min_price.
#           The system should match the order with the highest available buy orders.
#           Orders that cannot be matched immediately are placed in a queue until they can be matched with future orders.

#   - print_all_stocks(): 
#           Prints all the stocks in the system, along with their current transaction prices. 
#           The transaction price is the price at which the most recent buy and sell orders were matched. 
#           The stocks should be ordered from the highest to the lowest transaction price.

# Constraints:
#   - 1 <= number of stocks <= 10^2
#   - 1 <= stock_id, price, quantity, max_price, min_price <= 10^5
#   - price, quantity, maxPrice, and minPrice are integers.
#   - The total number of operations will not exceed 10^7.

class stock_manager:
    # Each stock in the system possesses the following properties:
    #   - stock_id: An integer representing the unique identifier for the stock.
    #   - price: An integer representing the current price of the stock.

    def __init__(self):
        self.stock_register = {}    # id, price(most recent transaction)
        self.buy_queue = []     # id, quantity, max_price
        self.sell_queue = []    # id, quantity, min_price
    
    #   - register_stock(stock_id): 
    #           Adds a stock with the specified stock_id to the system. 
    #           This method is called once for each stock at the system's initiation.
    #           The initial price of the stock is 0.
    def register_stock(self, stock_id):
        if stock_id not in self.stock_register:
            self.stock_register[stock_id] = 0
    
    def place_buy_order(self, stock_id, quantity, max_price):
        # Adds a stock with the specified stock_id to the system. 
        # This method is called once for each stock at the system's initiation.
        # The initial price of the stock is 0.

        #sort so that cheapest stock comes first in sell_queue
        self.sell_queue.sort(key=lambda x: x[2])

        for sell_order in self.sell_queue[:]:
            sell_id, sell_quantity, sell_price = sell_order

            if sell_id == stock_id and max_price >= sell_price:  # if stock_id is correct and the stock selling price is less than max_price
                remaining = quantity - sell_quantity    # what I need to buy - what is being sold
                if remaining <= 0:   # there is enough stock to buy
                    self.sell_queue.remove(sell_order)  # remove seller (because has all sold, or to update log)
                    if remaining < 0:   # seller still has more to sell
                        self.sell_queue.append((sell_id, -remaining, sell_price))

                    self.stock_register[stock_id] = sell_price  # update register after purchase
                    return
                else:   # there is not enough stock to buy
                    self.sell_queue.remove(sell_order)
                    quantity -= sell_quantity   # quantity = remaining stock I need to buy

                
        # end of loop(order not fullfilled) - add order to queue
        self.buy_queue.append((stock_id, quantity, max_price))
        
    
    def place_sell_order(self, stock_id, quantity, min_price):
        # Places a sell order, attempting to sell a specified quantity of a stock at a price not below than min_price.
        # The system should match the order with the highest available buy orders.
        # Orders that cannot be matched immediately are placed in a queue until they can be matched with future orders.

        #sort so that expensive stock comes first in buy_queue
        self.buy_queue.sort(key=lambda x: x[2], reverse=True)

        for buy_order in self.buy_queue[:]:
            buy_id, buy_quantity, buy_price = buy_order

            if buy_id == stock_id and min_price <= buy_price:  # check correct stock and buying price is higher than min_price
                remaining = quantity - buy_quantity    # what I need to sell - what is being bought
                if remaining <= 0:   # there is enough stock to buy
                    self.buy_queue.remove(buy_order)  # remove buyer (because has all bought, or to update log)
                    if remaining < 0:   # seller still has more to sell
                        self.buy_queue.append((buy_id, -remaining, buy_price))

                    self.stock_register[stock_id] = buy_price  # update register after purchase
                    return
                else:   # there is not enough orders to deplete sell
                    self.buy_queue.remove(buy_order)
                    quantity -= buy_quantity   # quantity = remaining stock I need to buy

        # if order not fullfilled
        self.sell_queue.append((stock_id, quantity, min_price))

    def print_all_stocks(self):
        stock_list = sorted(self.stock_register.items(), key=lambda x: x[1], reverse=True)
        print(stock_list)

stock_manager = stock_manager()
while True:
    try:
        user_input = input().split()
    except EOFError:
        break  # Stop the loop when input ends

    if not user_input:
        continue

    cmd = user_input[0]

    if cmd == "register_stock":
        stock_manager.register_stock(int(user_input[1]))
    elif cmd == "place_buy_order":
        stock_manager.place_buy_order(int(user_input[1]), int(user_input[2]), int(user_input[3]))
    elif cmd == "place_sell_order":
        stock_manager.place_sell_order(int(user_input[1]), int(user_input[2]), int(user_input[3]))
    elif cmd == "print_all_stocks":
        stock_manager.print_all_stocks()
        break


# problem: time limit -> problem: sort & remove
# solution: sort -> insert, remove -> pop