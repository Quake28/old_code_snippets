# source(s)-2 & destination (t)-4
# source(s)-1 & destination (t)-4
"""
4 4 3 2
1 2 4
1 3 20
2 3 4
3 4 4
1 4
2 4

"""

"""
12
8
"""

"""
5 6 5 3
1 2 4
1 3 4
1 4 20
2 4 4
3 4 1
4 5 4
1 5
2 5
3 5

"""

"""
9
8
5
"""


class Node:
    count = 1

    def __init__(self):
        self.identifier = Node.count
        Node.count += 1
        self.weight = []
        self.next = []

    def add(self, n, w):
        self.next.append(n)
        self.weight.append(w)
        # n.next.append(self)
        # n.weight.append(w)

    def __repr__(self):
        return str(self.identifier)


def djikstra(nodeList, s):
    queue = [[s], [0], [None]]
    b = 0
    while b < len(queue[0]):
        for a in range(len(queue[0][b].next)):
            if queue[0][b].next[a] not in queue[0]:
                queue[0].append(queue[0][b].next[a])
                queue[1].append(float("inf"))
                queue[2].append(queue[0][b])
        b += 1
    count = 0
    # print(queue)
    while True:
        for a in range(len(queue[0][count].next)):
            x = 0
            for x in range(1, len(queue[0])):
                if queue[0][x] == queue[0][count].next[a]:
                    break
            z = queue[0][count].weight[a] + queue[1][count]
            # print(z,queue[0][count])
            if z < queue[1][x]:
                queue[1][x] = z
        count += 1
        if len(queue[0]) == count:
            break
    for a in range(len(queue[0])):
        for b in range(len(queue[0]) - 1):
            if queue[1][b] > queue[1][b + 1]:
                for c in range(len(queue)):
                    temp = queue[c][b]
                    queue[c][b] = queue[c][b + 1]
                    queue[c][b + 1] = temp
    return queue


if __name__ == "__main__":
    input1 = input()
    input1 = input1.split()
    input1 = [int(a) for a in input1]
    nodeList = [Node() for a in range(input1[0])]
    for a in range(input1[1]):
        input2 = input()
        input2 = input2.split()
        input2 = [int(a) for a in input2]
        nodeList[input2[0] - 1].add(nodeList[input2[1] - 1], input2[2])
    queuex = djikstra(nodeList, nodeList[input1[2] - 1])
    # print(queuex)
    printer = []
    for a in range(input1[3]):
        input3 = input()
        input3 = input3.split()
        input3 = [int(a) for a in input3]
        queue = djikstra(nodeList, nodeList[input3[0] - 1])  # nodeList[input3[0] - 1]
        # print(queue)
        distance = 0
        for b in range(1, len(queue[0])):
            if queue[0][b] == queuex[0][0]:
                distance += queue[1][b]
                break
        for c in range(1, len(queuex[0])):
            if queuex[0][c] == nodeList[input3[1] - 1]:
                distance += queuex[1][c]
        # print(distance)
        printer.append(distance)
    for a in range(len(printer)):
        print("Case", a + 1, ":", printer[a])
