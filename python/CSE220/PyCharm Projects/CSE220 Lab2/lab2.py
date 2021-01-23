class Node:
    def __init__(self, a=None, b=None):
        self.value = a
        self.next = b
class MyList:
    def __init__(self, a=None):
        if a is None:
            self.head = Node()
        else:
            if type(a) == type(list()) and len(a) > 0:
                self.head = Node(a[0])
                for m in range(1, len(a)):
                    self.insert(a[m])
            elif type(a) is type(Node()):
                self.head = a
            elif type(a) is type(self):
                self.head = a.head
            elif type(a) == type(list()) and len(a) == 0:
                self.head = Node()
    def showList(self):
        if self.isEmpty():
            print("Empty list")
        else:
            nodePointer = self.head
            if nodePointer is self.head and  nodePointer.next is None:
                print( nodePointer.value)
            while True:
                print( nodePointer.value)
                if  nodePointer.next is not None:
                    nodePointer =  nodePointer.next
                else:
                    break
    def isEmpty(self):
        if self.head.value is None:
            return True
        else:
            return False
    def clear(self):
        if not self.isEmpty():
            self.head.value = None
            self.head.next = None
    def insert(self, newElement, index=None):
        if index is None:
            nodePointer = self.head
            status = True
            if not self.isEmpty():
                while True:
                    if  nodePointer.value == newElement:
                        status = False
                        break
                    if  nodePointer.next is not None:
                        nodePointer =  nodePointer.next
                    else:
                        break
            if status:
                 nodePointer.next = Node(newElement, None)
        else:
            nodePointer = self.head
            pos = 0
            status = True
            if not self.isEmpty():
                while True:
                    if  nodePointer.value == newElement:
                        status = False
                        break
                    if  nodePointer.next is not None:
                        nodePointer =  nodePointer.next
                    else:
                        break
                    pos += 1
                if index == 0 and status:
                    self.head = Node(newElement, self.head)
                elif index <= pos and status:
                    nodePointer = self.head
                    pos = 1
                    while pos != index:
                        nodePointer =  nodePointer.next
                        pos += 1
                    nodePointer.next = Node(newElement,  nodePointer.next)
                elif index > pos and status:
                    self.insert(newElement)
    def remove(self, deletekey):
        nodePointer = self.head
        status = False
        if  nodePointer.value == deletekey:
            returnValue =  nodePointer.value
            self.head =  nodePointer.next
            return returnValue
        if not self.isEmpty() and not status:
            while  nodePointer.next is not None:
                if  nodePointer.next.value == deletekey:
                    status = True
                    break
                nodePointer =  nodePointer.next
        if status:
            returnValue =  nodePointer.next.value
            nodePointer.next =  nodePointer.next.next
            return returnValue
    ######TASK3######
    def task3_1(self):
        nodePointer = self.head
        evenNum = MyList()
        while True:
            if  nodePointer.value % 2 == 0 and  nodePointer.value != 0:
                evenNum.insert(nodePointer.value)
            if  nodePointer.next is not None:
                nodePointer =  nodePointer.next
            else:
                break
        evenNum.showList()

    def task3_2(self):
        nodePointer = self.head
        m = ""
        while not m.isnumeric():
            m = input("Enter number for searching: ")
        m = int(m)
        status = False
        while  nodePointer.next is not None:
            if  nodePointer.value == m:
                status = True
                break
            nodePointer =  nodePointer.next
        if  nodePointer.value == m:
            status = True
        print(status)
    def task3_3(self):
        listLen = 1
        nodePointer = self.head
        newNode = None
        header = None
        while  nodePointer.next is not None:
            nodePointer =  nodePointer.next
            listLen += 1
        for a in range(listLen):
            nodePointer = self.head
            for b in range(listLen - a - 1):
                nodePointer =  nodePointer.next
            if header == None:
                newNode = Node( nodePointer.value)
                header = newNode
            else:
                newNode.next = Node( nodePointer.value)
                if newNode == header:
                    header.next = newNode.next
                newNode = newNode.next
        self.head = header
        self.showList()
    def task3_4(self):
        listLen = 1
        nodePointer = self.head
        while  nodePointer.next is not None:
            nodePointer =  nodePointer.next
            listLen += 1
        for a in range(listLen):
            previous = None
            current = self.head
            nextNode = self.head.next
            while nextNode is not None:
                if current.value > nextNode.value:
                    if previous is None:
                        self.head = nextNode
                        current.next = nextNode.next
                        nextNode.next = current
                    else:
                        previous.next = nextNode
                        current.next = nextNode.next
                        nextNode.next = current
                previous = current
                current = nextNode
                nextNode = nextNode.next
        self.showList()
    def task3_5(self):
        nodePointer = self.head
        total = 0
        while True:
            total +=  nodePointer.value
            if  nodePointer.next is not None:
                nodePointer =  nodePointer.next
            else:
                break
        print(total)
    def task3_6(self):
        direction = str(input("Enter direction of rotation (left/right): "))
        counter = int(input("Enter the number of rotations: "))
        if direction == "left":
            for a in range(counter):
                temp=self.head.value
                self.remove(temp)
                self.insert(temp)
        elif direction == "right":
            for a in range(counter):
                current=self.head
                while True:
                    if current.next==None:
                        break
                    current=current.next
                temp=current.value
                self.remove(temp)
                self.insert(temp)
        self.showList()
class TestClass:
    def __init__(self):
        #myList=MyList(self.inputCatcher())
        myList = MyList([123, 4123, 4, 235, 123, 512, 35, 123, 5, 234, 6523, 45, 123, 5412, 34, 1234])
        print(myList.isEmpty())
        myList.insert(102, 10)
        myList.task3_1()
        myList.task3_2()
        myList.task3_3()
        myList.task3_4()
        myList.task3_5()
        myList.task3_6()
        myList.remove(45)
        myList.clear()
        print(myList.isEmpty(), "\n")
        myList.showList()
    def inputCatcher(self):
        print("To enter a list of numbers, press enter after each number.\nTo stop taking any more inputs press enter with a blank input.\n")
        a = 0
        list1 = []
        while a != "":
            a = input("Enter number: ")
            if a.isnumeric():
                list1.append(int(a))
            elif a != "":
                print("This is not an integer, please re-enter your value.")
        return list1
testClass = TestClass()
