def move_zeroes(array):
    left = 0
    for right in array:
        if array[right] != 0:
            array[left], array[right] = array[right], array[left]
            left += 1
    return array

result = move_zeroes([0,5,4,5,0,6])
print(result)