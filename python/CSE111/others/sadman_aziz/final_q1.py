class SmartPhone:
    def __init__(self, name):
        self.name = name

    def check(self):
        print("The phone is working properly")


# Write your code here
class Xiaomi(SmartPhone):
    def __init__(self, name, year):
        super().__init__(name)
        self.year = year

    def check(self):
        print("This is Xiaomi {}\nRelease year: {}".format(self.name, self.year))
        super().check()


class Huawei(SmartPhone):
    def __init__(self, name, year):
        super().__init__(name)
        self.year = year

    def check(self):
        print("This is Huwawei {}\nRelease year: {}".format(self.name, self.year))
        super().check()


f = Xiaomi("Redmi Note 8", 2016)
c = Huawei("Y9", 2017)
f.check()
print("=========================")
c.check()
print("=========================")


"""
Output:
This is Xiaomi Redmi Note 8
Release year: 2016
The phone is working properly
=========================
This is Huawei Y9
Release year: 2017
The phone is working properly
=========================
"""
