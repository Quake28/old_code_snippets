def letter_score(letter):
    if letter == "" or letter==" ":
        return 0
    list1=[1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]
    return list1[ord(letter)-ord('A')]

def word_score(word, row=None, col=None, direction=None):
    triple_list=[[0,0],[0,7],[0,14],[7,0],[7,7],[7,14],[14,0],[14,7],[14,14]]
    double_list=[[1,1],[1,13],[2,2],[2,12],[3,3],[3,11],[4,4],[4,10],[10,4],[10,10],[11,3],[11,11],[12,2],[12,12],[13,1],[13,13]]
    score=0
    location=[row,col]
    multiplier=1
    tf = not(row==col and col==direction and direction==None)
    if tf and (row==None or col==None or direction==None):
        return("Invalid input: Missing parameter")
    if direction=="LR":
        increment=1
    elif direction=="TB":
        increment=0
    for a in word:
        if location in triple_list:
            multiplier=3
        elif location in double_list and multiplier<2:
            multiplier=2
        score+=letter_score(a)
        if tf:
            location[increment]+=1
    score*=multiplier
    return score

print(word_score("APPLE",0,6,"LR"))