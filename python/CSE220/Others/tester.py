class Surprise:
    def mystery(self,n):
        print("h(" ,n,")")
        if(n==0):
            print("value: 0")
            return 0
        else:
            print("going down")
            temp = self.mystery(n-1)+1
            print("h(",n,") --> ",temp)
            return temp
#Tester
s = Surprise()
s.mystery(4)