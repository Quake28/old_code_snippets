"""
class Mammal(object):
    def __init__(self, mammalName, leg_no):
        self.name=mammalName
        self.leg_no=leg_no
    def print(self):
        print(self.name, "has", self.leg_no,"legs.")
        print(self.name, "is a warm-blooded animal")

#######################################
class Dog(Mammal):
    def __init__(self):
        super().__init__("Dog",4)
class Human(Mammal):
    def __init__(self):
        super().__init__("Human",2)
#######################################
d1=Dog()
print("************")
d1.print()
h1=Human()
print("************")
h1.print()
"""

"""
import math
class Geometry:
    count=0
    def __init__(self):
        Geometry.count+=1
        self.area=0
    def circleArea(self,r):
        self.area=round(math.pi*r**2,2)
    def triangleArea(self,b,h):
        self.area=0.5*b*h
    def squareArea(self,l):
        self.area=l**2
    def printingDeatils(self):
        print(f"The Area is {self.area}")
        
##########################333
print("No of Geometry chapters:", Geometry.count)
circle=Geometry()
triangle=Geometry()
square=Geometry()
print("No of Geometry chapters:", Geometry.count)
circle.circleArea(5)
print("***********")
circle.printingDeatils()
triangle.triangleArea(3,6)
print("***********")
triangle.printingDeatils()
square.squareArea(4)
print("***********")
square.printingDeatils()
"""

"""
dividend=int(input())
list1=[]
for a in range(1,int(dividend/2)+1):
    if dividend%a==0:
        if a not in list1:
            list1.append(a)
list1.append(dividend)
dict1={}
for b in list1:
    string=input()
    while True:
        try:
            if dict1[string]:
                string=input()
        except:
            dict1[string]=b
            break
print(dict1)
"""
