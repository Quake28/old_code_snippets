class Node():
    def init(self,data=None,prev=None,next_node=None):
        self.data=data
        self.prev=prev
        self.next_node=next_node
class DoublyList():
    def init(self,x:type(list)):
        if len(x)!=0:
            self.head=Node()
            self.head.next=self.head
            self.head.prev=self.head
            n=self.head
            for i in x:
                self.insert(i)
        else:
            print("Empty List!")