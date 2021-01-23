"""
#Easy1
list1=[]
for a in range(10):
    list1.append(input("Enter a number: "))
list1.reverse()
print(list1)
"""

"""
#Easy2
input1=input("Enter list 1 seperated by commas(no whitespaces allowed): ")
input2=input("Enter list 2 seperated by commas(no whitespaces allowed): ")
list1=input1.split(",")
list2=input2.split(",")
list3=list1[:-1]+list2
print(list3)
"""

"""
#Easy3
list1=[]
for a in range(10):
    input1=input("Enter a number: ")
    while (input1 in list1) or (not input1.isnumeric()):
        input1=input("Number already exists or this is not a number,\nPlease re-enter a different number: ")
    list1.append(input1)
print(list1)
"""

"""
#Medium1
list1=[]
list2=[]
input1=input("Enter a number: ")
while input1!="STOP":
    list1.append(input1)
    input1=input("Enter a number: ")
a=0
while a<len(list1):
    list2.append(1)
    while list1[a] in list1[a+1:]:
        list2[a]+=1
        list1.pop(list1.index(list1[a],a+1))
    a+=1
for b in range(len(list1)):
    print(list1[b],"-",list2[b],"times")
"""

"""
#Medium2
count=input("Enter the number of lists you want to enter: ")
list1=[]
list2=[]
for a in range(int(count)):
    list1.append(input("Enter a list of numbers, use space so separate values: "))
for b in range(len(list1)):
    list1[b]=list1[b].split(" ")
for c in range(len(list1)):
    total=0
    for d in range(len(list1[c])):
        total+=int(list1[c][d])
    list2.append(total)
maximum=list2[0]
for e in range(len(list2)):
    if list2[e]>maximum:
        maximum=list2[e]
maximum=list2.index(maximum)
print(list2[maximum]+"\n"+list1[maximum])
"""

"""
#Medium3
list1=[]
list2=[]
list1.append(input("Enter a list of numbers, use space so separate values: "))
list1.append(input("Enter a list of numbers, use space so separate values: "))
for a in range(len(list1)):
    list1[a]=list1[a].split(" ")
for c in range(len(list1[0])):
    for d in range(len(list1[1])):
        list2.append(int(list1[0][c])*int(list1[1][d]))
print(list2)
"""

"""
#Medium4
list1=[]
count=int(input("Enter a number: "))
string=input("Enter a list of characters(separate with commas only, no whitespaces): ")
list1=string.split(",")
list2=[[],[],[]]
for a in range(count):
    for b in range(a,len(list1),count):
        list2[a].append(list1[b])
print(list2)
"""

"""
#Hard1
input1=input("Enter a list of numbers(separate only with whitespaces, type STOP to stop): ")
while input1!="STOP":
    list1=input1.split(" ")
    list2=[]
    jumperStatus=True
    for a in range(len(list1)-1):
        list2.append(int(list1[a])-int(list1[a+1]))
        if list2[a]<0:
            list2[a]*=-1
    for b in range(1,len(list2)):
        if not b in list2:
            jumperStatus=False
    if jumperStatus:
        print("UB Jumper")
    else:
        print("Not UB Jumper")
    input1=input("Enter a list of numbers(separate only with whitespaces, type STOP to stop): ")
"""

"""
#Hard2
input1=input("Enter a string: ")
list1=[]
list2=[[],[],[],[],[]]
for a in input1:
    list1.append(a)
for b in list1:
    if (ord(b)>47) and (ord(b)<58):
        if int(b)%2==1:
            list2[2].append(b)
        else:
            list2[3].append(b)
    elif (ord(b)>64) and (ord(b)<91):
        list2[1].append(b)
    elif (ord(b)>96) and (ord(b)<123):
        list2[0].append(b)
    else:
        list2[4].append(b)
for c in range(len(list2)):
    #Now running a bubble sort to sort everything into order
    for d in range(len(list2[c])):
        for e in range(len(list2[c])-1):
            if ord(list2[c][e])>ord(list2[c][e+1]):
                temp=list2[c][e]
                list2[c][e]=list2[c][e+1]
                list2[c][e+1]=temp
s=""
string=""
for f in range(len(list2)):
    string=string+s.join(list2[f])
print(string)
"""

"""
#Hard3
input1=input("Enter a n and k: ")
list1=input("Enter list of participations(use spaces to separate): ")
list1=list1.split(" ")
input1=input1.split(" ")
for a in range(len(list1)):
    list1[a]=int(list1[a])+int(input1[1])
participation=0
for b in list1:
    if b<6:
        participation+=1
print(int(participation/3))
"""
