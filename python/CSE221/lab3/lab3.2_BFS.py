# number of different fixed positions (including Nora’s one)
# number of connections
# position 0 is connected with position 1
# ’x’-Lina’s position
# ‘p’-Nora’s position
# ‘q’-Lara’s position
"""
9
12
0 1
0 2
0 3
1 3
1 4
2 3
3 5
4 8
4 7
5 6
6 7
7 8
7
5
3

"""
# winner, since Nora can go to ‘x’ with 2 moves and Lara can go with 3 moves
"""
Nora
"""


class Node:
    count = 0

    def __init__(self):
        self.identifier = Node.count
        Node.count += 1
        self.adj = []

    def add(self, next):
        self.adj.append(next)
        next.adj.append(self)

    def __repr__(self):
        return str(self.identifier)


def bfs(node, search, count=1):
    level = node.adj
    while search not in level:
        # print(level)
        for a in range(len(level)):
            level = level[1:] + level[0].adj
        count += 1
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
    nora = nodeList[int(input())]
    lara = nodeList[int(input())]
    """
    for a2 in nodeList:
        print(a2,a2.adj)
    print()
    """
    nora_dist = bfs(nora, search)
    lara_dist = bfs(lara, search)
    # print(nora_dist,lara_dist)
    if nora_dist > lara_dist:
        print("Lara")
    elif nora_dist < lara_dist:
        print("Nora")  # ,nora_dist,lara_dist)
    else:
        print("Both")
