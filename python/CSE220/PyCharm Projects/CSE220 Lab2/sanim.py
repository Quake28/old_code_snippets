class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


# Dummy headed circular linked list
class CircularLinkedList:
    # Constructor
    def __init__(self):
        self.head=Node()
        self.temp=self.head

    # Function to insert a single item
    def insert(self, item):
        self.temp.next = Node(item,self.head)
        self.temp=self.temp.next

    # Function to insert multiple Items
    def multipleInsert(self, size):
        print("Enter the Items please: ")
        for i in range(size):
            item = (input("Enter "+str(i+1)+" : "))
            self.insert(item)
            # Function to show the Circular Linked List

    def showList(self):
        n = self.head.next
        while True:
            print(n.value,end=" -> ")
            if n.next==self.head:
                break
            n = n.next


class Tester:
    MyList = CircularLinkedList()
    MyList.multipleInsert(7)
    MyList.showList()


    '''
        self.temp = Node()
        self.head = Node(None, self.temp)
        self.temp.next = self.head
    '''