# 6. Implement binary search algorithm RECURSIVELY.
# TASK 6
def binary_recursive(array, item, start=0, end=0, count=0):
    if count == 0:
        end = len(array)
    x = (end - start) / 2 - 1
    if x % 1 != 0:
        x += 0.5
    x = int(x)
    if x < 0:
        return "{} was not found in the array".format(item)
    elif array[start + x] == item:
        return "{} found in location {}".format(item, start + x)
    elif array[start + x] < item:
        start += x + 1
    elif array[start + x] > item:
        end -= x + 1
    return binary_recursive(array, item, start, end, 1)


array2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(binary_recursive(array2, 9))
