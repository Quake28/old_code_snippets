import math
num=2

count=0
while count<10:
    x=1
    status = True
    for i in range(2,(math.ceil(math.sqrt(x))+1)):
        if(x%i==0):
            status = False
    if (status):
        x=x+1
        a=str(x)+". "+str(num)
        print(a)
        count+=1
    num=num+1
