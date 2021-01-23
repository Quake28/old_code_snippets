"""
RANDOM GENERATOR (NO DUPLICATE DATA ALLOWED, that's why code is so much longer than usual)
"""
import random
x=10
#x=int(input("Enter no. of elements in Binary tree: ")) #-Input for variable length tree instead of fixed length for random no. generator
binTree=[[0 for a in range (x)],[],[0 for b in range (x)]]
match=False
randcount=0#*
while len(binTree[1])<len(binTree[0]):
    randomnum=random.randint(0,99)
    randcount+=1#*
    for c in range(len(binTree[1])):
        if randomnum==binTree[1][c]:
            match=True
            break
        else:
            match=False
    if match:
        continue
    binTree[1].append(randomnum)

#----Debug prints----#
for d in range(len(binTree[1])):
    print(binTree[0][d],binTree[1][d],binTree[2][d])
print("\n")
print(randcount) #-No. of times random was necessary to be counted, using "#*" to denote it, for ease of removeal by commentning with "#"
print("\n")
#----Debug prints----#

"""
Calculating and forming the base of the binary tree
"""
for e in range (1,len(binTree[1])):
    nextpointer=0
    while True:
        if (binTree[1][e]>binTree[1][nextpointer])and(binTree[2][nextpointer]!=0):
            nextpointer=binTree[2][nextpointer]
        elif (binTree[1][e]<binTree[1][nextpointer])and(binTree[0][nextpointer]!=0):
            nextpointer=binTree[0][nextpointer]
        elif (binTree[1][e]>binTree[1][nextpointer])and(binTree[2][nextpointer]==0):
            binTree[2][nextpointer]=e
        elif (binTree[1][e]<binTree[1][nextpointer])and(binTree[0][nextpointer]==0):
            binTree[0][nextpointer]=e
        else:
            break
#----Final Output
for f in range(len(binTree[1])): 
    print(binTree[0][f],binTree[1][f],binTree[2][f])
print("\n"*2)

#----Attempt at creating one which is highly scalable and allows for use of modules and classes

class binary():
    def __init__(self): #-Initializing values
        self.pointernew=0
        self.tree=[[],[],[]]
    def verification(self, inputnum1): #-Verifying that the value does not exist in the tree already
        for a in range (len(self.tree[1])):
            if inputnum1==self.tree[1][a]:
                return True
        return False
    def addvalue(self,inputnum2): #-Appending the value to the tree
        self.pointernext=0
        self.tree[1].append(inputnum2)
        self.tree[0].append(0)
        self.tree[2].append(0)
    def addpointer(self,inoutnum3): #-Calculates and adds the pointers for each 
        for b in range (1,len(self.tree[1])):
            self.pointernew=0
            while True:
                if (self.tree[1][b]>self.tree[1][self.pointernew])and(self.tree[2][self.pointernew]!=0):
                    self.pointernew=self.tree[2][self.pointernew]
                elif (self.tree[1][b]<self.tree[1][self.pointernew])and(self.tree[0][self.pointernew]!=0):
                    self.pointernew=self.tree[0][self.pointernew]
                elif (self.tree[1][b]>self.tree[1][self.pointernew])and(self.tree[2][self.pointernew]==0):
                    self.tree[2][self.pointernew]=b
                elif (self.tree[1][b]<self.tree[1][self.pointernew])and(self.tree[0][self.pointernew]==0):
                    self.tree[0][self.pointernew]=b
                else:
                    break
    def printer(self): #-Prints the tree itself
        for f in range(len(self.tree[1])): 
            print(self.tree[0][f],self.tree[1][f],self.tree[2][f])
        print("\n")

d=binary()
while True:
    c=int(input("Enter a number : "))
    while d.verification(c): #-Loops input unless the number is unique
        c=int(input("Please enter another number, this already exists in the tree : "))
    d.addvalue(c)
    d.printer()
    d.addpointer(c)
    d.printer()
    e=input("Do you want to add more?(type anything and press enter for no) :")
    if e!="": #-Will break off of the loop if nothing is given as input
        break
