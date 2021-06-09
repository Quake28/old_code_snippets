# 2. Sort an array RECURSIVELY using insertion sort algorithm.
# TASK 2
def insertion_recursive(array, count=1):
    if count < len(array):
        temp = array[count]
        array, swap = insert(array, count)
        array[swap] = temp
        # print() # DEBUG
        insertion_recursive(array, count + 1)

    return array


def insert(array, count, temp=None):
    # print(array,count,array[count-1],temp) # DEBUG
    temp2 = count
    if temp == None:
        temp = array[count]
    if count > 0:
        if array[count - 1] > temp:
            array[count] = array[count - 1]
            return insert(array, count - 1, temp)
        else:
            return array, temp2
    else:
        return array, temp2


array1 = [8, 9, 0, 6, 7, 5, 3, 4, 1, 2]
print(insertion_recursive(array1))
