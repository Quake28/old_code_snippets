def recursion(x,y,c=0,b=0):
    if len(x)==1:
        return x[0]
    if c>=len(x):
        c=0
    if b==len(y):
        b=0
    if y[b]=="2" or y[b]=="4":
        return recursion(x[:c]+x[c+1:],y,c,b+1)
    else:
        return recursion(x,y,c+1,b+1)

a=int(input())
x=[a+1 for a in range(a)] 
y=input()

player=recursion(x,y)

print(player)