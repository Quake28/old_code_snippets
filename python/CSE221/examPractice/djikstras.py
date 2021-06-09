class Node:
    def __init__(self, a):
        self.name = a
        self.next = []
        self.weights = []

    def addedges(self, b, c):
        self.next.append(b)
        self.weights.append(c)

def djikstra():
    pass

if __name__ == "__main__":
    strInput= input().split()
    nodeCount = int(strInput[0])
    edgeCount = int(strInput[1])
    #hotel = NodeList[int(strInput[2])]
    attempts = int(strInput[3])
    nodeList = [Node(chr(a)) for a in range(nodeCount)]
    for a in range(edgeCount):
        temp = input().split()
        nodeList[int(temp[0])].add(nodeList(int(temp[1])), int(temp[2]))
    for b in range()
    
    priorityQueue=djistra(nodeList,)
    
"""
3
4 4 2
1 2 4
1 3 20
2 3 4
3 4 4
1 4
2 4


12
8

5
5 6 3
1 2 4
1 3 4
1 4 20
2 4 4
3 4 1
4 5 4
1 5
2 5
3 5


9
8
5
"""