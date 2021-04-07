# n - number of different fixed positions (including Nora’s one)
# m - number of connections
# position 0 is connected with position 1
# ’x’-Lina’s position
# ‘k’- number of participants
# position of k1 participant
# position of k2 participant
# position of k3 participant
# position of k4 participant
# position of k5 participant
"""
10
14
0 1
0 2
0 3
1 3
1 4
2 3
3 5
4 7
4 8
5 6
6 7
6 9
7 8
8 9
9
5
0
1
3
5
7

"""
# minimum number of moves the winner(k5) needed to go to ‘x’
"""
2
"""


class Node:
    count = 0

    def __init__(self):
        self.identifier = Node.count
        Node.count += 1
        self.adj = []

    def add(self, next):
        self.adj.append(next)

    def __repr__(self):
        return str(self.identifier)


def bfs(node, search, k, count=1):
    level = node.adj
    while search not in level:
        # print(level)
        old_level = level[:]
        for a in range(len(level)):
            for b in level[0].adj:
                if b not in old_level:
                    temp = [b]
                    level = level[:] + temp
            level = level[1:]
        count += 1
        for b in k:
            if b in level:
                count = 1
    return count


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
    search = nodeList[int(input())]
    k = []
    d = int(input())
    for d1 in range(d):
        k.append(nodeList[int(input())])
    """
    for a2 in nodeList:
        print(a2,a2.adj)
    print()
    """
    print(bfs(k[0], search, k))
