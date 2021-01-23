class Node():
    def __init__(self,value=None,prev=None,next=None):
        self.value=value
        self.prev=prev
        self.next=next
    def __str__(self):
        return str(self.value)+" - "+str(hex(id(self.prev)))+" - "+str(hex(id(self.next)))

class DoublyList():
    def __init__(self,a:type(list)):
        if len(a)!=0:
            self.head=Node()
            self.head.next=self.head
            self.head.prev=self.head
            n=self.head
            for i in a:
                self.insert(i)
        else:
            print("Empty List!")
    def showList(self):
        n=self.head.next
        while n!=self.head:
            print(n.value,end=" ")
            n=n.next
        print()
    def insert(self,newElement=None,index=None):
        n=self.head
        length=0
        while n.next!=self.head:
            n=n.next
            length+=1
            if n.value==newElement:
                print("The value "+newElement+" already exists in list")
                return None
        n=self.head
        if index==None or index==length:
            n.prev=Node(newElement,n.prev,n)
            n.prev.prev.next=n.prev
        elif index>length:
            print("Index \'"+index+"\' is out of range.")
        else:
            if length==0:
                print("List is empty, cannot add values.")
                return None
            count=0
            while count<=index:
                n=n.next
                count+=1
            n.prev = Node(newElement, n.prev, n)
            n.prev.prev.next = n.prev
    def showReversedList(self):
        n=self.head
        while n.prev!=self.head:
            n=n.prev
            print(n.value,end=(" "))
        print()
    def remove(self,index):
        n = self.head
        length = 0
        while n.next != self.head:
            n = n.next
            length += 1
        if length==0:
            print("List is empty.")
        elif index>=length:
            print("Index out of range.")
        else:
            count=0
            n=self.head
            p=n.prev
            while n.next!=self.head:
                p=n
                n=n.next
                if count==index:
                    p.next=n.next
                    n.next.prev=p
                    break
                count+=1
    def removeKey(self,deletekey):
        n = self.head
        length = 0
        while n.next != self.head:
            n = n.next
            length += 1
        if length!=0:
            n=self.head
            count=0
            while n.next!=self.head:
                n=n.next
                if n.value==deletekey:
                    self.remove(count)
                    return deletekey
                count+=1
            return "Key was not found"

#Here I've used a reverse print function to show the validity of the fact that my DHDLCL program is working as intended.
#This is proved by my program by cycling in the counter clockwise direction with x.prev

z=DoublyList([0,1,2,3,4,5,6,7,8,9])
z.showList()
z.insert(100)
z.showList()
z.showReversedList()
z.insert(200,2)
z.showList()
z.showReversedList()
z.remove(11)
z.showList()
z.showReversedList()
print(z.removeKey(9))
z.showList()
z.showReversedList()
