class Node:
    def __init__(self, value, next=None):
        self.value=value
        self.next=next

def addition(linked):
    if linked==None:
        return 0
    else:
        return linked.value + addition(linked.next)

def reversed(linked):
    if linked==None:
        return ""
    else:
        return reversed(linked.next) + "\n" + str(linked.value)

z=Node(10,Node(20,Node(30,Node(40))))

#print(addition(z))

print(reversed(z))
