#Task-6

class Shape:
    def __init__(self, name='Default', height=0, base=0):
        self.area = 0
        self.name = name
        self.height = height
        self.base = base
    def get_height_base(self):
        return "Height: "+str(self.height)+",Base: "+str(self.base)


#write your code here
class triangle(Shape):
    def __init__(self, name='Default', height=0, base=0):
        super().__init__(name, height, base)
    def printDetail(self):
        return "Shape name: "+self.name+"\n"+super().get_height_base()+"\n"+"Area: "+str(self.area)
    def calcArea(self):
        self.area=0.5*self.height*self.base

class trapezoid(triangle):
    def __init__(self, name='Default', height=0, base=0, side_a=0):
        super().__init__(name, height, base)
        self.side_a=side_a
    def printDetail(self):
        return "Shape name: "+str(self.name)+"\n"+super().get_height_base()+", Side_A: "+str(self.side_a)+"\n"+"Area: "+str(self.area)
    def calcArea(self):
        self.area=0.5*(self.height+self.side_a)*self.base


tri_default = triangle()
tri_default.calcArea()
print(tri_default.printDetail())
print("--------------------------")
tri = triangle('Triangle', 10, 5)
tri.calcArea()
print(tri.printDetail())
print("---------------------------")
trap = trapezoid('Trapezoid', 10, 6, 4)
trap.calcArea()
print(trap.printDetail())


"""
Shape name: Default
Height: 0, Base: 0
Area: 0.0
---------------------------
Shape name: Triangle
Height: 10, Base: 5
Area: 25.0
---------------------------
Shape name: Trapezoid
Height: 10, Base: 6, Side_A: 4
Area: 50.0
"""