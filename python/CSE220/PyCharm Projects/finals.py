def newYearGame(player,diceRoll,array=[],dice=0,count=0):
    arr1=["1","3","5","6"]
    arr2=["2","4"]
    if count==0:
        for a in range(player):
            array.append(a+1)
            player=0
    count+=1
    if len(array)==1:
        return array[0]
    if diceRoll[dice] in arr1:
        pass
    elif diceRoll[dice] in arr2:
        array.pop(player)
    player+=1
    dice+=1
    if player>=len(array):
        player=0
    if dice==len(diceRoll):
        dice=0
    return newYearGame(player,diceRoll,array,dice,count)
print(newYearGame(3,"152"))

hashed=["","","","","","","",""]
def hashtable(string):
    char,num=0,0
    for a in string:
        if a.isnumeric():
            num+=int(a)
        elif a!="A" or a!="E" or a!="I" or a!="O" or a!="U":
            char+=ord(a)
    total=char-num
    if total<0:
        total=0-total
    hashValue=total%8
    while hashed[hashValue]!="":
        hashValue+=1
        if hashValue>=len(hashed):
            hashValue-=len(hashed)
    hashed[hashValue]=string

def hashtable2(string):
    char=0
    num=0
    for a in string:
        if a.isnumeric():
            num+=int(a)
        elif a!="A" or a!="E" or a!="I" or a!="O" or a!="U":
            char+=ord(a)
    total=char-num
    if total<0:
        total*=-1
    hashValue=total%8
    while hashed[hashValue]!="":
        hashValue+=1
        if hashValue>=len(hashed):
            hashValue-=len(hashed)
    hashed[hashValue]=string
val=-1
val*=-1
print(val)
strings=["3C2SE11","8B41","DE4Z23DA","J4","6GOJE45"]
for a in strings:
    hashtable(a)
#hashtable("2C2SDE1")
print(hashed)

