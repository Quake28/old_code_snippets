#Question 1
"""
word=input("Enter a word: ")
string=[]
if len(word)>1:
    for d in range(len(word)):
        string.append(word[d])
    if (string[-1]=="a") or(string[-1]=="e") or(string[-1]=="i") or (string[-1]=="o") or (string[-1]=="u"):
        string.append("yay")
        temp=string[-1]
        for a in range(len(string)-1,0,-1):
            string[a]=string[a-1]
        string[0]=temp
    else:
        temp=string[-1]
        for b in range(len(string)-1,0,-1):
            string[b]=string[b-1]
        string[0]=temp
        string.append("ay")
for c in string:
    print(c,end="")
"""

#Question 2
"""
string=input("Enter a word: ")
list1=string.split(", ")
list2=[]
for a in list1:
    if a[-4:]!="WXYZ":
        list2.append(a)
print(list2)
"""

#Question 3
"""
import math
def calculateArea(x,y=-1):
    if y==-1:
        print("Area of the circle is:", round(math.pi*(x**2),4))
    else:
        print("Area of the triangle is:", x*y*0.5)
calculateArea(4,4)
"""

"""
string="asdASDFasd"
status1=False
for a in range(len(string)-4):
    status=True
    for b in range(4):
        if string[a+b].islower():
            status=False
            break
    if status:
        status1=True
        break
if status1:
    print("Found")
else:
    print("Not Found")
"""
"""
How many censored words are there? 
3 
Please enter censored/uncensored pair #1: 
mean unpleasant 
Please enter censored/uncensored pair #2: 
fat bulky 
Please enter censored/uncensored pair #3: 
obnoxious confident 
Please enter a sentence with lowercase letters only: 
the mean obnoxious bully yelled at fat people 
The censored sentence is as follows(Output): 
the unpleasant confident bully yelled at bulky people
"""
"""
censors=[[],[]]
num=int(input("How many censored words are there?: "))
for a in range(num):
    words=input("Please enter censored/uncensored pair #"+str(a+1)+": ")
    words=words.split()
    censors[0].append(words[0])
    censors[1].append(words[1])
string=input("Please enter a sentence with lowercase letters only: ")
string=string.split()
for b in range(len(string)):
    for c in range(len(censors[0])):
        if string[b]==censors[0][c]:
            string[b]=censors[1][c]
s=" "
print("The censored sentence is as follows(Output): ")
string=s.join(string)
print(string)
"""

"""
def thisFunction(list1):
    list2=[]
    for a in range(len(list1)):
        if list1[a]%2==0:
            list2.append(list1[a])
    if len(list2)<2:
        print("-1")
    else:
        for b in range(len(list2)):
            for c in range(len(list2)-1):
                if list2[c+1]>list2[c]:
                    temp=list2[c]
                    list2[c]=list2[c+1]
                    list2[c+1]=temp
        print(list2[0]*list2[1])

listz=[1,2,3,4,5,6,7]
thisFunction(listz)
"""


string=input("Enter a string: ")
list1=[]
for a in range(len(string)):
    list1.append(ord(string[a]))
for b in range(len(list1)):
    list1[b]+=4
    if list1[b]>90:
        list1[b]-=27
for c in range(len(list1)):
    list1[c]=chr(list1[c])
s=""
string=s.join(list1)
print(string)
