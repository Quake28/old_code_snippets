"""
#Easy1
sample=input("Enter a string: ")
vowels=["a","e","i","o","u"]
vowelCount=0
formatted=sample.lower()
for a in vowels:
    while True:
        if a in formatted:
            formatted=formatted.replace(a,"",1)
            vowelCount+=1
        else:
            break 
print(formatted+str(vowelCount))
"""


"""
#Easy2
sample=input("Enter a string: ")
reverseString=""
for a in range (len(sample)-1,-1,-1):
    reverseString+=sample[a]
if reverseString==sample:
    print("True")
else:
    print("False")
"""

"""
#Easy3
sample=input("Enter a string: ")
outpuString=""
if sample.endswith("ful"):
    sample=sample+"ly"
elif len(sample)>3:
    sample=sample+"ful"
print(sample)
"""

"""
#Medium1
sample=input("Enter a string: ")
uppercase=0
lowercase=0
outputString=""
for a in sample:
    if a.isupper():
        uppercase+=1
    elif a.islower():
        lowercase+=1
if uppercase>lowercase:
    outputString=sample.upper()
else:
    outputString=sample.lower()
print(outputString)
"""

"""
#Medium2
sample=input("Enter a string: ")
if sample.isnumeric():
    print("NUMBER")
elif sample.isalpha():
    print("WORD")
else:
    print("MIXED")
"""

"""
#Medium3
sample=input("Enter a string: ")
substring=""
for a in range(len(sample)):
    if sample[a].isupper():
        a+=1
        while sample[a].islower():
            substring+=sample[a]
            a+=1
        break
if substring=="":
    print("BLANK")
else:
    print(substring)
"""

"""
#Medium4
sample=input("Enter a string: ")
sample=sample.replace("too good","excellent")
print(sample)
"""

"""
#Hard1
sample1=input("Enter a string: ")
sample2=input("Enter a second string: ")
commons=""
finalString=""
copy1=sample1
copy2=sample2
a=0
while a<len(copy1):
    if copy2.find(copy1[a])!=-1:
        commons+=copy1[a]
        copy2=copy2.replace(copy1[a],"")
        copy1=copy1.replace(copy1[a],"")
    a+=1
for b in range(len(commons)):
    c=0
    while c<len(sample1):
        found=sample1.find(commons[b],c)
        if found!=-1:
            finalString+=sample1[found]
            c=found
        else:
            break
        c+=1
for d in range(len(commons)):
    e=0
    while e<len(sample2):
        found=sample2.find(commons[d],e)
        if found!=-1:
            finalString+=sample2[found]
            e=found
        else:
            break
        e+=1
if finalString=="":
    print("Notihng in common")
else:
    print(finalString)
"""

"""
#Hard2
sample=input("Enter a string: ")
substring=""
for a in range(1,int(len(sample)/3)+1):
    if sample[len(sample)-a:]==sample[:a]:
        if sample.find(sample[:a],1,len(sample)-a+1)!=-1:
            #it just looked too messy in one line
            #so decided to use nested if
            #it wasn't really necessary
            #Basic code hygiene? *Thinking emoji* 🤔
            substring=sample[:a]
if substring=="":
    print("Not Palindrome Substring")
else:
    print(substring)
"""

"""
#Hard3
x=input("Enter new password: ")
specChars=["_","$","#","@"]
upper=False
lower=False
digit=False
specChar=False

for a in range(len(x)):
    if x[a].isupper():
        upper=True
    if x[a].islower():
        lower=True
    if x[a].isnumeric():
        digit=True
for b in specChars:
    if x.find(b)!=-1:
        specChar=True
start=""
if not upper:
    print("Uppercase character missing",end="")
    start=", "
if not lower:
    print(start+"Lowercase character missing",end="")
    start=", "
if not digit:
    print(start+"Digit missing",end="")
    start=", "
if not specChar:
    print(start+"Special character missing")
if upper and lower and digit and specChar:
    print("OK")
"""
