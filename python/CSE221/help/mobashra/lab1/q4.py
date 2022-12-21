def Multiply_matrix(matA,matB):
    n=len(matA)
    c=[[0 for a in range(n)] for b in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += matA[i][k]*matB[k][j]
    return c

inputFile=open("input4.txt","r")
dataArr = [[],[]]
fileData = inputFile.read().split("\n")
n=int(fileData[0])
count=0
start=1
for a in range(2):
    for b in range(start,start+n):
        y = fileData[b].split()
        x=[int(x) for x in y]
        dataArr[a].append(x)
    start+=n+1
#print(dataArr)

result = Multiply_matrix(dataArr[0],dataArr[1])
#print(result)

outputFile = open("output4.txt","w")

for a in range(len(result)):
    for b in range(len(result)):
        outputFile.write(" {}".format(result[a][b]))
    outputFile.write("\n")

outputFile.close()