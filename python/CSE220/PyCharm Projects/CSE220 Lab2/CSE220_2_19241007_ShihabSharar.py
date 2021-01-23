import random


class Task1:
    def __init__(self,a:list):
        self.participants=a
        while len(self.participants)!=1:
            self.rotate()
            if self.randomNumber()==1:
                self.eliminate()
            self.printList()
        print("Congratulations to "+self.participants[0]+" for winning the game")

    def rotate(self):
        self.participants=self.participants[1:]+[self.participants[0]]

    def randomNumber(self):
        return random.randint(0,3)

    def eliminate(self):
        x=len(self.participants)
        x=int(x/2)
        self.participants=self.participants[:x]+self.participants[x+1:]

    def printList(self):
        for a in self.participants:
            print(a)
        #print(str(self.participants)[1:-1]+"\n")
        print()


class Node:
    def __init__(self,a=None,b=None,c=None):
        self.value=a
        self.next=b
        self.prev=c

    def __str__(self):
        #str(memoryview(b'self.next'))
        return (str(self.value)+" - "+hex(id(self.next)))

class LinkedList:
    def __init__(self,a=None):
        if a is None:
            self.head = Node()
        else:
            if type(a)==type(list()) and len(a)>0:
                self.head=Node(a[0])
                for x in range(1,len(a)):
                    self.insert(a[x])
            elif type(a) is type(Node()):
                self.head = a
            elif type(a) is type(self):
                self.head=a.head
            elif type(a)==type(list()) and len(a)==0:
                self.head=Node()

    def showList(self):
        if self.isEmpty():
            print("Empty list")
        else:
            n=self.head
            if n is self.head and n.next is None:
                print(n.value,end=" ")
            while True:
                print(n.value,end=" ")
                if n.next is not None:
                    n = n.next
                else:
                    break
        print()

    def isEmpty(self):
        if self.head.value is None:
            return True
        else:
            return False

    def clear(self):
        if not self.isEmpty():
            self.head.value=None
            self.head.next=None

    def insert(self,newElement,index=None):
        if index is None:
            n = self.head
            if not self.isEmpty():
                while True:
                    if n.next is not None:
                        n = n.next
                    else:
                        break
            n.next = Node(newElement, None)
        else:
            n = self.head
            pos = 0
            if not self.isEmpty():
                while True:
                    if n.next is not None:
                        n = n.next
                    else:
                        break
                    pos += 1
                if index == 0:
                    self.head = Node(newElement, self.head)
                elif index <= pos:
                    n = self.head
                    pos = 1
                    while pos != index:
                        n = n.next
                        pos += 1
                    n.next = Node(newElement, n.next)
                elif index > pos:
                    self.insert(newElement)


    def remove(self,index):
        if not self.isEmpty():
            n=self.head
            previous = None
            pos = 0
            while True:
                if index == pos or n.next == None:
                    break
                pos += 1
                previous = n
                n = n.next
            if index==0:
                self.head=self.head.next
            else:
                previous.next = n.next


    def find(self,x=None):
        n=self.head
        if x==None:
            x=""
            while not x.isnumeric():
                x=input("Enter number to be searched: ")
            x=int(x)
        status=False
        while n.next is not None:
            if n.value == x:
                status=True
                break
            n=n.next
        if n.value==x:
            status=True
        return status

    def reverse(self):
        listLen = 1
        n = self.head
        newNode = None
        header=None
        while n.next is not None:
            n = n.next
            listLen += 1
        for a in range(listLen):
            n = self.head
            for b in range(listLen - a - 1):
                n = n.next
            if header == None:
                newNode = Node(n.value)
                header=newNode
            else:
                newNode.next=Node(n.value)
                if newNode==header:
                    header.next = newNode.next
                newNode=newNode.next
        self.head=header

    def sort(self):
        listLen=1
        n=self.head
        while n.next is not None:
            n = n.next
            listLen+=1
        for a in range(listLen):
            prev = None
            curr = self.head
            nex = self.head.next
            while nex is not None:
                if curr.value>nex.value:
                    if prev is None:
                        self.head=nex
                        curr.next=nex.next
                        nex.next=curr
                    else:
                        prev.next = nex
                        curr.next = nex.next
                        nex.next = curr
                prev=curr
                curr=nex
                nex=nex.next

    def rotate(self,direction=None,count=1):
        if direction == None:
            direction = input("Enter a direction (left|right): ")
        for a in range(count):
            if direction == "left":
                temp = self.head.value
                self.remove(0)
                self.insert(temp)
            elif direction == "right":
                n = self.head
                while n.next != None:
                    n = n.next
                temp = n.value
                n=self.head
                pos=0
                while True:
                    if n.next==None:
                        break
                    n=n.next
                    pos+=1
                self.remove(pos)
                self.insert(temp, 0)

    def shift(self,direction,count=1):
        for a in range(count):
            self.rotate(direction, 1)
            if direction=="left":
                n = self.head
                pos = 0
                while True:
                    if n.next == None:
                        break
                    n = n.next
                    pos += 1
                self.remove(pos)
                self.insert("_",pos)
            elif direction=="right":
                self.remove(0)
                self.insert("_",0)

