def remove_duplicate(arr):
    seen = set()
    array = []
    for i in arr:
        if i not in seen:
            seen.add(i)
            array.append(i)
    return array

result = remove_duplicate([1,2,3,2,4])
print(result)