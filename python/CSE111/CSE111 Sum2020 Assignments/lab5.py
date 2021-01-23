"""
class DataType():
    def __init__(self,x,y):
        self.name=x
        self.value=y

data_type1 = DataType("Integer", 1234)
print(data_type1.name)
print(data_type1.value)
print('=====================')
data_type2 = DataType("String", "Hello")
print(data_type2.name)
print(data_type2.value)
print('=====================')
data_type3 = DataType("Float", 4.0)
print(data_type3.name)
print(data_type3.value)
"""

class Flower():
    def __init__(self):
        self.name=""
        self.color=""
        self.num_of_petal=""
flower1 = Flower()
flower1.name="Rose"
flower1.color="Red"
flower1.num_of_petal=6
print("Name of this flower:", flower1.name)
print("Color of this flower:",flower1.color)
print("Number of petal:",flower1.num_of_petal)
print("=====================")
flower2 = Flower()
flower2.name="Orchid"
flower2.color="Purple"
flower2.num_of_petal=4
print("Name of this flower:",flower2.name)
print("Color of this flower:",flower2.color)
print ("Number of petal:",flower2. num_of_petal)
print(flower1,flower2)
if flower1==flower2:
  print("They are same")
else:
  print("They are different")
