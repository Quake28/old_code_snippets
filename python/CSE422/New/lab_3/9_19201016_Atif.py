import random
import math

def pruning(nodes,level):
    newNodeSet = []
    if level == 0:
        return nodes[0]
    for a in range(0,len(nodes),2):
        if level%2==1:
            if nodes[a]<nodes[a+1]:
                newNodeSet.append(nodes[a+1])
            else:
                newNodeSet.append(nodes[a])
        else:
            if nodes[a]>=nodes[a+1]:
                newNodeSet.append(nodes[a+1])
            else:
                newNodeSet.append(nodes[a])
    return pruning(newNodeSet,level-1)

# TASK 1
# id = input("Enter ID: ")
id = "19201016"
for a in range(len(id)):
    if id[a]=="0":
        id  = id[:a] + "8" + id[a+1:]
start = int(id[5])
winScore = int(id[-2:][::-1])
end = int(winScore*1.5)
terminalNodes = [random.randint(start,end) for randomNum in range(8)]
print("Generated 8 random points between the minimum and maximum point limits:",terminalNodes)
x = pruning(terminalNodes,int(math.log(len(terminalNodes),2)))
print("Total points to win:",winScore)
print("Achieved point by applying alpha-beta pruning =",x)
if x>winScore:
    print("Optimus Prime wins")
else:
    print("Megatron wins")

# TASK 2
print("After the shuffle:")
shuffleCount = int(id[3])
scores = []
for a in range(shuffleCount):
    scores.append(pruning([random.randint(start,end) for randomNum in range(8)],int(math.log(len(terminalNodes),2))))
print("List of all points values from each shuffle:",scores)
print("The maximum value of all shuffles:", max(scores))
winCount = 0
for b in scores:
    if b>winScore:
        winCount+=1
print("Won",winCount,"times out of",shuffleCount,"number of shuffles")