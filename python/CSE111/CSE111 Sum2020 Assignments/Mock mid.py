#Question 1
"""
x=input("Enter a string: ")
count=0
for a in x:
    if a<="Z" and a>="A" :
        count+=1
print("Number of capital letters:",count)
"""

#Question 2
"""
def palindromeCheck(x):
    x=x.replace(" ","")
    y=[]
    for a in range(len(x)):
        y.append(x[a])
    y.reverse()
    s=""
    y=s.join(y)
    if x==y:
        return True
    else:
        return False
stringInput=input("Enter a string: ")
print(palindromeCheck(stringInput))
"""

#Question 3
#W,79,V,89,U,63,Y,54,X,91
"""
stringInput=input("Enter data: ")
x=stringInput.split(",")
y=[]
z=[]
for a in range(0,len(x),2):
    y.append(x[a])
for b in range(1,len(x),2):
    z.append(x[b])
for c in range(len(y)):
    for d in range(len(y)-1):
        if y[d]>y[d+1]:
            temp=y[d]
            y[d]=y[d+1]
            y[d+1]=temp
            temp=str(z[d])
            z[d]=str(z[d+1])
            z[d+1]=str(temp)
finalList=[]
for e in range(len(y)):
    finalList.append(y[e])
    finalList.append(z[e])
print(finalList)
"""
