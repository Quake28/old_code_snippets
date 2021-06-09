class Node():
    def __init__(self,a):
        self.name = a
        self.next = [] 
        self.indegree = 0
    def add(self,a):
        self.next.append(a)
        a.indegree+=1
    def __repr__(self):
        return self.name

if __name__=="__main__":
    nodeList=[]
    nodeCount=int(input())
    edgeCount=int(input())
    for a in range(65,nodeCount+65):
        nodeList.append(Node(chr(a)))
    for b in range(edgeCount):
        inputString = input().split()
        nodeList[ord(inputString[0])-65].add(nodeList[ord(inputString[1])-65])
    #for c in nodeList:
    #    print(c,c.next)
    visited=0
    queue=[]
    for d in nodeList:
        if d.indegree==0:
            queue.append(d)
    while len(queue)!=0:
        visited+=1
        for e in queue[0].next:
            e.indegree-=1
            if e.indegree==0:
                queue.append(e)
        queue.pop(0)
    if len(nodeList)!=visited:
        print("Cyclic")
    else:
        print("Acyclic")

"""
5
6
A B
A C
A D
B E
D B
E D

5
6
A B
A C
A D
B D
B E
E D

"""