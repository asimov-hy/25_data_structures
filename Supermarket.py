# 공식 제출 코드

# You are tasked with developing a system to manage the inventory of produced goods(egg, milk, bread, etc.) for a supermarket.
# == create structure

# The system should ensure that the freshest products (the most recently produced ones) are sold first,
#   while products that have expired should not be sold.
# == stack with recent being on top of stack

# Each product in the inventory has the following properties:
# == structure variables

    # id: An integer representing the unique identifier for the product.

    # current_timestamp: An integer representing the Unix timestamp at the time the method is called. 
    #   This value is used to determine the current time and is guaranteed to be monotonically increasing.

    # expires_in: An integer representing the duration in seconds until the product expires (from the current_timestamp). 
    #   The product is immediately unavailable for sale once it reaches its expiration.


# Implement the ProductInventory class:

class ProductInventory:
    def __init__(self):
        # create empty stack
        self._inventory = []
    
    # add_product(current_timestamp, id, expires_in): Adds a product with the specified id to the inventory. 
    #   The product expires in expires_in seconds from the current_timestamp.
    # == add element to stack
    def add_product(self, current_timestamp: int, id: int, expires_in: int):
        
        expiration = current_timestamp + expires_in # save expiration instead of expires_in for optimized calculations
        self._inventory.append([id, expiration])    # add data to inventory list
    
    # sell_product(current_timestamp): Removes the most recently added product that has not expired from the inventory and returns 
    #   its id. If no product is available for sale, return -1.
    def sell_product(self, current_timestamp: int):
        # print most recent product that hasn't passed expiration

        # if empty list
        if len(self._inventory) == 0:
            print(-1)
            return
        
        # if not empty list
        index = len(self._inventory) - 1
        
        while index >= 0:
            product_id, expiration = self._inventory[index]
            # if not expired print, remove and return and return
            if expiration > current_timestamp:
                print(product_id)
                self._inventory.pop(index)
                return
            else:
                self._inventory.pop(index)
            
            index -= 1
        
        # if end of loop == no product
        print(-1)


    # get_inventory(current_timestamp): Returns a list of all product ids currently in the inventory that have not expired, 
    #   sorted by the timestamp they were added to the inventory, from the freshest to the oldest.
    def get_inventory(self, current_timestamp):
        # print not expired inventory

        current_inventory = []
        index = len(self._inventory) - 1  # Start from the last element
        while index >= 0:
            product_id, expiration = self._inventory[index]
            if expiration <= current_timestamp:
                self._inventory.pop(index)  # Remove expired product
            else:
                current_inventory.append(product_id)
            index -= 1
            
        print(current_inventory)
        
        # print
        # print(f"[{', '.join(map(str, inventory_list))}]")

        # other solution for print
        # print [ and ] at beginning and end and pring product_id within loop
        # problem - the comma - need seperate operation for testing first or last element to be printed 
        # (most likely first as knowing last element is a problem)

# create instance of ProductInventory
inventory = ProductInventory()

while True:
    try:
        user_input = input().split()
    except EOFError:
        break  # Stop the loop when input ends

    if not user_input:
        continue

    cmd = user_input[0]

    if cmd == "add_product":
        num1, num2, num3 = map(int, user_input[1:])
        inventory.add_product(num1, num2, num3)
    elif cmd == "sell_product":
        num1 = int(user_input[1])
        inventory.sell_product(num1)
    elif cmd == "get_inventory":
        num1 = int(user_input[1])
        inventory.get_inventory(num1)
    elif cmd == "exit":
        break

    # debug - inventory after action
    #print(inventory._inventory)

# problem 1) only most recent input is saved
# solution - init was within loop -> constant reset

# problem 2) starts with Invalid command print
# solution - remove lint

# problem 3) large input breaks file
# solution - not breaking, just wrong output
# --> unify if statements and conditions to not get confused + check output order
