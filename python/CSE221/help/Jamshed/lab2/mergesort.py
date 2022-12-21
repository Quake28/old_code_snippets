def mergeSort(arr):
    if len(arr)==1:
        return arr
    else:
        mid=int(len(arr)/2)
        arr1=mergeSort(arr[:mid])
        arr2=mergeSort(arr[mid:])
        new_arr=[]
        pointer1=0
        pointer2=0
        for a in range(len(arr)):
            if arr1[pointer1]<arr2[pointer2]:
                new_arr.append(arr1[pointer1])
                pointer1+=1
            elif arr1[pointer1]>arr2[pointer2]:
                new_arr.append(arr2[pointer2])
                pointer2+=1
            else:
                new_arr.append(arr1[pointer1])
                pointer1+=1
                new_arr.append(arr2[pointer2])
                pointer2+=1
            if pointer1>=len(arr1):
                new_arr+=arr2[pointer2:]
                break
            elif pointer2>=len(arr2):
                new_arr+=arr1[pointer1:]
                break
        return new_arr

if __name__=="__main__":
    arr=[7,8,3,4,2,9]
    sorted=mergeSort(arr)
    print(arr)
    print(sorted)
