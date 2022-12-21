def DFS(graph, node, endpoint, visited, bfsList=[]):
    visited[node-1]=1
    bfsList.append(node)
    if node==endpoint:
        return bfsList,visited
    for a in graph[node-1].next:
        if visited[a-1]==0:
            bfsList,visited=DFS(graph,a,endpoint,visited,bfsList)
            if bfsList[-1]==12:
                break
    return bfsList,visited

import task1
nodeList=task1.nodeList[1:]
visited =[0 for a in range(len(nodeList))]

nodesVisited = DFS(nodeList, 1, 12, visited)[0]
print(nodesVisited)
for a in nodesVisited:
    print(a,end=" ")
print()
if nodesVisited[-1]!=12:
    print("End point not found")