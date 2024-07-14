def rotate_arr(array, n):
    n = n % len(array)
    reverse(array, 0, len(array) - 1)
    reverse(array, 0, n - 1)
    reverse(array, n, len(array) - 1)

def reverse(array, start, end):
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1


arr = [2, 3, 4, 5, 6]
rotate_arr(arr, 3)
print(arr)