def intersection(arr1,arr2):
    first = set(arr1)
    final = []
    for i in arr2:
        if i in arr1:
            final.append(i)
            first.remove(i)
    return final
hey = intersection([1,2,3,4], [2,3,4,5])
print(hey)
