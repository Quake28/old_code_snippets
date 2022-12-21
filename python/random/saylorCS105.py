import re
"""
def sget(string):
    # write your code here
    regex = re.compile(r'[A-Z]\.\s')
    return regex.findall(string)
    
s='FirstName M. LastName'
print(sget(s))

"""
import math
import random
import matplotlib.pyplot as plt
"""
def getstr(str_list):
    pattern = '...[w-z]'#fill in instruction here
    regex = re.compile(pattern)
    for val in str_list:
        if regex.match(val):
            print(val)
    return
getstr(["asdw"])
"""
def get_log(n):
    try:
        z=math.log(n)
    except ValueError:
        print('Input argument must be nonnegative')
        z=None
    else:
        return z
        
print(get_log(0))