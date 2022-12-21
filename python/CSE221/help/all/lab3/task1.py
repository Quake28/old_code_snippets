class Node:
    count=1
    def __init__(self):
        self.name=Node.count
        Node.count+=1
        self.next=[]

fileR=open("input1.txt","r")
nodeList=[None]
for a in range(int(fileR.readline())):
    nodeList.append(Node())
for b in range(int(fileR.readline())):
    edge=[int(a) for a in fileR.readline().split()]
    nodeList[edge[0]].next.append(edge[1])

if __name__=="__main__":
    for c in nodeList[1:]:
        print(c.name," --> ", c.next)