def BFS (visited, graph, node, endPoint):
    bfsList=[]
    queue =[]
    visited[node-1]=1
    queue.append(node)
    while len(queue)!=0:
        m=queue.pop(0)
        bfsList.append(m)
        if m==endPoint:
            break
        for neighbour in graph[m-1].next:
            if visited[neighbour-1] == 0:
                visited[neighbour-1] = 1
                queue.append(neighbour)
    return bfsList
import task1
nodeList=task1.nodeList[1:]
visited =[0 for a in range(len(nodeList))]

nodesVisited = BFS(visited,nodeList,1,12)
for a in nodesVisited:
    print(a,end=" ")
print()
if nodesVisited[-1]!=12:
    print("End point not found")