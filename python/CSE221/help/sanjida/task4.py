import random
def mergeSort(arr):
    arr=[[a] for a in arr]
    while len(arr)>1:
        leftArr=arr[0]
        rightArr=arr[1]
        arr.pop(0)
        arr.pop(0)
        newArr = []
        leftLen=len(leftArr)
        rightLen=len(rightArr)
        while leftLen>0 and rightLen>0:
            if rightArr[0]<leftArr[0]:
                newArr.append(rightArr[0])
                rightArr.pop(0)
                rightLen-=1
            elif rightArr[0]>leftArr[0]:
                newArr.append(leftArr[0])
                leftArr.pop(0)
                leftLen-=1
            else:
                newArr.append(leftArr[0])
                leftArr.pop(0)
                leftLen-=1
                newArr.append(rightArr[0])
                rightArr.pop(0)
                rightLen-=1
        while leftLen>0:
            newArr.append(leftArr[0])
            leftArr.pop(0)
            leftLen-=1
        while rightLen>0:
            newArr.append(rightArr[0])
            rightArr.pop(0)
            rightLen-=1
        arr.append(newArr)
    return arr[0]
    
    
    
array1=[random.randint(0,100) for a in range(10)]
print(array1)
print(mergeSort(array1))