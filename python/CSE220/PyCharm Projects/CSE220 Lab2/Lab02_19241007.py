class Node:
    def __init__(self,a=None,b=None):
        self.value=a
        self.next=b

    def __str__(self):
        return (str(self.value)+" - "+str(memoryview(b'self.next')))

class MyList:
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
                print(n.value)
            while True:
                print(n.value)
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
            status = True
            if not self.isEmpty():
                while True:
                    if n.value == newElement:
                        status = False
                        break
                    if n.next is not None:
                        n = n.next
                    else:
                        break
            if status:
                n.next = Node(newElement, None)
        else:
            n = self.head
            pos = 0
            status = True
            if not self.isEmpty():
                while True:
                    if n.value == newElement:
                        status = False
                        break
                    if n.next is not None:
                        n = n.next
                    else:
                        break
                    pos+=1
                if index==0 and status:
                    self.head=Node(newElement,self.head)
                elif index<=pos and status:
                    n=self.head
                    pos=1
                    while pos!=index:
                        n = n.next
                        pos += 1
                    n.next = Node(newElement, n.next)
                elif index>pos and status:
                    self.insert(newElement)


    def remove(self,deletekey):
        n=self.head
        status=False
        if n.value==deletekey:
            returnValue = n.value
            self.head= n.next
            return returnValue
        if not self.isEmpty() and not status:
            while n.next is not None:
                if n.next.value == deletekey:
                    status = True
                    break
                n = n.next
        if status:
            returnValue=n.next.value
            n.next=n.next.next
            return returnValue

######TASK3######
    def subtask1(self):
        n = self.head
        newList = MyList()
        while True:
            if  n.value % 2 == 0 and  n.value != 0:
                newList.insert(n.value)
            if  n.next is not None:
                n =  n.next
            else:
                break
        newList.showList()

    def subtask2(self):
        n=self.head
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
        print(status)
        print()

    def subtask3(self):
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
        self.showList()
        print()

    def subtask4(self):
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
        self.showList()

    def subtask5(self):
        n=self.head
        total=0
        while True:
            total+=n.value
            if n.next is not None:
                n=n.next
            else:
                break
        print(total)
        print()

    def subtask6(self):
        direction=str(input("Enter direction of rotation (lef/right): "))
        count=int(input("Enter the number of rotations: "))
        if direction=="left":
            for a in range(count):
                curr=self.head
                while curr.next is not None:
                    curr=curr.next
                curr.next=self.head
                self.head=self.head.next
                curr.next.next=None
        elif direction=="right":
            for a in range(count):
                prev=None
                curr = self.head
                while curr.next is not None:
                    prev = curr
                    curr = curr.next
                prev.next = None
                curr.next=self.head
                self.head=curr
        self.showList()


class TestClass:
    def __init__(self):
        #uncomment line below to take manual inputs
        #linkedList1=MyList(self.takingInput())
        linkedList1 = MyList([0,1,1,1,1,2,2,2,2,2,3,4,5,6,7,8,9])
        print(linkedList1.isEmpty(),"\n")
        linkedList1.showList()
        linkedList1.insert(1000,8)
        linkedList1.showList()

        linkedList1.subtask1()
        linkedList1.subtask2()
        linkedList1.subtask3()
        linkedList1.subtask4()
        linkedList1.subtask5()
        linkedList1.subtask6()

        linkedList1.remove(1000)
        linkedList1.showList()
        linkedList1.clear()
        print(linkedList1.isEmpty(),"\n")
        linkedList1.showList()

    def takingInput(self):
        print("To enter a list of numbers, press enter after each number.\nTo stop taking any more inputs press enter with a blank input.\n")
        x = 0
        list1 = []
        while x != "":
            x = input("Enter number: ")
            if x.isnumeric():
                list1.append(int(x))
            elif x != "":
                print("This is not an integer, please re-enter your value.")
        return list1


z=TestClass()