class Graph:
    def __init__(self, Nodes):
        self.nodes=Nodes 
        self.adj_list={}
        for node in self.nodes:
            self.adj_list[node]={}

    def edge(self, ver, edg):
        if edg == '0':
            return 0
        else:
            self.adj_list[ver][edg[0]]=edg[1]

def priorityQueueSort(prioQueue, dist, position, currLength):
    pos2=position-1
    swap=prioQueue[pos2]
    if pos2-1>0:
        while dist[prioQueue[pos2-1]][1]>currLength:
            #print("swapped",prioQueue[pos2],prioQueue[pos2-1])
            prioQueue[pos2]=prioQueue[pos2-1]
            #print("swapped",prioQueue[pos2],prioQueue[pos2-1])
            pos2-=1
        prioQueue[pos2]=swap
    return prioQueue

def dijkstra(graph,source, stop):
    prioQueue=[]
    currNode = graph.adj_list
    infinity= float('inf')
    dist = {}
    for node in currNode :
        prioQueue.append(node)
        dist[node]=[node,infinity,None]
    dist[source][1]=0
    priorityQueueSort(prioQueue, dist, source, 0)
    for pos in range(1,len(prioQueue)+1):
        node=prioQueue[pos-1]
        adj=currNode[node]
        for nextNode in adj:
            currLength=dist[node][1]+adj[nextNode]
            if currLength<dist[nextNode][1]:
                #print(dist)
                dist[nextNode][1]=currLength
                dist[nextNode][2]=node
                #print(dist)
                prioQueue=priorityQueueSort(prioQueue,dist,nextNode,currLength)
            #print(prioQueue)
        #print()
    return dist
def mainProcess():
    f1=open("input1.txt","r") 
    returnData=[]
    for a in range(int(f1.readline())):
        r1=f1.readline().split()
        r1=[int(b) for b in r1]
        nodes=[b for b in range(1,r1[0]+1)]
        edg1=[]
        graph=Graph(nodes)
        for b in range(r1[1]):
            r2=f1.readline().split()
            edg1.append([int(b) for b in r2])
        for c in range(r1[1]):
            graph.edge(edg1[c][0],edg1[c][1:])
        #print(graph.adj_list)
        returnData.append(dijkstra(graph, nodes[0], nodes[-1]))
    f1.close()
    return returnData

if __name__=="__main__":
    printData = mainProcess()
    #print(printData)
    f2=open("output1.txt","w")
    for a in range(len(printData)):
        lastKey=list(printData[a].keys())[-1]
        f2.write(str(printData[a][lastKey][1])+"\n")
    f2.close()
