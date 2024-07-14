def max_element (array):
    if len(array) == 0 :
        return None
    a = array[0]
    for i in array :
        if i > a:
            a = i
            return a

value = max_element([1,4,6,8])
print(value)