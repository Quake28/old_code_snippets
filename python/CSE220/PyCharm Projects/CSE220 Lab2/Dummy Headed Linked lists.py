class singleNode:
    def __init__(self,a=None,b=None):
        self.value = a
        self.next = b
    def __str__(self):
        return (str(self.value)+" - "+str(memoryview(b'self.next')))

class doubleNode:
    def __init__(self,a=None,b=None,c=None):
        self.value = a
        self.next = b
        self.prev = c
    def __str__(self):
        return (str(memoryview(b'self.prev'))+" - "+str(self.value)+" - "+str(memoryview(b'self.next')))

class MyList:
    def __init__(self,a=None):
        self.head=doubleNode()
        if a==None:
            self.head.next=doubleNode()
        elif type(a)==type(list()):
            self.head.next=doubleNode()
            for i in range(len(a)):
                self.insert(a[i])
        elif type(a) is type(singleNode()) or type(a) is type(doubleNode()):
            self.head = a
        elif type(a) is type(self):
            self.head = a.head

    def isEmpty(self):
        if self.head.next==None:
            return True
        if self.head.next.value==None:
            return True
        else:
            return False

    def insert(self,key,index=None):
        n = self.head
        if index==None:
            while True:
                n=n.next
                if n.value==None:
                    n.value=key
                    break
                elif n.next == None:
                    if type(self.head) == type(singleNode()):
                        n.next = singleNode(key)
                    elif type(self.head) == type(doubleNode()):
                        n.next = doubleNode(key,None,n)
                    break

        elif not self.isEmpty():
            n=n.next
            pos=0
            while True:
                if n.next == None:
                    break
                n=n.next
                pos+=1
            n=self.head.next
            if index<=pos:
                if index==0:
                    if type(self.head) == type(singleNode()):
                        self.head=singleNode(key,self.head)
                else:
                    count=0
                    prev=self.head
                    while True:
                        if count==index:
                            if type(self.head) == type(singleNode()):
                                prev.next=singleNode(key,n)
                            break
                        prev=n
                        n=n.next
                        count += 1
            elif index + 1 == pos:
                self.insert(key)
            elif type(self.head) == type(doubleNode()):
                pos = 0
                while True:
                    if n.next == None:
                        break
                    n = n.next
                    pos += 1
                n=self.head.next
                if index <= pos:
                    if index == 0:
                        self.head.next = doubleNode(key, self.head)
                    elif index == pos:
                        self.insert(key)
                    else:
                        count = 0
                        prev = None
                        while True:
                            if count == index:
                                prev.next = doubleNode(key, n, prev)
                                break
                            prev = n
                            n = n.next
                            count += 1

    def remove(self,key=None,index=None):
        if not self.isEmpty():
            n=self.head
            previous = None
            if key!=None:
                while True:
                    if n.value==key or n.next==None:
                        break
                    previous=n
                    n = n.next
            if index!=None:
                pos = 0
                while True:
                    if index == pos or n.next == None:
                        break
                    pos += 1
                    previous = n
                    n = n.next
            if type(self.head) == type(singleNode()):
                if index==0:
                    self.head=self.head.next
                else:
                    previous.next = n.next
            elif type(self.head) == type(doubleNode()):
                if index == 0:
                    self.head = self.head.next
                else:
                    previous.next = n.next
                    if n.next != None:
                        n.next.prev = previous

    def rotate(self,direction=None,turn=1):
        if direction==None:
            direction=input("Enter a direction (left|right): ")
        for a in range(turn):
            if direction=="left":
                temp=self.head.value
                self.remove(index=0)
                self.insert(temp)
            elif direction=="right":
                n=self.head
                while n.next!=None:
                    n=n.next
                temp=n.value
                self.remove(key=temp)
                self.insert(temp,0)

    def shift(self,direction,turn=1):
        if direction==None:
            direction=input("Enter a direction (left|right): ")
        for a in range(turn):
            if direction=="left":
                self.remove(index=0)
                self.insert(0)
            elif direction=="right":
                n=self.head
                while n.next!=None:
                    n=n.next
                self.remove(key=n.value)
                self.insert(0,0)

    def clear(self):
        if type(self.head)==type(singleNode()):
            self.head=singleNode()
        if type(self.head)==type(doubleNode()):
            self.head=doubleNode()

    def showList(self):
        if self.isEmpty():
            print("Empty List")
        else:
            n=self.head
            while True:
                if n.next==None:
                    break
                n = n.next
                print(n.value,end=" ")
            print()

# list1=[1,2,3,4,5,6]
# list2=MyList(list1)
# z=MyList(list2.head)
# z.showList()
#
# z.insert(7,3)
# z.showList()
# z.remove(index=0)
# z.showList()
# z.shift("left",2)
# z.showList()
#
# z.insert(100,0)
# z.showList()
