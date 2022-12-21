def Multiply_matrix(matrixA,matrixB):
    n=len(matrix_A)
    matrix_C = [[0 for a in range(n)] for b in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                matrix_C[i][j] += matrixA[i][k]*matrixB[k][j]
    return matrix_C


readFile=open("input4.txt","r")
n=int(readFile.readline())
matrix_A,matrix_B=[],[]
for count in range(n):
    matrix_A.append([int(a) for a in readFile.readline().split()])
readFile.readline()
for count in range(n):
    matrix_B.append([int(a) for a in readFile.readline().split()])
readFile.close()
resultMatrix=Multiply_matrix(matrix_A,matrix_B)
writeFile=open("output4.txt","w")
for a in resultMatrix:
    for b in a:
        writeFile.write(str(b)+" ")
    writeFile.write("\n")
writeFile.close()