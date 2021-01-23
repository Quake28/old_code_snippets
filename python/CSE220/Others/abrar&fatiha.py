'''
1. Sort an array RECURSIVELY using selection sort algorithm.
2. Sort an array RECURSIVELY using insertion sort algorithm.
3. Sort a singly linked sequential list using bubble sort algorithm.
4. Sort a singly linked sequential list using selection sort algorithm.
5. Sort a DOUBLY linked sequential list using insertion sort algorithm.
6. Implement binary search algorithm RECURSIVELY.
7. Implement a recursive algorithm to find the n-th Fibonacci number using memoization.
'''
########################################################################
# Task 1

def selection_sort(arr):
    if len(arr)>1:
        low=lowest(arr)
        temp=arr[0]
        arr[0]=arr[low]
        arr[low]=temp
        return arr[:1]+selection_sort(arr[1:])
    else:
        return arr
def lowest(arr,low=0,index=0):
    if index<len(arr):
        if arr[index]<arr[low]:
            low=index
        return lowest(arr,low,index+1)
    else:
        return low

array=[9,8,7,6,5,4,3,2,1]
print(array,"\n")
#print(selection_sort(array))

########################################################################
# Task 2

def insertion_sort(arr,index=1):
    if index<len(arr):
        temp=arr[index]
        arr,curr=shift(arr,temp,index-1)
        arr[curr]=temp
        return insertion_sort(arr,index+1)
    else:
        return arr
def shift(arr,temp,curr):
    if curr>=0:
        if arr[curr]>temp:
            arr[curr+1]=arr[curr]
            return shift(arr,temp,curr-1)
        else:
            return arr,curr
    else:
        return arr,curr+1

print(insertion_sort(array))
