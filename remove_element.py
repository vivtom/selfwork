def remove_element(arr, val):
    i = 0
    while i < len(arr):
        if arr[i] == val:
            arr.pop(i)
        else:
            i += 1
            # print(i)
    return arr, len(arr)
results = remove_element([1,2,3,4,3,5], 3)
print(results)