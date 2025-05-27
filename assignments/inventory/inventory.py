def partition(arr, low, high):
    pivot = arr[high][0]
    i = low -1
    for j in range(low, high):
        if arr[j][0] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
    


if __name__ == "__main__":

    # save inventory id and stack size
    temp_inventory = []
    inventory_specs = {}
    inventory_data = {}
    inventory_col = 0
    inventory_size = 0



    # input for inventory_specs
    specs_input = input().strip()
    specs_input = specs_input[1:-1]
    specs = specs_input.split("),(")

    for set in specs:
        key, value = set.split(",")
        temp_inventory.append((int(key), int(value)))

    # Apply quickSort
    inventory_size = len(temp_inventory)
    quickSort(temp_inventory, 0, inventory_size - 1)
    
    # convert back to dictionary
    inventory_specs = dict(temp_inventory)
    inventory_data = {key: 0 for key in inventory_specs.keys()}

    # print(inventory_specs)
    # print("-"*20)
    # print(inventory_data)
    
    # rest of input
    while True:
        try:
            line = input().strip()
            if inventory_col == 0:
                inventory_col = len(line.split(","))


            if not line:
                break
            # if item is- then skip

            for item in line.split("),"):

                item = item.strip()

                if item == "-":
                    continue

                # else if item is (a, b) then save to inventory_data
                else:
                    item = item.strip("()")
                    item_id, item_count = map(int, item.split(","))
                    inventory_data[item_id] += item_count
            
        except EOFError:
            break

    # print inventory
    #for range in inventory_size:
    cell = 0
    for count in range(inventory_size):
        # if remaining item exists print
        if cell < inventory_size - 1:
            if count < inventory_size - 1:
                # print ever item in inventory_data from beinnign to end, max is from inventory_specs
                if inventory_data[cell] > inventory_specs[cell]:
                    print(f"({cell},{inventory_specs[cell]})", end="")
                    inventory_data[cell] -= inventory_specs[cell]
                else:
                    print(f"({cell},{inventory_data[cell]})", end="")
                    inventory_data[cell] = 0
                cell += 1
        # no items remaining: print -
        else:
            print(f"({cell},{inventory_data[cell]})", end="")
        

        if (count+1) % inventory_col == 0:
            print()
