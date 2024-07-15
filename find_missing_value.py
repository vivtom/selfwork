def find_missing_value(array, n):
    array.sort()
    n = 0
    for i in array:
        n += 1
        if i != n:
            return n
    return n + 1

results = find_missing_value([1,2,4,5], 5)
print(results)