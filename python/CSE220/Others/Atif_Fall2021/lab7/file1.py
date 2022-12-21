"""
# TASK 2
arr=[None for a in range(10)]
for z in range(10):
    string = input("Enter string : ")
    vowels = ["a","e","i","o","u"]
    total = 0
    for a in string:
        if a.isnumeric():
            total+=int(a)
        elif a.lower() not in vowels:
            total+=24
    hash=total%9
    status=False
    while arr[hash]!=None:
        hash+=1
        if hash>=len(arr):
            status=True
            break
    if status:
        arr.append(string)
    else:
        arr[hash]=str
        
"""

# TASK 1
import random
class KeyIndex:
    def __init__(self,arr):
        xmin=min(arr)
        xmax=max(arr)
        diff=xmax-xmin
        self.bias=xmin
        self.arr=[0 for a in range(diff+1)]
        for a in arr:
            self.arr[a-self.bias]+=1
    def search(self,num):
        count=0
        if num-self.bias<len(self.arr):
            if self.arr[num-self.bias]>0:
                for a in self.arr[:num-self.bias]:
                    count+=a
            else:
                return False
        else:
            return False
        return count-1
    def sort(self):
        arr=[]
        #print(self.bias)
        for a in range(len(self.arr)):
            #print(a+self.bias,a)
            for b in range(0,self.arr[a],1):
                arr.append(a+self.bias)
        return arr

def test():
    arr=[random.randint(-5,5) for a in range(5)]
    print(arr)
    key = KeyIndex(arr)
    print(key.bias,key.arr)
    search_result = key.search(5)
    if search_result==False:
        print("Not Found")
    else:
        print(str(search_result)+"th position")
    print(key.sort())
test()