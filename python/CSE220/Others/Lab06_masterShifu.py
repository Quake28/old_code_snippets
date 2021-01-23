#task1
def selectionSort(arr):
    minimum=low(arr)
    if minimum!=0:
        temp = arr[0]
        arr[0] = arr[minimum]
        arr[minimum] = temp
    if len(arr)!=1:
        arr=arr[:1]+selectionSort(arr[1:])
    return arr

def low(arr,current=1,minimum=0):
    if current<len(arr):
        if arr[current]<arr[minimum]:
            minimum=low(arr,current+1,current)
        else:
            minimum=low(arr,current+1,minimum)
    return minimum

#task2
def insertionSort(arr,count=1):
    if count<len(arr):
        temp=arr[count]
        arr,swap=insert(arr,count)
        arr[swap]=temp
        insertionSort(arr,count+1)

    return arr

def insert(arr,count,temp=None):
    temp2 = count
    if temp==None:
        temp=arr[count]
    if count>0:
        if arr[count-1]>temp:
            arr[count]=arr[count-1]
            return insert(arr,count-1,temp)
        else:
            return arr,temp2
    else:
        return arr,temp2
#node
class Node:
    def __init__(self,value,next=None,previous=None):
        self.value=value
        self.next=next
        self.previous=previous

def doublelinked(arr):
    head=Node(arr[0])
    loop1=head
    for a in arr[1:]:
        loop1.next=Node(a)
        loop1=loop1.next
    loop1=head
    while True:
        if loop1.next==None:
            break
        loop1.next.previous=loop1
        loop1=loop1.next
    return head

def printer(self):
    if self.next==None:
        return str(self.value)
    return str(self.value)+" "+printer(self.next)

#task3
def linkedBubbleSort(head):
    loop1 = head
    while True:
        loop2=head
        if loop1.next==None:
            break
        while True:
            if loop2.next==None:
                break
            if loop2.value>loop2.next.value:
                temp=loop2.next.value
                loop2.next.value=loop2.value
                loop2.value=temp
            loop2=loop2.next
        loop1=loop1.next
    return head

#task4
def linkedSelectionSort(head):
    loop1 = head
    while True:
        loop2=loop1.next
        min=loop1
        if loop1.next==None:
            break
        while True:
            if loop1.value>loop2.value:
                min=loop2
            if loop2.next==None:
                break
            loop2=loop2.next
        temp = min.value
        min.value = loop1.value
        loop1.value = temp
        loop1=loop1.next
    return head

#task5
def linkedInsertionSort(head):
    loop1 = head.next
    while True:
        loop2=loop1
        if loop1==None:
            break
        temp=loop1.value
        while True:
            if loop2.previous == None:
                break
            if loop2.previous.value>temp:
                loop2.value=loop2.previous.value
            else:
                break
            loop2=loop2.previous
        loop2.value = temp
        loop1=loop1.next
    return head


#task6
def binarySearch(arr, item, current=0, count=0):
    if count==0:
        end=len(arr)
    mid = int(len(arr) / 2)
    if len(arr)==1:
        if arr[mid]==item:
            return str(item)+" was found in the list"
        else:
            return str(item)+" was not found in the list"
    elif arr[mid]==item:
        return str(item)+" was found in the list"
    elif arr[mid]<item:
        return binarySearch(arr[mid+1:],item, current+mid+1, 1)
    elif arr[mid]>item:
        return binarySearch(arr[:mid],item, current-mid, 1)

#task7
storage_list=[1, 1, 2, 3, 5, 8, 13, 21, 34]
def memoization(n,previous=0,current=1):
    if previous==0 and current==1:
        if n==len(storage_list):
            return storage_list[n-1]
        elif n>len(storage_list):
            return memoization(n-len(storage_list),storage_list[-2],storage_list[-1])
    elif n!=0:
        storage_list.append(previous+current)
        return memoization(n-1,current,storage_list[-1])
    else:
        return current
arr1=[9,1,3,6,8,7,4,2,0,5]
arr2=[0,1,2,3,4,5,6,7,8,9]
linked = doublelinked(arr1)
#print(printer(linked))

print(selectionSort(arr1))
print(insertionSort(arr1))
print(printer(linkedBubbleSort(linked)))
print(printer(linkedSelectionSort(linked)))
print(printer(linkedInsertionSort(linked)))
print(binarySearch(arr2,0))
print(memoization(46))
print(storage_list)
