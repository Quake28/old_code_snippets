class Node:
    def __init__(self,name):
        self.name=str(name)
        self.next=[]
        self.titan=[]
    def addEdge(self,next,titan):
        self.next.append(next)
        self.titan.append(titan)
    def __repr__(self):
        return  str(self.name)


def djikstras(itemList,destination):
    queue = [[a,float("inf"),None,b] for b,a in enumerate(itemList)]
    dictx = {a[0]:a for a in queue}
    queue[0][1]=0
    pos=0
    print(queue,dictx)
        
    return queue


if __name__=="__main__":
    fileRead=open("input1.txt","r")
    for number in range(int(fileRead.readline())):
        x=fileRead.readline().rstrip()
        x=[int(a) for a in x.split()]
        nodeList=[Node(a+1) for a in range(x[0])]
        titanCount=0
        for b in range(x[1]):
            y=fileRead.readline().rstrip()
            y=[int(a) for a in y.split()]
            nodeList[y[0]].addEdge(y[1],y[2])
        graphHead=nodeList[0]
        destinationNode=nodeList[-1]
        resutls = djikstras(nodeList,destinationNode)
        pass