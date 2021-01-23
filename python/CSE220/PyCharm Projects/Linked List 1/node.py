class Node:
    def __init__(self, a, b):
        self.value = a
        self.next = b

    def printNode(self):
        print(self.value, "-", self.next)
