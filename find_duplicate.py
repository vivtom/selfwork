def find_num(array):
    final = set()
    for i in array:
        if i in final:
            return i
        else:
            final.add(i)
results = find_num([1,3,4,2,5,3])
print(results)
