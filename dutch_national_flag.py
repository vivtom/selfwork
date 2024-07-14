def dutch_national_flag(array):
    start = 0
    end = len(array)-1
    mid = 0
    for _ in range(len(array)):
        if mid > end:
            break
        elif array[mid] == 0:
            array[start],array[mid] = array[mid], array[start]
            mid += 1
            start += 1
        elif array[mid] == 1:
            mid += 1
        else:
            array[end], array[mid] = array[mid], array[end]
            end -= 1
    return array

sol = dutch_national_flag([1,0,2,1,2])
print(sol)