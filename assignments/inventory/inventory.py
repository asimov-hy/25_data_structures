def partition(arr, low, high):
    pivot = arr[high]
    i = low -1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i+1, high)
    return i + 1

def quick_sort(S):
    n = len(S)
    if n < 2:
        returnP = S.first()
    


if __name__ == "__main__":

    # save inventory id and stack size
    inventory_specs = {}
    inventory_data = []
    inventory_col = 0
    inventory_size = 0



    # input for inventory_specs
    specs_input = input().strip()
    specs_input = specs_input[1:-1]
    specs = specs_input.split("),(")

    for set in specs:
        key, value = set.split(",")
        inventory_specs[key] = int(value)
    
    # sort dictionary

        # first line = inventory specs
        
        # sort first line =  inventory specs

        # store rest into data
        # remember N X M specs

    # print inventory
    #for range in inventory_size:
        # if remaining item exists print
            # if still on same row then print ,
            # else new row print \n
        # else print -