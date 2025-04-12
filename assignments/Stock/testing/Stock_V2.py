class stock_manager:

    def __init__(self):
        self.stock_register = {}    # id, price(most recent transaction)
        self.buy_queue = []     # id, quantity, max_price
        self.sell_queue = []    # id, quantity, min_price

    def register_stock(self, stock_id):
        if stock_id not in self.stock_register:
            self.stock_register[stock_id] = 0
    
    def place_buy_order(self, stock_id, quantity, max_price):

        #self.sell_queue.sort(key=lambda x: x[2])

        index = 0
        while index < len(self.sell_queue) and quantity > 0:
            sell_id, sell_quantity, sell_price = self.sell_queue[index]

            if sell_id == stock_id and max_price >= sell_price:  # if stock_id is correct and the stock selling price is less than max_price
                remaining = quantity - sell_quantity    # what I need to buy - what is being sold

                if remaining <= 0:   # there is enough stock to buy
                    if remaining < 0:
                        self.sell_queue[index] = (sell_id, -remaining, sell_price)
                    else:
                        self.sell_queue.pop(index)
                    self.stock_register[stock_id] = sell_price
                    return
                else:   # there is not enough stock to buy
                    self.sell_queue.pop(index)
                    quantity -= sell_quantity   # quantity = remaining stock I need to buy
                    self.stock_register[stock_id] = sell_price

            index += 1
        # end of loop(order not fullfilled) - add order to queue
        low, high = 0, len(self.buy_queue)
        while low < high:
            mid = (low + high) // 2
            if self.buy_queue[mid][2] < max_price:
                high = mid
            else:
                low = mid + 1
        self.buy_queue.insert(low, (stock_id, quantity, max_price))
        
    
    def place_sell_order(self, stock_id, quantity, min_price):
        index = 0
        while index < len(self.buy_queue) and quantity > 0:
            buy_id, buy_quantity, buy_price = self.buy_queue[index]

            if buy_id == stock_id and min_price <= buy_price:
                remaining = quantity - buy_quantity

                if remaining <= 0:  # enough to fully sell
                    if remaining < 0:
                        self.buy_queue[index] = (buy_id, -remaining, buy_price)
                    else:
                        self.buy_queue.pop(index)
                    self.stock_register[stock_id] = buy_price
                    return
                else:  # partial match
                    self.buy_queue.pop(index)
                    quantity -= buy_quantity
                    self.stock_register[stock_id] = buy_price
                    continue  # re-check same index after pop

            index += 1

        # if order not fulfilled, insert into sell_queue in sorted order (ascending min_price)
        low, high = 0, len(self.sell_queue)
        while low < high:
            mid = (low + high) // 2
            if self.sell_queue[mid][2] > min_price:
                high = mid
            else:
                low = mid + 1
        self.sell_queue.insert(low, (stock_id, quantity, min_price))


    def print_all_stocks(self):
        stock_list = sorted(self.stock_register.items(), key=lambda x: x[1], reverse=True)
        print(stock_list)




if __name__ == "__main__":
    input_filename = "stock_test.in"

    manager = stock_manager()  # no need to pass output_writer

    with open(input_filename, 'r') as input_file:
        for line in input_file:
            tokens = line.strip().split()
            if not tokens:
                continue

            cmd, *args = tokens

            if cmd == "register_stock":
                stock_id = int(args[0])
                manager.register_stock(stock_id)

            elif cmd == "place_buy_order":
                stock_id, quantity, max_price = map(int, args)
                manager.place_buy_order(stock_id, quantity, max_price)

            elif cmd == "place_sell_order":
                stock_id, quantity, min_price = map(int, args)
                manager.place_sell_order(stock_id, quantity, min_price)

            elif cmd == "print_all_stocks":
                manager.print_all_stocks()
                break

            elif cmd == "exit":
                break




# problem: time limit