def shiftLeft(arr,k):
    for a in range(k):
        arr.pop(0)
        arr.append(0)
    return arr

def rotateLeft(arr,k):
    for a in range(k):
        x=arr.pop(0)
        arr.append(x)
    return arr

def remove(arr, length, idx):
    if idx<length:
        arr.pop(idx)
    return arr

def removeAll(arr, len, num):
    for a in range(len):
        if arr[a]==num:
            arr.pop(a)
    return arr


def main():
    print(shiftLeft([10,20,30,40,50,60],3))
    print(rotateLeft([10,20,30,40,50,60],3))
    print(remove([10,20,30,40,50,60],6,6))
    print(removeAll([10,20,30,40,50,60,10],7,10))

main()


