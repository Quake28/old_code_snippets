import node as Node

class LinkedList:
    def __init__(self,a):
        self.head=None
        tail=None
        for x in a:
            n=Node.Node(x,None)
            if self.head is None:
                self.head=n
                tail=n
            else:
                tail.next=n
                tail=n

    def printList(self):
        n=self.head
        while n is not None:
            n.printNode()
            n=n.next