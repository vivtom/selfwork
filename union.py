def union(arr1,arr2):
    final = set()
    for i in arr1:
        final.add(i)
    for j in arr2:
        final.add(j)
    print(final)
union([2,3,4], [5,6,4])