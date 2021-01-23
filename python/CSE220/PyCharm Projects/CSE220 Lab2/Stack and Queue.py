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
        self.head=singleNode()
        if a==None:
            self.head.next=singleNode()
        elif type(a)==type(list()):
            self.head.next=singleNode()
            print(self.head,self.head.next)
            for i in range(len(a)):
                self.insert(a[i])
        elif type(a) is type(singleNode()):
            self.head.next = a
        elif type(a) is type(doubleNode()):
            self.head.next = a
            a.prev = self.head
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
        n = self.head.next
        print(n,n.next)
        if index==None:
            while True:
                if n.value==None:
                    n.value=key
                    break
                if n.value == None:
                    if type(self.head) == type(singleNode()):
                        n.next = singleNode(key,self.head)
                    elif type(self.head) == type(doubleNode()):
                        n.next = doubleNode(key,self.head,n)
                    break
                n=n.next

        elif not self.isEmpty():
            if type(self.head) == type(singleNode()):
                pos=0
                while True:
                    if n.next == None:
                        break
                    n=n.next
                    pos+=1
                n=self.head.next
                if index<=pos:
                    count=0
                    prev=self.head
                    while True:
                        if count==index:
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
                    if index == pos:
                        self.insert(key)
                    else:
                        count = 0
                        prev = self.head
                        while True:
                            if count == index:
                                prev.next = doubleNode(key, n, prev)
                                break
                            prev = n
                            n = n.next
                            count += 1

    def remove(self,key=None,index=None):
        if not self.isEmpty():
            n=self.head.next
            previous = self.head
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
                previous.next = n.next
            elif type(self.head) == type(doubleNode()):
                previous.next = n.next
                if n.next != None:
                    n.next.prev = previous

    def rotate(self,direction=None,turn=1):
        if direction==None:
            direction=input("Enter a direction (left|right): ")
        for a in range(turn):
            if direction=="left":
                temp=self.head.next.value
                self.remove(index=0)
                self.insert(temp)
            elif direction=="right":
                n=self.head.next
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
                n=self.head.next
                while n.next!=None:
                    n=n.next
                self.remove(key=n.value)
                self.insert(0,0)

    def clear(self):
        if type(self.head)==type(singleNode()):
            self.head.next=None
        if type(self.head)==type(doubleNode()):
            self.head.next=None

    def showList(self):
        if self.isEmpty():
            print("Empty List")
        else:
            n=self.head.next
            while True:
                print(n.value,end=" ")
                if n.next==None:
                    break
                n=n.next
            print()

    def pop(self):
        n=self.head.next
        p=self.head
        while n.value!=None:
            p=n
            n=n.next
        p.next=n.next

list1=[1,2,3,4,5,6]
list2=MyList(list1)
#z=MyList(list2.head)

z=MyList(list1)
'''
z.showList()

z.insert(7,3)
z.showList()
z.remove(index=0)
z.showList()
z.shift("left",2)
z.showList()
'''
'''
1 2 3 4 5 6 
1 2 3 7 4 5 6 
2 3 7 4 5 6 
7 4 5 6 0 0 
'''

#STACK
z.showList()
z.insert(12)
z.showList()
z.pop()
z.showList()