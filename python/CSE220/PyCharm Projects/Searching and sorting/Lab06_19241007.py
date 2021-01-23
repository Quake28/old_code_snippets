'''
1. Sort an array RECURSIVELY using selection sort algorithm.
2. Sort an array RECURSIVELY using insertion sort algorithm.
3. Sort a singly linked sequential list using bubble sort algorithm.
4. Sort a singly linked sequential list using selection sort algorithm.
5. Sort a DOUBLY linked sequential list using insertion sort algorithm.
6. Implement binary search algorithm RECURSIVELY.
7. Implement a recursive algorithm to find the n-th Fibonacci number using memoization.
'''

##############################################################

# TASK 1
def selection_recursive(array,unsorted=0):
    #print(unsorted,array) #debug
    if unsorted<len(array)-1:
        lowest=unsorted+min(array[unsorted:])
        if lowest!=unsorted:
            temp = array[unsorted]
            array[unsorted] = array[lowest]
            array[lowest] = temp
        selection_recursive(array, unsorted + 1)
    return array

def min(array,curr=1,lowest=0):
    if curr<len(array):
        if array[curr]<array[lowest]:
            lowest=min(array,curr+1,curr)
        else:
            lowest=min(array,curr+1,lowest)
    return lowest

##############################################################

# TASK 2
def insertion_recursive(array,count=1):
    if count<len(array):
        temp=array[count]
        array,swap=insert(array,count)
        array[swap]=temp
        #print() # DEBUG
        insertion_recursive(array,count+1)

    return array

def insert(array,count,temp=None):
    #print(array,count,array[count-1],temp) # DEBUG
    temp2 = count
    if temp==None:
        temp=array[count]
    if count>0:
        if array[count-1]>temp:
            array[count]=array[count-1]
            return insert(array,count-1,temp)
        else:
            return array,temp2
    else:
        return array,temp2

##############################################################

# NODE CLASS - with modified string so that it is easier to see output
class Node:
    def __init__(self,value=None,next=None,prev=None):
        # Doing this solely because I don't want to deal with multiple Node classes
        # This essentially allows me to use more than one type of Node in 1 Node class
        self.value=value
        self.next=next
        self.prev=prev
    def __str__(self):
        if self.next==None:
            return str(self.value)
        return str(self.value)+" "+self.next.__str__()

def doubleLinked(array):
    head=Node(array[0])
    head1=head
    for a in array[1:]:
        head1.next=Node(a)
        head1=head1.next
    head1=head
    while True:
        if head1.next==None:
            break
        head1.next.prev=head1
        head1=head1.next
    return head

# Loop to print Linked list using .prev
def reverse(head):
    while True:
        if head.next==None:
            break
        head=head.next
    while True:
        print(head.value)
        if head.prev==None:
            break
        head=head.prev

##############################################################

# TASK 3
def bubble_linked(head):
    head1 = head
    while True:
        head2=head
        if head1.next==None:
            break
        while True:
            if head2.next==None:
                break
            if head2.value>head2.next.value:
                temp=head2.next.value
                head2.next.value=head2.value
                head2.value=temp
            head2=head2.next
        head1=head1.next
    return head

##############################################################

# TASK 4
def selection_linked(head):
    head1 = head
    while True:
        head2=head1.next
        min=head1
        if head1.next==None:
            break
        while True:
            if min.value>head2.value:
                min=head2
            if head2.next==None:
                break
            head2=head2.next
        temp = min.value
        min.value = head1.value
        head1.value = temp
        head1=head1.next
    return head

##############################################################

# TASK 5
def insertion_linked(head):
    head1 = head.next
    while True:
        head2=head1
        if head1==None:
            break
        temp=head1.value
        while True:
            if head2.prev == None:
                break
            if head2.prev.value>temp:
                head2.value=head2.prev.value
            else:
                break
            head2=head2.prev
        head2.value = temp
        head1=head1.next
    return head

##############################################################


# TASK 6
def binary_recursive(array, item, start=0, end=0, count=0):
    if count==0:
        end=len(array)
    x = (end - start) / 2 - 1
    if x%1!=0:
        x+=0.5
    x=int(x)
    # print(start, end, x)
    # print(array)

    # V1.0
    # if x<0:
    #     return "{} was not found in the array".format(item)
    # elif array[x]==item:
    #     return "{} found in location {}".format(item,curr+x)
    # elif array[x]<item:
    #     return binary_recursive(array[x+1:],item, curr+x+1)
    # elif array[x]>item:
    #     # This won't work properly for all values, can't figure out the exact math, something is flawed, too tired
    #     return binary_recursive(array[:x],item, curr-x)

    # v2.0
    # changed approach to just keeping the array intact
    # plitting array created math that required furthur processing overload
    # Which :I really didn't want to deal with because that just makes it really inefficient.
    if x<0:
        return "{} was not found in the array".format(item)
    elif array[start+x]==item:
        return "{} found in location {}".format(item,start+x)
    elif array[start+x]<item:
        start+=x+1
    elif array[start+x]>item:
        end-=x+1
    return binary_recursive(array, item, start, end, 1)

##############################################################

# TASK 7
memoization101=[1, 1, 2, 3, 5, 8, 13, 21, 34]
# I'm assuming that 0 isn't a valid fibonacci value, so I'm starting from 1
def fibonacci(n,prev=0,curr=1):
    if prev==0 and curr==1:
        if n<=len(memoization101):
            return memoization101[n-1]
        elif n>len(memoization101):
            return fibonacci(n-len(memoization101),memoization101[-2],memoization101[-1])
    elif n!=0:
        memoization101.append(prev+curr)
        return fibonacci(n-1,curr,memoization101[-1])
    else:
        return curr

##############################################################

array1=[8,9,0,6,7,5,3,4,1,2]
array2=[0,1,2,3,4,5,6,7,8,9]
# reverse(linkedlist1)

##print(selection_recursive(array1))
##print(insertion_recursive(array1))
##linkedlist1=doubleLinked(array1)
##print(bubble_linked(linkedlist1))
##linkedlist1=doubleLinked(array1)
##print(selection_linked(linkedlist1))
##linkedlist1=doubleLinked(array1)
##print(insertion_linked(linkedlist1))
##print(binary_recursive(array2,9))
print(fibonacci(11))
print(memoization101)
