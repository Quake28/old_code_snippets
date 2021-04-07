# n - number of different fixed positions (including Nora’s one)
# m - number of connections
# position 0 is connected with position 6
"""
7
8
0 6
1 2
1 5
2 0
2 5
3 4
4 2
3 1

"""
#suitable first position for Nora
"""
3
"""

class Node:
    count = 0

    def __init__(self):
        self.identifier = Node.count
        Node.count += 1
        self.next = []
        self.prev = []

    def add(self, next):
        self.next.append(next)
        next.prev.append(self)

    def __repr__(self):
        return str(self.identifier)

def dfs(nodeList):
    for a in nodeList:
        if len(a.prev)!=0:
            return dfs(a.prev)
        return a


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    nodeList = []
    for a1 in range(a):
        nodeList.append(Node())
    for b1 in range(b):
        c = input()
        c = c.split()
        nodeList[int(c[0])].add(nodeList[int(c[1])])
    """
    for a2 in nodeList:
        print(a2,a2.adj)
    print()
    """
    print(dfs(nodeList))
