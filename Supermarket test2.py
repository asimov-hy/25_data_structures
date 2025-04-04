class ProductInventory:
    def __init__(self):
        self._inventory = []

    def add_product(self, current_timestamp: int, id: int, expires_in: int):
        expiration = current_timestamp + expires_in
        self._inventory.append([id, expiration])

    def sell_product(self, current_timestamp: int):
        while self._inventory:
            product_id, expiration = self._inventory[-1]
            if expiration > current_timestamp:
                print(product_id)
                self._inventory.pop()
                return
            else:
                self._inventory.pop()
        print(-1)

    def get_inventory(self, current_timestamp: int):
        while self._inventory and self._inventory[-1][1] <= current_timestamp:
            self._inventory.pop()

        result = [item[0] for item in reversed(self._inventory)]
        print(result)


# ====== Read from .in file and print output to console ======
if __name__ == "__main__":
    input_filename = "test.0.0.in"  # Change as needed

    inventory = ProductInventory()

    with open(input_filename, 'r') as input_file:
        for line in input_file:
            tokens = line.strip().split()
            if not tokens:
                continue

            cmd, *args = tokens

            if cmd == "add_product":
                t, id, exp = map(int, args)
                inventory.add_product(t, id, exp)
            elif cmd == "sell_product":
                t = int(args[0])
                inventory.sell_product(t)
            elif cmd == "get_inventory":
                t = int(args[0])
                inventory.get_inventory(t)
            elif cmd == "exit":
                break
