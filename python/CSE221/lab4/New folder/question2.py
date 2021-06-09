class Node:
    count = 0
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
def shortest_path(nodes, start, exclusions):
    nodeQueue = [[start], [0], [None]]
    for i in nodes[1:]:
        nodeQueue[0].append(i)
        nodeQueue[1].append(float("inf"))
        nodeQueue[2].append(None)
    count = 0
    while True:
        for i in range(len(nodeQueue[0][count].next)):
            x = int(str(nodeQueue[0][count].next[i]))
            if x in exclusions:
                continue
            z = float("inf")
            if nodeQueue[1][count]!=float("inf"):
                z = nodeQueue[1][count] + nodeQueue[0][count].weight[i]
            if z < nodeQueue[1][x]:
                nodeQueue[1][x] = z
                nodeQueue[2][x] = nodeQueue[0][count] 
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

location=["Mouchak","Panthapath","Rampura","Shahahbagh","Dhanmondi","Lalmatia","Badda","Hatirjheel","Nilkhet","TSC","Dhaka University","BUET"]
nodeCount = int(input())
nodes = [Node() for i in range(nodeCount)]
edgeCount = int(input())
for i in range(edgeCount):
    edges = input()
    edges = edges.split(",")
    edges = [int(i) for i in edges]
    nodes[edges[0]].add(nodes[edges[1]], edges[2])
startNode = int(input())
endNode = int(input())
exclusions = input()
exclusions = exclusions.split(",")
exclusions = [int(i) for i in exclusions]
nodeQueue = shortest_path(nodes, nodes[startNode],exclusions)
print()
distance = 0
path=[endNode] 
x=0
for j in range(1, len(nodeQueue[0])):
    if nodeQueue[0][j] == nodes[endNode]:
        distance = nodeQueue[1][j]
        x=j
        break
while True:
    path.append(nodeQueue[2][x])
    for i in range(len(nodeQueue[0])):
        if nodeQueue[0][i] == nodeQueue[2][x]:
            x=i
            break
    if nodeQueue[0][x]==nodes[startNode]:
        break
path=path[::-1]
print(location[int(str(path[0]))], end="")
for i in path[1:]:
    print("->"+location[int(str(i))],end="")
print()
print("Path cost:",distance)