def task2(string):
    list1=[]
    for a in string:
        if a!=" ":
            list1.append(a)
    linkedList=LinkedList(list1)
    linkedList.showList()
    linkedList.reverse()
    linkedList.showList()
    linkedList.insert("P",0)
    linkedList.showList()
    linkedList.insert("A",2)
    linkedList.showList()
    linkedList.rotate("left",4)
    linkedList.showList()
    linkedList.remove(1)
    linkedList.showList()
    linkedList.insert("G")
    linkedList.showList()
    linkedList.rotate("right",3)
    linkedList.showList()
    linkedList.shift("right",2)
    linkedList.showList()
    linkedList.sort()
    linkedList.showList()


def printDuplicate(head):
    n=head
    if n.next==None:
        print("List length 1, too short for duplicates.")
        return None
    n = head
    pos = 0
    while True:
        if n.next == None:
            break
        n = n.next
        pos += 1
    n = head
    count1=0
    while True:
        count2 = 0
        status=False
        m=n.next
        while count1<pos and count2<pos-count1:
            print(n,m)
            if m.value==n.value:
                status=True
                break
            m=m.next
            count2+=1
        if n.next==None or status:
            break
        n = n.next
        count1 += 1
    if status:
        print(n.value)
    else:
        print("No duplicates found")


def remove_multiple_of_five(x):
    curr = x
    prev = None
    while True:
        if curr.value % 5 == 0:
            if prev != None:
                prev.next = curr.next
            else:
                x = curr.next
        else:
            prev = curr
        if curr.next == None:
            break
        curr = curr.next

    n = x
    try:
        if n is x and n.next is None:
            print(n.value, end=" ")
        while True:
            print(n.value, end=" ")
            if n.next is not None:
                n = n.next
            else:
                break
    except:
        print("null")


def task5(head1,head2):
    num1=""
    num2=""
    while head1.next!=None:
        num1+=str(head1.next.value)
        head1=head1.next
    while head2.next!=None:
        num2+=str(head2.next.value)
        head2=head2.next
    num1=int(num1)
    num2=int(num2)
    total=num1+num2
    total=str(total)
    totalList=Node()
    n=totalList
    for a in total:
        n.next=Node(a,None)
        n=n.next
    n=totalList
    while True:
        if n.value==None:
            print("x ->",end="")
        elif n.next==None:
            print(n.value)
            break
        else:
            print(n.value, end=" -> ")
        n=n.next

def task6(head,item):
    n=head
    while True:
        if n.next==head:
            break
        n=n.next
    n.next=Node(item,head)
    LinkedList(head).showList()

def insertBefore(head, elem, newElement):
    prev=head
    curr=head.next
    while True:
        if curr.value==elem:
            prev.next=Node(newElement,curr,prev) #assuming Node is designed as Node(value, next, prev)
            curr.prev=prev.next
        if curr.next==head:
            print("No matching element found")
            break
        prev=curr
        curr=curr.next

def tester():
    #Task1(["Player 0","Player 1","Player 2","Player 3","Player 4","Player 5","Player 6","Player 7","Player 8","Player 9"])
    task2("SHIHAB")
    #task3=LinkedList([5,4,15,2,3,4])
    #printDuplicate(task3.head)
    #task4=remove_multiple_of_five(LinkedList([10,20,30,40,50]).head)
    #task5(Node(None,LinkedList([4,5,3]).head),Node(None,LinkedList([9,5,2]).head))
    #list1=LinkedList([1,2,3,4,5]).head #here I don't have a circular list, but if you want you can put one yourself, code will generate an error unless a circular array is given
    #task6(list1,100)
    #task7=insertBefore(head,3,50)
    pass
z=tester()
