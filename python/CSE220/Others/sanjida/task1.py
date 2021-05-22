# 1. Sort an array RECURSIVELY using selection sort algorithm.
# TASK 1
def selection_recursive(array, unsorted=0):
    if unsorted < len(array) - 1:
        lowest = unsorted + min(array[unsorted:])
        if lowest != unsorted:
            temp = array[unsorted]
            array[unsorted] = array[lowest]
            array[lowest] = temp
        selection_recursive(array, unsorted + 1)
    return array


def min(array, curr=1, lowest=0):
    if curr < len(array):
        if array[curr] < array[lowest]:
            lowest = min(array, curr + 1, curr)
        else:
            lowest = min(array, curr + 1, lowest)
    return lowest


array1 = [8, 9, 0, 6, 7, 5, 3, 4, 1, 2]
print(selection_recursive(array1))
