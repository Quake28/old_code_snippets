class BattleShipBoard():
    def __init__(self,a,b):
        self.dimension=a
        self.player1Board=[[b for x in range(a)]for y in range(a)]
        self.player2Board=[[b for x in range(a)]for y in range(a)]
    def toString(self):
        for c in range(len(self.player1Board)):
            for d in range(len(self.player1Board[0])):
                print(self.player1Board[c][d]+" ",end="")
            print("\t",end="")
            for e in range(len(self.player2Board[0])):
                print(self.player2Board[c][e]+" ",end="")
                if e==(len(self.player2Board[0])-1):
                    print()
    def addBoat(self,x, y, direction, size, playerNumber):
        #ADDING BOATS
        if(playerNumber==0):
            if(direction==0):
                for h in range(x,x+size):
                    self.player1Board[y][h]="B"
            elif(direction==1):
                for h in range(y,y+size):
                    self.player1Board[h][x]="B"
        elif(playerNumber==1):
            if(direction==0):
                for h in range(x,x+size):
                    self.player2Board[y][h]="B"
            elif(direction==1):
                for h in range(y,y+size):
                    self.player2Board[h][x]="B"
    def shoot(self,x, y, playerNumber):
        #ATTEMPT TO SHOOT BOATS\
        if(playerNumber==0):
            if self.player2Board[y][x]=="B":
                self.player2Board[y][x]="X"
        elif(playerNumber==1):
            if self.player1Board[y][x]=="B":
                self.player1Board[y][x]="X"
    def isGameOver(self):
        #GOES THROUGH BOTH THE ARRAYS TO DETERMINE IF THE GAME IS OVER OR NOT, AND PRINTS IF GAME IS OVER
        status = 0
        countB1 = 0
        countB2 = 0
        for m in range(self.dimension):
            for n in range(self.dimension):
                if(self.player1Board[m][n]=="B"):
                    countB1+=1
                if(self.player2Board[m][n]=="B"):
                    countB2+=1
        if ((countB1==0) and (countB2==0)):
            status = 3
        elif ((countB1>0) and (countB2>0)):
            status = 0
        elif (countB1>countB2):
            status = 1
        elif (countB1<countB2):
            status = 2
        return status
    def winCondition(self,x):
        #PRINTS IF THE GAME IS OVER OR NOT, OR WHO WON THE GAME
        if (x==0):
            print("Game is not over.")
        elif (x==1):
            self.toString()
            print("Game Over! Player 1 won the game.")
        elif (x==2):
            self.toString()
            print("Game Over! Player 2 won the game.")
        else:
            self.toString()
            print("Game is over, DRAW!")
class Main():
    def __init__(self):
        inputstr = input("Enter dimensions and symbol for water. Format - <dimensions> <symbol>: ")
        inputstr=inputstr.split()
        dimension = int(inputstr[0])
        waterSymbol = inputstr[1][0]
        x = BattleShipBoard(dimension, waterSymbol)
        boatNum = int(input("Enter number of Boats : "))

        #ADD BOATS ACCORDING TO BOAT NUMBERS    
        for f in range(boatNum):
            for g in range(2):
                #TAKE IN COORDINATES, DIRECTION AND SIZE
                splitInt = input("[Player "+str(g+1)+"] Enter the coordinates(x,y), direction (0/1), and size of the boats to be added. Format - <x> <y> <direction> <size> : ")
                splitInt=splitInt.split()
                for m in range(4):
                    splitInt[m]=int(splitInt[m])
                x.addBoat(splitInt[0],splitInt[1],splitInt[2],splitInt[3],g)
        x.toString()
        #ENTER NUMBER OF SHOTS
        shotNum = int(input("Enter number of shots to be taken : "))
        init = 0
        #TAKE SHOTS ACCORDING TO NUMBER OF SHOTS
        while (x.isGameOver()==0) :
            for f in range(shotNum) :
                for g in range(2) :
                    #TAKE IN COORDINATES TO SHOOT
                    splitInt2 = input("[Player "+str(g+1)+" : Shot#"+str(init+1)+"] Enter the coordinates(x,y) for the shot to be taken. Format - <x> <y> : ")
                    splitInt2=splitInt2.split()
                    for m in range(2) :
                        splitInt2[m]=int(splitInt2[m])
                    x.shoot(splitInt2[0],splitInt2[1],g)
                init+=1
            shotNum=1
            x.winCondition(x.isGameOver())
Main()
