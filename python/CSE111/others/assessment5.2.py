# Answer
"""
Output:
Total E-Customer: 0
=========================
Name:   James
Total cost with delivery charge: 46410.0
=========================
Name:   Mike
Total cost with delivery charge: 73040.0
=========================
Name:   Sarah
Total cost with no delivery charge: 1400.0
=========================
Name:   John
Total cost with delivery charge: 66220.0
=========================
Total E-Customer: 4
"""

# Write your codes here.
class ECustomer:
    count=0
    def __init__(self,a):
        self.name = a
        self.products=[]
        self.prices=[]
        ECustomer.count+=1
    def setProductDetails(self,*params):
        for a in range(0,len(params),2):
            self.products.append(params[a])
            self.prices.append(params[a+1])
    def printDetail(self):
        print("Name:",self.name)
        additionalFee=0
        summation=200
        for a in self.prices:
            summation+=a
        if summation>50000:
            additionalFee+=summation/10
        elif summation>10000:
            additionalFee+=summation/20
        print("Total cost with delivery charge:",summation+additionalFee)
# Do not change the following lines of code.
print("Total E-Customer:", ECustomer.count)
c1 = ECustomer("James")
c1.setProductDetails("TV",35000,"Air Cooler", 9000)
c2 = ECustomer("Mike")
c2.setProductDetails("Mobile",20000,"Headphone", 1200, "Fridge", 45000)
c3 = ECustomer("Sarah")
c3.setProductDetails("Headphone", 1200)
c4 = ECustomer("John")
c4.setProductDetails("AC",60000)
print("=========================")
c1.printDetail()
print("=========================")
c2.printDetail()
print("=========================")
c3.printDetail()
print("=========================")
c4.printDetail()
print("=========================")
print("Total E-Customer:", ECustomer.count)
