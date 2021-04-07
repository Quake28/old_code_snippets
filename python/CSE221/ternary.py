import random

list1 = random.sample(range(0, 10), 10)
list2 = [random.randint(0, 10) for a in range(10)]
print(len(list1), list1)
print(len(list2), list2)

list1.sort()
list2.sort()

#list1= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#list2= [1, 1, 4, 4, 5, 5, 6, 6, 7, 7]

print(len(list1), list1)
print(len(list2), list2)

x = int(input("x: "))
y = int(input("y: "))


def ternary(list1: list, search: int, start: int = None, end: int = None, count:int=0):
    count+=1
    if start == None:
        x = len(list1)
        start = 0
        end = len(list1) - 1
    else:
        x = end - start
    print(list1[start:end+1])
    pointer1 = start + int(x / 3)
    pointer2 = end - int(x / 3)
    if x < 3:
        if search == list1[pointer1]:
            if search == list1[pointer1 - 1]:
                return ternary(list1, search, start - 1, end - 1,count)
            return "Found at position: {} ,with {} iterations.".format(pointer1,count)
        if x > 0:
            return ternary(list1, search, start + 1, end,count)
        else:
            return "Not Found in list."
    else:
        if list1[pointer1] > search:
            end = pointer1 - 1
        elif list1[pointer2] < search:
            start = pointer2 + 1
        else:
            start = pointer1
            end = pointer2
        print(start, end)
        return ternary(list1, search, start, end,count)


print(ternary(list1, x))
print(ternary(list2, y))
