# Answer no. 1

"""
Output:
No.of Smartphone = 0
=========================
Model Name: Oneplus 9 Pro
Year of release: 2021
Features: Snapdragon 888, Wireless Charging, Hasselblad Camera
=========================
Model Name: Samsung Galaxy S21
Year of release: 2020
Features: Exynos 2100, Fast charging 25W
=========================
Model Name: MI 11 Ultra
Year of release: 2021
Features: Fast charging 67W,  Snapdragon 888
=========================
No.of Smartphone = 3
"""


class Smartphone:
    count = 0

    def __init__(self, a, b):
        self.name = a
        self.release_year = b
        Smartphone.count += 1

    def add_Features(self, *args):
        self.features = args

    def printPhoneDetail(self):
        print("Model Name:", self.name)
        print("Year of release:", self.release_year)
        print("Features: ", end="")
        print_string = ""
        for a in self.features:
            print_string += a + ", "
        print(print_string[:-2])


print("No.of Smartphone =", Smartphone.count)
s1 = Smartphone("Oneplus 9 Pro", 2021)
s1.add_Features("Snapdragon 888", "Wireless Charging", "Hasselblad Camera")
s2 = Smartphone("Samsung Galaxy S21", 2020)
s2.add_Features("Exynos 2100", "Fast charging 25W")
s3 = Smartphone("MI 11 Ultra", 2021)
s3.add_Features("Fast charging 67W", "Snapdragon 888")
print("=========================")
s1.printPhoneDetail()
print("=========================")
s2.printPhoneDetail()
print("=========================")
s3.printPhoneDetail()
print("=========================")
print("No.of Smartphone =", Smartphone.count)
