import sys

class ProductInventory:
    __slots__ = ['_inv']
    # instead of __init__ method, we use __slots__ to define the attributes of the class
    # __slots__ is a memory optimization technique in Python that allows you to define a fixed set of attributes for a class,
    # by removing the default __dict__ attribute that stores instance attributes.
    # _dict_ is added as default to all classes in Python, which is a dictionary that stores the instance attributes of the class.

    def __init__(self):
        self._inv = []

    def add_product(self, t, id, exp_in):
        # optimized by putting calculation in append method
        self._inv.append((id, t + exp_in))

    def sell_product(self, t):
        # create inv to avoid using self._inv multiple times
        inv = self._inv

        # range checks for the last element to the first element
        # range(start, stop, step) -> range object
        # range goes in reverse order from the last element to the first element
        # this is so we can pop the last element in O(1) time, avoiding popping the first element in O(n) time
        # note: inv.pop() removes the last element in O(1) time
        for i in range(len(inv) - 1, -1, -1):
            # unpack to id_ and exp
            id_, exp = inv[i]

            # if not expired, print id_ and remove from inventory
            if exp > t:

                # print(id_)
                # instead of print, we use sys.stdout.write to avoid using print multiple times
                # sys is faster than print because it doesn't add a newline character at the end and doesn't flush the output buffer                sys.stdout.write(f"{id_}\n")
                # remove the product from the inventory
                # using inv.pop() instead of inv.pop(i)
                inv.pop(i)
                return
            

            # remove expired product
            inv.pop(i)
        # if no product is available for sale, return -1
        # or if the inventory is empty
        sys.stdout.write("-1\n")

    def get_inventory(self, t):
        # create inv to avoid using self._inv multiple times
        inv = self._inv
        
        # out is created to store the result
        # why is this faster/needed?
        out = []
        # write_pos is used to keep track of the position to write in the inventory
        write_pos = 0
        # range checks for the last element to the first element
        for i in range(len(inv)):
            # unpack to id_ and exp
            id_, exp = inv[i]
            # if not expired, add to inventory
            if exp > t:
                # update inv[write_pos] to id_ and exp
                # instead of inv[write_pos] = (id_, exp), we use inv[write_pos] = inv[i]
                # this is because we want to avoid creating a new tuple and instead use the existing tuple in the inventory
                # this is faster than creating a new tuple and assigning it to inv[write_pos]
                inv[write_pos] = inv[i]
                write_pos += 1
        # remove expired products from the inventory
        del inv[write_pos:]
        # now inv is the inventory with only the products that are not expired
        out = [inv[i][0] for i in range(write_pos - 1, -1, -1)]
        sys.stdout.write(f"{out}\n")


inv = ProductInventory()
read = sys.stdin.readline

while True:
    line = read()
    if not line:
        break

    tokens = line.split()
    if not tokens:
        continue

    cmd = tokens[0]

    if cmd == "add_product":
        inv.add_product(int(tokens[1]), int(tokens[2]), int(tokens[3]))
    elif cmd == "sell_product":
        inv.sell_product(int(tokens[1]))
    elif cmd == "get_inventory":
        inv.get_inventory(int(tokens[1]))
    elif cmd == "exit":
        break
