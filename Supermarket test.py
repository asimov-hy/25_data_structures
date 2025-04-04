class ProductInventory:
    def __init__(self, output_writer):
        self._inventory = []
        self._output_writer = output_writer

    def add_product(self, current_timestamp: int, id: int, expires_in: int):
        expiration = current_timestamp + expires_in
        self._inventory.append([id, expiration])

    def sell_product(self, current_timestamp: int):
        if not self._inventory:
            self._output_writer.write("-1\n")
            return

        index = len(self._inventory) - 1
        while index >= 0:
            product_id, expiration = self._inventory[index]
            if expiration > current_timestamp:
                self._output_writer.write(f"{product_id}\n")
                self._inventory.pop(index)
                return
            else:
                self._inventory.pop(index)
            index -= 1

        self._output_writer.write("-1\n")

    def get_inventory(self, current_timestamp):
        current_inventory = []
        index = len(self._inventory) - 1
        while index >= 0:
            product_id, expiration = self._inventory[index]
            if expiration <= current_timestamp:
                self._inventory.pop(index)
            else:
                current_inventory.append(product_id)
            index -= 1

        result = current_inventory
        self._output_writer.write(f"{result}\n")


# ====== Entry point for named .in and .out files ======
if __name__ == "__main__":
    input_filename = "test.0.0.in"
    output_filename = "test.0.0.out"

    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        inventory = ProductInventory(output_writer=output_file)

        for line in input_file:
            line = line.strip()
            if not line:
                continue

            tokens = line.split()
            cmd = tokens[0]

            if cmd == "add_product":
                t, id, exp = map(int, tokens[1:])
                inventory.add_product(t, id, exp)
            elif cmd == "sell_product":
                t = int(tokens[1])
                inventory.sell_product(t)
            elif cmd == "get_inventory":
                t = int(tokens[1])
                inventory.get_inventory(t)
            elif cmd == "exit":
                break
