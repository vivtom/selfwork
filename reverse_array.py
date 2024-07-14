def reverse_string(array):
    i = 0
    j = len(array)-1

    while i < j:
        array[i],array[j] = array[j],array[i]
        i += 1
        j -= 1

        print(array)
reverse_string([2,5,6])
