class Node:
    count = 1
    def __init__(self):
        self.myname = Node.count
        Node.count += 1
        self.weight = []
        self.next = []
    def add(self, n, w):
        self.next.append(n)
        self.weight.append(w)
    def __repr__(self):
        return str(self.myname)
def shortest_path(nodes, start):
    nodeQueue = [[start], [0], [None]]
    j=0
    while j<len(nodeQueue[0]):
        for i in range(len(nodeQueue[0][j].next)):
            if nodeQueue[0][j].next[i] not in nodeQueue[0]:
                nodeQueue[0].append(nodeQueue[0][j].next[i])
                nodeQueue[1].append(float("inf"))
                nodeQueue[2].append(nodeQueue[0][j])
        j+=1
    count = 0
    while True:
        for i in range(len(nodeQueue[0][count].next)):
            x = 0
            for x in range(1,len(nodeQueue[0])):
                if nodeQueue[0][x] == nodeQueue[0][count].next[i]:
                    break
            z = nodeQueue[0][count].weight[i] + nodeQueue[1][count]
            if z < nodeQueue[1][x]:
                nodeQueue[1][x] = z
        count += 1
        if len(nodeQueue[0]) == count:
            break
    for i in range(len(nodeQueue[0])):
        for j in range(len(nodeQueue[0]) - 1):
            if nodeQueue[1][j] > nodeQueue[1][j + 1]:
                for k in range(len(nodeQueue)):
                    temp = nodeQueue[k][j]
                    nodeQueue[k][j] = nodeQueue[k][j + 1]
                    nodeQueue[k][j + 1] = temp
    return nodeQueue

parameters = input()
parameters = parameters.split()
parameters = [int(i) for i in parameters]
nodes = [Node() for i in range(parameters[0])]
for i in range(parameters[1]):
    flights = input()
    flights = flights.split()
    flights = [int(i) for i in flights]
    nodes[flights[0] - 1].add(nodes[flights[1] - 1], flights[2])
hotelQueue = shortest_path(nodes, nodes[parameters[2] - 1])
distanceList=[]
for i in range(parameters[3]):
    start_end = input()
    start_end = start_end.split()
    start_end = [int(i) for i in start_end]
    nodeQueue = shortest_path(nodes, nodes[start_end[0] - 1])
    distance = 0
    for j in range(1, len(nodeQueue[0])):
        if nodeQueue[0][j] == hotelQueue[0][0]:
            distance += nodeQueue[1][j]
            break
    for k in range(1, len(hotelQueue[0])):
        if hotelQueue[0][k] == nodes[start_end[1] - 1]:
            distance += hotelQueue[1][k]
    distanceList.append(distance)
for i in range(len(distanceList)):
    print("Case",i+1,":",distanceList[i])
