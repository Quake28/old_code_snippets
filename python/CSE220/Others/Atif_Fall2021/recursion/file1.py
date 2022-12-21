"""
Sort an array RECURSIVELY using selection sort algorithm.
Sort an array RECURSIVELY using insertion sort algorithm.
Sort a singly linked sequential list using bubble sort algorithm.
Sort a singly linked sequential list using selection sort algorithm.
Sort a DOUBLY linked sequential list using insertion sort algorithm.
Implement binary search algorithm RECURSIVELY.
Implement a recursive algorithm to find the n-th Fibonacci number using memoization.
"""

"""
# TASK 1

def selection(arr,pos=0):
    if pos==len(arr)-1:
        return arr
    min=pos
    for a in range(pos+1,len(arr)):
        print(a,arr[a],min,arr[min])
        if arr[a]<arr[min]:
            min=a
    arr[pos],arr[min] = arr[min],arr[pos]
    print(arr)
    print()
    return selection(arr,pos+1)

print([5,2,1,8,3,9,2],"\n")
print(selection([5,2,1,8,3,9,2]))


# TASK 2


def insertion(arr,pos=1):
    if pos==len(arr):
        return arr
    curr = arr[pos]
    for a in range(pos-1,-1,-1):
        if arr[a]>curr:
            arr[a+1]=arr[a]
        else:
            a+=1
            break
    arr[a]=curr
    print(arr)
    print()
    return insertion(arr,pos+1)

print([5,2,1,8,3,9,2],"\n")
print(insertion([5,2,1,8,3,9,2]))


# TASK 6

def bin(arr,search,str=0,end=None):
    if end==None:
        end=len(arr)-1
    #print(str,end)
    if str==end:
        if arr[str]==search:
            return str
        else:
            return None
    else:
        mid=int((str+end)/2)
        if arr[mid]==search:
            return mid
        elif arr[mid]>search:
            return bin(arr,search,str,mid-1)
        else:
            return bin(arr,search,mid+1,end)

returned_value=bin([1, 2, 2, 3, 5, 8, 9],1)
if returned_value!=None:
    print(returned_value)
else:
    print("Not found")


# TASK 7

memory={1:0,2:1}
def memfib(num):
    if num in memory:
        return memory[num]
    else:
        fib=memfib(num-1)+memfib(num-2)
        memory[num]=fib
        return fib

print(memfib(2566))

"""

# NODE CLASS
class Node:
    def __init__(self,value,next=None,prev=None):
        self.value=value
        self.next=next
        self.prev=prev

    def singly_linked_list(arr):
        head=Node(arr[0])
        curr=head
        for a in arr[1:]:
            curr.next=Node(a)
            curr=curr.next
        return head

    def printer(head):
        while head!=None:
            print(head.value,end="")
            if head.next!=None:
                print(" -> ",end="")
            head=head.next
        print()

    def length(head):
        count=0
        while head!=None:
            count+=1
            head=head.next
        return count
import random
list1=Node.singly_linked_list([random.randint(0,100) for a in range(10)])
Node.printer(list1)
length = Node.length(list1)
#print(length)

"""
# Task 3 - Bubble Sort

for b in range(length):
    curr=list1
    for a in range(length-1):
        if curr.value>curr.next.value:
            curr.value,curr.next.value = curr.next.value,curr.value
        curr=curr.next
Node.printer(list1)


# Task 4 - Selection Sort
curr_1=list1
for b in range(length-1):
    curr_2=curr_1
    minimum=curr_2
    for a in range(length-b):
        if curr_2.value<minimum.value:
            minimum=curr_2
        curr_2=curr_2.next
    curr_1.value,minimum.value=minimum.value,curr_1.value
    curr_1=curr_1.next
Node.printer(list1)

"""
