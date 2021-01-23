###### QUESTION 1 #######

def findEverywhere(cir,start,size):
    count=0
    status=True
    temp1 = start
    temp2 = start + 1
    finder1=0
    finder2=0
    while count<size-1 and status:
        if temp1>=len(cir):
            temp1-=len(cir)
        if temp2>=len(cir):
            temp2-=len(cir)
        curr=cir[temp1]
        next=cir[temp2]
        temp1+=1
        temp2+=1
        count+=1
        if count==1:
            finder1=curr
            finder2=next
        if finder1!=curr and finder1!=next and finder2!=curr and finder2!=next:
            status=False
    if status:
        print("true") #only for capital 'T' and small 't'
    else:
        print("false") #only for capital 'F' and small 'f'

findEverywhere([0,0,1, 2, 1, 3],2,4)
findEverywhere([2,0,1,2,2,3],2,3)
findEverywhere([1,2,0,0,1,3,4],4,5)

########Question 2#########

class Node:
    def __init__(self, v, n):
        self.val= v
        self.next = n
class LinkedList:
    def __init__(self,list1):
        self.head=Node(None, None)
        n=self.head
        for a in list1:
            n.next=Node(a,None)
            n=n.next
def properSubset(head1, head2):
    status1=True
    n1=head1.next
    while True:
        status2 = False
        n2 = head2.next
        while True:
            if n1.val==n2.val:
                status2=True
                break
            if n2.next==None:
                break
            n2=n2.next
        if not status2:
            status1 = False
            break
        if n1.next==None:
            break
        n1=n1.next
    return status1

head1=LinkedList([1,2,3]).head
head2=LinkedList([1,2,3,4]).head
print(properSubset(head1,head2))
head1=LinkedList([1,2,3]).head
head2=LinkedList([1,5,3]).head
print(properSubset(head1,head2))
head1=LinkedList([1,2,3,4]).head
head2=LinkedList([1,2,3,6,4]).head
print(properSubset(head1,head2))