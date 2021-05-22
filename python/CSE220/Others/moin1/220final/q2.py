def sum(arr, index):
    if index == 0:
        print(arr[index], end=" ")
        return arr[index]
    else:
        x = sum(arr, index - 1) + arr[index]
        print(x, end=" ")
        return x


arr = [1, 4, 5, 2, 9, 10, 12]
a = sum(arr, len(arr) - 1)
print()
arr = [9, 10, 12, 3, 1, 0, 2]
b = sum(arr, len(arr) - 1)

