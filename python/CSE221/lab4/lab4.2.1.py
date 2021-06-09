# no. of nodes
# no. of connecting routes

# source-Mouchak
# destination-DU
# colour-yellow

"""
12
16
0,1,5
0,2,2
0,3,10
1,4,20
1,5,10
2,6,3
2,7,12
3,8,5
3,9,8
4,11,5
5,10,6
7,8,2
8,10,10
8,11,12
9,11,2
11,10,2
0
10
2,5,6,8

"""

"""
Mouchak->Shahbagh->TSC->BUET->Dhaka University
Path cost: 22 
"""

"""
M,0 Mouchak
Pn ,1 Panthapath
R ,2 Rampura
Sh ,3 Shahahbagh
Dh ,4 Dhanmondi
Lm ,5 Lalmatia
B ,6 Badda
H ,7 Hatirjheel
N ,8 Nilkhet
TSC,9 TSC
DU, 10 Dhaka University
BUET ,11 BUET

["Mouchak","Panthapath","Rampura","Shahahbagh","Dhanmondi","Lalmatia","Badda","Hatirjheel","Nilkhet","TSC","Dhaka University","BUET"]
"""

class Node:
    count = 0

    def __init__(self):
        self.identifier = Node.count
        Node.count += 1
        self.weight = []
        self.next = []

    def add(self, n, w):
        self.next.append(n)
        self.weight.append(w)
        #n.next.append(self)
        #n.weight.append(w)

    def __repr__(self):
        return str(self.identifier)


def dijkstra(nodeList, s, construction):
    queue = [[s], [0], [None]]
    for a in nodeList[1:]:
        queue[0].append(a)
        queue[1].append(float("inf"))
        #print(queue[0][b])
        queue[2].append(None)
    count = 0
    #print(queue)
    while True:
        for a in range(len(queue[0][count].next)):
            #print(queue[0][count],queue[0][count].next[a])]
            x = int(str(queue[0][count].next[a]))
            if x in construction:
                continue
            z = float("inf")
            if queue[1][count]!=float("inf"):
                z = queue[1][count] + queue[0][count].weight[a]
            #print(z,queue[0][count])
            if z < queue[1][x]:
                queue[1][x] = z
                queue[2][x] = queue[0][count]
                #break
        count += 1
        if len(queue[0]) == count:
            break
    #print(queue)
    for a in range(len(queue[0])):
        for b in range(len(queue[0]) - 1):
            if queue[1][b] > queue[1][b + 1]:
                for c in range(len(queue)):
                    temp = queue[c][b]
                    queue[c][b] = queue[c][b + 1]
                    queue[c][b + 1] = temp
    return queue


if __name__ == "__main__":
    names=["Mouchak","Panthapath","Rampura","Shahahbagh","Dhanmondi","Lalmatia","Badda","Hatirjheel","Nilkhet","TSC","Dhaka University","BUET"]
    
    # INPUTS - START
    input1 = int(input())
    nodeList = [Node() for a in range(input1)]
    input2 = int(input())
    # FORM EDGES AND PLACE WEIGHTS
    for a in range(input2):
        input3 = input()
        input3 = input3.split(",")
        input3 = [int(a) for a in input3]
        nodeList[input3[0]].add(nodeList[input3[1]], input3[2])
        
    input4 = int(input())
    input5 = int(input())
    input6 = input()
    input6 = input6.split(",")
    input6 = [int(a) for a in input6]

    #INPUTS - END
    for a in nodeList:
        for b in range(len(a.weight)):
            for c in range(len(a.weight)-1):
                if a.weight[c]>a.weight[c+1]:
                    temp1,temp2=a.next[c+1],a.weight[c+1]
                    a.next[c+1],a.weight[c+1]=a.next[c],a.weight[c]
                    a.next[c],a.weight[c]=temp1,temp2
    queue = dijkstra(nodeList, nodeList[input4],input6)
    print()
    #print(queue)
    distance = 0
    path=[input5]
    x=0
    #print(names[input5])
    for b in range(1, len(queue[0])):
        if queue[0][b] == nodeList[input5]:
            distance = queue[1][b]
            x=b
            break
    #print(queue)
    while True:
        #print(queue[0][x],queue[1][x],queue[2][x])
        path.append(queue[2][x])
        for a in range(len(queue[0])):
            #print(queue[0][a],queue[2][x])
            if queue[0][a] == queue[2][x]:
                x=a
                break
        if queue[0][x]==nodeList[input4]:
            break
    path=path[::-1]
    print(names[int(str(path[0]))], end="")
    for a in path[1:]:
        print("->"+names[int(str(a))],end="")
    print()
    print("Path cost:",distance)
