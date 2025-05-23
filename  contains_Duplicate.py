set1 = set()
def contains_duplicate(arr):
    for i in arr:
        if i in set1:
            return True
        else:
            set1.add(i)
    return False
print(contains_duplicate([1,2,3]))
