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
            # remove all ( , ) from line
            line = input().strip()

            if not line:
                break
            
            cells = line.replace("-", "(e,e)").replace('),(', ')#(').split('#')
            # (e, e) fake cell for easier format

            for item in cells:
                
                item = item.strip(",")
                # print(item)
                
                # item is "(a,b)"
                item = item.strip("()")
                item_id, item_count = item.split(",")

                # empty cell
                if item_id == "e":
                    #print("empty cell")
                    continue

                inventory_data[int(item_id)] += int(item_count)
                # print(f"{item_count} added to {item_id}")

            # (1,5),(2,10),(3,9)
            # -,(3,2),(1,5)
            
            if inventory_col != 0 and inventory_col != len(cells):
                print("error in col size")
                break
            inventory_col = len(cells)         # e.g. columns per row
            inventory_size += inventory_col

        except EOFError:
            break

    # print(inventory_size)
    # print(inventory_col)
    # print(inventory_data)

    # list of items
    id_list = [item_id for item_id, _ in temp_inventory]

    
    # track which item is being printed
    cell = 0
    item_dat = len(id_list)  # how many items in id_list

    # print inventory_size number of cells
    for count in range(inventory_size):
        
        # no more items to print
        if cell >= item_dat:
            print("-", end="")

        # items left to print
        else:
            # get item id from id_list
            item_id = id_list[cell]

            # print ever item in inventory_data from beinnign to end, max is from inventory_specs
            if inventory_data[item_id] > inventory_specs[item_id]:
                print(f"({item_id},{inventory_specs[item_id]})", end="")
                inventory_data[item_id] -= inventory_specs[item_id]

            # remaining items are less than inventory max
            else:
                print(f"({item_id},{inventory_data[item_id]})", end="")
                inventory_data[item_id] = 0

                # move to next item
                cell += 1
                

        # if row has been filled, print new line
        if (count+1) % inventory_col == 0:
            print()
        else:
            print(",", end="")