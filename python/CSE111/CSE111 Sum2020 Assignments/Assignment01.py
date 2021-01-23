"""
#Easy 1
for x in range (1,31):
    if x%3==0:
        if x%5==0:
            continue
        print(x)
    if x%5==0:
        print(x)
"""

"""
#Easy 2
x=[]
largest=0
for a in range (3):
    x.append(int(input("Enter a number: ")))
for b in range (len(x)):
    if x[b]>largest:
        largest=x[b]
print(largest)
"""

"""
#Easy 3
x=int(input("Enter a number: "))
if (x<0) or (x>100):
    print("Invalid")
elif x<50:
    print("F")
elif x<52:
    print("D-")
elif x<55:
    print("D")
elif x<57:
    print("D+")
elif x<60:
    print("C-")
elif x<65:
    print("C")
elif x<70:
    print("C+")
elif x<75:
    print("B-")
elif x<80:
    print("B")
elif x<85:
    print("B+")
elif x<90:
    print("A-")
else:
    print("A")
"""

"""
#Easy 4
import math
x=int(input("Enter a number: "))
status=True
if (x<0)or(x>2):
    for a in range (2,math.floor(x/2)):
        if x%a==0:
            status=False
            break
if status:
    print("Number is prime")
else :
    print("Number is not a prime")
"""

"""
#Medium 1
n=int(input("Enter a number: "))
c1=0
c2=1
c3=c1+c2
print(str(c1)+" "+str(c2),end=" ")
while c3<n:
    print(c3,end=" ")
    c1=c2
    c2=c3
    c3=c1+c2
"""

"""
#Medium 2
x=input("Enter a number: ")
for a in range (0, len(x)):
    print(x[-(a+1)],end="")
"""


"""
#Medium 3
x=int(input("Enter a number: "))
status=False
total=0
for a in range (1,x):
    if x%a==0:
        total+=a
if x==total:
    status=True
if status:
    print("Perfect Number")
else :
    print("Not Perfect")
"""

"""
#HARD 1
x=input("Enter a number: ")
y=0
for a in range(0,10):
    z=0
    for b in range(len(x)):
        if int(x[b])==a:
            if z==0:
                y+=1
            z+=1
print(str(y)+".")
"""

"""
#HARD 2
x=int(input("Enter height: "))
for a in range(1,x):
    if a==1:
        print(" "*(x-a)+"*")
    if a!=1:
        print(" "*(x-a)+"*"+" "*(1+2*(a-2))+"*")
print("*"*(1+2*a))

for a in range(x-1,0,-1):
    if a==1:
        print(" "*(x-a)+"*")
    if a!=1:
        print(" "*(x-a)+"*"+" "*(1+2*(a-2))+"*")

"""

"""
#HARD 3
x=int(input("Enter a number: "))
#Binary conversion
a=0
while 2**a<x:
    a+=1
binary="0"*a
b=len(binary)
while x!=0:
    c=0
    while (2**c<x)or(c==0):
        c+=1
    c-=1
    x-=2**c
    binary=binary[:b-c-1]+"1"+binary[b-c:]
d=0
for e in range(len(binary)):
    if binary[e]=="1":
        d+=1
f=0
for g in range(d):
    f+=2**g
print(f)
"""
