def first_queen(list1):
    for a in range(len(list1)):
        for b in range(len(list1[a])):
            if list1[a][b]==1:
                return [a,b]
def queens(list1):
    firstQueenPos=first_queen(list1)
    if firstQueenPos[0]>firstQueenPos[1]:
        x=firstQueenPos[0]
    else:
        x=firstQueenPos[1]
    #VERTICAL
    for a in range(firstQueenPos[0]+1,len(chessboard[firstQueenPos[0]])):
        if list1[a][firstQueenPos[1]]==1:
            return True
    #HORIZONTAL
    for b in range(firstQueenPos[1]+1,len(chessboard[firstQueenPos[0]])):
        if list1[firstQueenPos[0]][b]==1:
            return True
    #DIAGONAL 0
    for c in range(0,8-x):
        if c==0:
            continue
        if list1[firstQueenPos[0]+c][firstQueenPos[1]+c]==1:
            return True
    #DIAGONAL 1
    for c in range(x,0,-1):
        if c==0:
            continue
        if list1[firstQueenPos[0]+c][firstQueenPos[1]-c]==1:
            return True
    return False
"""
def printer(list1):
    for a in range(len(list1)):
        for b in range(len(list1[a])):
            print(list1[a][b],end=" ")
        print()
"""
chessboard= [[0 for a in range(8)] for a in range(8)]
chessboard[3][4]=1
chessboard[7][5]=1
#printer(chessboard)
print(queens(chessboard))
