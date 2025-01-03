array = input('Enter array : ').split()
x = input('what do you want to find? : ')
found = False
for i in range(len(array)): #we want to stop after the last element hence here we wanted to use the indexes hence we used in range(len(array))
        if x == array[i]:
            print(i)
            found = True
            break
if not found :
        print('it does not exist ','\ntry with some other number.')
        