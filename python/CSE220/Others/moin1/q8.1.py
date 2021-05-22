# Question 8

class Node:
    count=1
    def __init__(self,a=None,b=None):
        if b==None:
            self.name=str(Node.count)
        else:
            self.name=b
        Node.count+=1
        if a==None:
            self.next=self
        else:
            self.next=a
    def __repr__(self):
        return self.name
if __name__=="__main__":
    x=int(input())
    head1=Node()
    tracker=head1
    for a in range(x-1):
        tracker.next=Node(head1)
        tracker=tracker.next
    
    y=input()
    head2=Node(None,y[0])
    tracker2=head2
    for a in y[1:]:
        tracker2.next=Node(head2,a)
        tracker2=tracker2.next
    
    tracker1=head1
    tracker2=head2
    prev=None
    while not(tracker1==tracker1.next and tracker1.next==prev):
        if tracker2.name=="2" or tracker2.name=="4":
            prev.next=tracker1.next
            tracker1=tracker1.next
        else:
            prev=tracker1
            tracker1=tracker1.next
        tracker2=tracker2.next
    print(tracker1)