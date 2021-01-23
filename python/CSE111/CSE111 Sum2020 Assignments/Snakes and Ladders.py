#SNAKE LUDO
import math
import random
class Player():
    ladders = [[6,10],[8,33],[26,3],[50,43],[59,25]]
    snakes = [[32,-20],[60,-22],[63,-60],[70,-45],[73,-26],[82,-39],[89,-36],[97,-85]]
    def __init__(self,a):
        self.name=a
        self.currentPosition=0
    def position(self,x):
        self.currentPosition+=x
        self.outputPosition()
        for a in range(len(Player.ladders)):
            if self.currentPosition==Player.ladders[a][0]:
                print("Congratulations! You have reached a ladder!")
                self.outputPosition(self.currentPosition+Player.ladders[a][1])
                self.currentPosition+=Player.ladders[a][1]
        for b in range(len(Player.snakes)):
            if self.currentPosition==Player.snakes[b][0]:
                print("Oh no! You have reached a snake!")
                self.outputPosition(self.currentPosition+Player.snakes[b][1])
                self.currentPosition+=Player.snakes[b][1]
    def outputPosition(self,x=None):
        if x==None:
            print("Your current position is {}".format(self.currentPosition))
        else:
            print("Your position changed from {} to {}".format(self.currentPosition,x))

    def move (self):
        input("\n{} press Enter/Return key to roll.".format(self.name))
        value=random.randint(1,6)
        print ("The dice rolled " + str(value))
        #SOME DECISION MAKING:
        if (self.currentPosition==0 and value!=1):
            print ("Sorry, your move will be discarded, you need to roll a 1 to start.")
        elif value+self.currentPosition>100:
            print ("Sorry, your move will be discarded, this is an invalid move.")
        else:
            self.position(value)
#==========================================================
print ("Welcome to Snake Ludo!")
#INPUTTING THE NUMBER OF PLAYERS
count = 2
while (count >= 2):
    try:
        num_of_players = int(input("Please enter the number of players(minimum 2): "))
        if (num_of_players < 2):
            print ("You need at least two players to start the game!")
            continue
        elif (num_of_players == 2):
            print ("Let's start!")
            break
    except:
        print ("Please enter a valid number.")
#TAKING NAMES
names = []
for c in range(num_of_players):
    names.append(Player(input("Please enter the name of the player " + str(c+1) + ": ")))
    print ("Hello! " + names[c].name)
#GAME STARTS
winCondition=False
while True:
    for d in names:
        d.move()
        if (d.currentPosition == 100):
            print ("You have won the game, " + d.name)
            winCondition=True
            break        
    if winCondition:
        break
