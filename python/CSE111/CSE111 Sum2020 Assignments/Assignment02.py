"""
#Easy1
def remainder(x,y):
    if y==0:
        return 0
    return (x/y)%1

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
print(remainder(a,b))
"""

"""
#Easy2
def bmi(x,y):
    y=y/100
    z=round(x/(y**2),1)
    if z<18.5:
        print("Underweight")
    elif z<25:
        print("Normal")
    elif z<30.1:
        print("Overweight")
    else:
        print("Obese")

a=int(input("Enter weight: "))
b=float(input("Enter height(cm): "))
bmi(a,b)
"""

"""
#Easy3
def num(x,y,z):
    total=0
    for a in range(x,y):
        if a%z==0:
            total+=a
    return total
    

a=int(input("Enter minimum number: "))
b=int(input("Enter maximum number: "))
c=int(input("Enter divisor: "))
print(num(a,b,c))
"""

"""
#Medium1
def foodPanda(y="Outside of Mohakhali",*x):
    total=40
    if (y!="mohakhali") or (y!="Mohakhali"):
        total+=20
    for a in x:
        if a=="Beef Burger":
            total+=170
        elif a=="BBQ Chicken Cheese Burger":
            total+=250
        else:
            total+=200
    return round(total*1.08, 2)

food=[]
while True:
    xinput=input("Enter item name (leave empty to continue): ")
    if xinput=="":
        break
    food.append(xinput)
location=input("Enter your location: ")
print(foodPanda(location,*food))
"""

"""
#Medium2
def replace_domain(x,y,z="sheba.com"):
    return (x[:(len(x)-(len(z)))]+y)
email=input("Enter email: ")
new_domain=input("Enter new domain: ")
old_domain=input("Enter old domain: ")
if old_domain=="":
    print(replace_domain(email,new_domain))
else:
    print(replace_domain(email,new_domain,old_domain))
"""

"""
#Medium3
def vowel(x):
    vowel_list=["a","e","i","o","u"]
    vowel_present=[]
    for a in x:
        for b in vowel_list:
            if a==b:
                vowel_present.append(b)
    print("Vowels: ",end="")
    for c in range(len(vowel_present)):
        ending=", "
        if c==len(vowel_present)-1:
            ending=". "
        print(vowel_present[c],end=ending)
    print("Total number of vowels: "+str(len(vowel_present)))
stringInput=input("Enter a string: ")
vowel(stringInput)
"""

"""
#Medium4
def palindrome(x):
    y=""
    for a in range (len(x)-1,-1,-1):
        y+=x[a]
    if x==y:
        print("Palindrome")
    else:
        print("Not Palindrome")
stringInput=input("Input a string: ")
palindrome(stringInput)
"""

"""
#Hard1
import datetime
def bonus(x,y,z):
    pass
    cT=datetime.datetime.now()
    for a in range(len(x)):
        print(x[a],end=": ")
        service=int(((365*(cT.year-z[a].year))+int(cT.strftime("%j"))-int(z[a].strftime("%j")))/365)
        if service<5:
            bonus=int(0.1*y[a])
        elif service<=10:
            bonus=int(0.1*y[a]+5000)
        else:
            bonus=int((0.15*y[a])+15000)
        ending=", "
        if a==len(x)-1:
            ending=""
        print(bonus,end=ending)
name=[]
salary=[]
date=[]
while True:
    name_input=input("Enter name (leave blank to stop):")
    if name_input=="":
        break
    name.append(name_input)
    salary.append(int(input("Enter salary:")))
    dateInput=input("Enter name (format= yyyymmdd, eg, 20201231):")
    date.append(datetime.datetime(int(dateInput[:4]),int(dateInput[4:6]),int(dateInput[6:])))
bonus(name,salary,date)   
"""

"""
#Hard2
def time(num):
    x=num/365
    y=(x%365)/30
    z=(x%365)%30
    print("%d years, %d months and %d days" % (x,y,z))
dayCount=int(input("Enter day count: "))
time(dayCount)
"""

"""
#Hard3
#my favourite animal is a dog. a dog has sharp teeth so that it can eat flesh very easily. do you know my pet dog’s name? i love my pet very much.
def capitalization(x):
    for a in range(len(x)-2):
        if x.find(" i ",a)==-1:
            break
        a=x.find(" i ",a)
        x=x[:a+1]+"I"+x[a+2:]
    y=[".","!","?"]
    for b in range(len(y)):
        c=0
        while c<len(x):
            if x.find(y[b],c)==-1:
                break
            print(c)
            c=x.find(y[b],c)
            print(c)
            if c+3<len(x):
                x=x[:c+2]+x[c+2].upper()+x[c+3:]
            c+=1
    x=x[0].upper()+x[1:]
    print(x)
string=input("Enter text:")
z="my favourite animal is a dog. a dog has sharp teeth so that it can eat flesh very easily. do you know my pet dog’s name? i love my pet very much."
capitalization(z)
"""
