#*****STARLABS!*****

"""
#Question09
h=int(input("Enter height: "))
for a in range(1,h+1):
    print(" "*(h-a)+"*"*((a*2)-1))
"""

"""
#Question10
h=int(input("Enter height: "))
for a in range(1,h+1):
    print(" "*(h-a),end="")
    for b in range(1,(a*2)):
        print(b,end="")
    print()
"""

"""
#Question11
h=int(input("Enter height: "))
for a in range(h,0,-1):
    print(" "*(a-1),end="")
    for b in range(a,h+1):
        print(b,end="")
    print()
"""

"""
#Question12
h=int(input("Enter height: "))
for a in range(1,h+1):
    print(" "*(h-a)+"*"*((a*2)-1))
for b in range(h-1,0,-1):
    print(" "*(h-b)+"*"*((b*2)-1))
"""

"""
#Question13
h=int(input("Enter height: "))
for a in range(1,h+1):
    print(" "*(h-a),end="")
    for b in range(1,(a*2)):
        print(b,end="")
    print()
for c in range(h-1,0,-1):
    print(" "*(h-c),end="")
    for d in range(1,(c*2)):
        print(d,end="")
    print()
"""

"""
#Question14
h=int(input("Enter height: "))
w=int(input("Enter width: "))
print("*"*w)
for a in range(h-2):
    print("*"+" "*(w-2)+"*")
print("*"*w)
"""

"""
#Question15
h=int(input("Enter height: "))
w=int(input("Enter width: "))
for a in range(1,w+1):
    print(a,end="")
print()

for b in range(h-2):
    print("1"+" "*(w-2)+str(w))
for a in range(1,w+1):
    print(a,end="")
print()
"""

"""
#Question16
h=int(input("Enter height: "))
print("*")
for a in range(h-2):
    print("*"+" "*a+"*")
print("*"*h)
"""

"""
#Question17
h=int(input("Enter height: "))
print("1")
for a in range(h-2):
    print("1"+" "*a+str(a+2))
for b in range(1,h+1):
    print(b,end="")
"""

"""
#Question18
h=int(input("Enter height: "))
print(" "*(h-1)+"*")
for a in range(h-2):
    print(" "*(h-a-2)+"*"+" "*a+"*")
print("*"*h)
"""

"""
#Question19
h=int(input("Enter height: "))
print(" "*(h-1)+str(h))
for a in range(h-2):
    print(" "*(h-a-2)+str(h-a-1)+" "*a+str(h))
for b in range(1,h+1):
    print(b,end="")
"""

"""
#Question20
h=int(input("Enter height: "))
print(" "*(h-1)+"*")
for a in range(1,h-1):
    print(" "*(h-a-1)+"*"+" "*(a*2-1)+"*")
print("*"*(h*2-1))
"""

"""
#Question21
h=int(input("Enter height: "))
print(" "*(h-1)+"1")
for a in range(1,h-1):
    print(" "*(h-a-1)+"1"+" "*(a*2-1)+str(a*2+1))
for b in range(1,h*2):
    print(str(b),end="")
"""

"""
#Question22
h=int(input("Enter height: "))
print(" "*(h-1)+"*")
for a in range(1,h-1):
    print(" "*(h-a-1)+"*"+" "*(a*2-1)+"*")
print("*"+" "*(h*2-3)+"*")
for b in range(h-1,1,-1):
    print(" "*(h-b)+"*"+" "*((b-1)*2-1)+"*")
print(" "*(h-1)+"*")
"""

"""
#Question23
h=int(input("Enter height: "))
print(" "*(h-1)+"1")
for a in range(1,h-1):
    print(" "*(h-a-1)+"1"+" "*(a*2-1)+str(a*2+1))
print("1"+" "*(h*2-3)+str(h*2-1))
for b in range(h-1,1,-1):
    print(" "*(h-b)+"1"+" "*((b-1)*2-1)+str((b-1)*2-1))
print(" "*(h-1)+"1")
"""

"""
#Question24
h=int(input("Enter height: "))
for a in range(1,h+1):
    print(" "*(h-a),end="")
    for b in range(1,a+1):
        print(b,end="")
    for c in range(a-1,0,-1):
        print(c,end="")
    print()
"""
