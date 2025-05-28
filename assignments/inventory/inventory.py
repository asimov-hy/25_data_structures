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
    inventory_specs = {}    # data base for max items in cell
    inventory_data = {} # data base for total number of items
    inventory_col = 0   # how long single line is
    inventory_size = 0  # how many cells are in input (preserve for output)



    # input for inventory_specs
    specs_input = input().strip()
    specs_input = specs_input[1:-1]
    specs = specs_input.split("),(")

    for set in specs:
        key, value = set.split(",")
        temp_inventory.append((int(key), int(value)))

    # Apply quickSort to dict
    inventory_size = len(temp_inventory)
    quickSort(temp_inventory, 0, inventory_size - 1)
    
    # convert back to dictionary
    inventory_specs = dict(temp_inventory)
    inventory_data = {key: 0 for key in inventory_specs.keys()}

    # print(inventory_specs)
    # print("-"*20)
    # print(inventory_data)
    
    
    inventory_size = 0
    # rest of input
    while True:
        try:
            
            line = input().strip()

            # if no more lines then break
            if not line:
                break

            # yes lines

            # update how many cells in single line
            if inventory_col == 0:
                inventory_col = len(line.split(","))
            # update inventory size to reflect how many cells are in input (excluding specs)
            inventory_size += inventory_col
            
            # strip line
            for item in line.split(","):
                # strip to per item
                item = item.strip()
                print(item)

                # # item is - == empty cell, move onto next
                # if item == "-":
                #     continue

                # # else if item is (a, b) then save to inventory_data key:a value += b
                # else:
                #     item = item.strip("()")
                #     item_id, item_count = map(int, item.split(","))
                #     inventory_data[item_id] += item_count
            
        except EOFError:
            break

    print(inventory_size)
    print(inventory_data)

    # print inventory

    # list of item id
    id_list = [item_id for item_id, _ in temp_inventory]

    #for range in inventory_size (run the number of times the input has (excluding spec))
    cell = 0
    for count in range(inventory_size): # loop the number of cells from input
        item_id = id_list[cell]


        # if items remaining exists print
        if cell < inventory_size:   # id_list has not been exhausted

            # print ever item in inventory_data from beinnign to end, max is from inventory_specs
            if inventory_data[item_id] > inventory_specs[item_id]:
                print(f"({item_id},{inventory_specs[item_id]})", end="")
                inventory_data[item_id] -= inventory_specs[item_id]

            # remaining items are less than inventory max
            else:
                print(f"({item_id},{inventory_data[item_id]})", end="")
                inventory_data[item_id] = 0

            cell += 1
            # no items remaining: print -
        else:
            print("-", end="")
        

        if (count+1) % inventory_col == 0:
            print()
