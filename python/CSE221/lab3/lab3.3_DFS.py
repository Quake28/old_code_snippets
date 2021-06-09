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


def dfs(node, search, k, count=0):
    min_dist = 9999
    if node == search:
        return count
    if node in k:
        count = 0
    distance = []
    for a in node.adj:
        # print(node,node.adj)
        result = dfs(a, search, k, count + 1)
        # print(history)
        if result != None:
            distance.append(result)
        # print(distance)
    for b in distance:
        if b < min_dist:
            min_dist = b
    return min_dist


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
    print(dfs(k[0], search, k))
