def powerN(m,n):
    if n == 0:
        return 1
    elif n < 0:
        return 1/powerN(m,-n)
    else:
        return m * powerN(m, n - 1)
#print(power(5,7))

def hocBuilder(height,floor=0):
    if height==0:
        return 0
    elif floor==0:
        return 3 + hocBuilder(height, floor+1)
    elif floor<height:
        return 5 + hocBuilder(height, floor+1)
    else:
        return 5
#print(hocBuilder(8))


def question5A(range,increment=0):
    if increment<range:
        increment+=1
        return iterationA2(increment) + "\n" + question5A(range,increment)
    else:
        return ""
    
def iterationA2(range,increment=1):
    if increment<range:
        return str(increment) + " " + iterationA2(range, increment+1)
    else:
        return str(increment)
#print(question5A(7))



def question5B(range,increment=0):
    if increment < range:
        increment += 1
        return iterantionB2(range, increment) + "\n" + patternB(range, increment)
    else:
        return ""
    
def iterantionB2(iter, range, increment=1):
    if increment == 1 :
        if range>1:
            return iterantionB3((iter-range)*2) + str(increment) + " " + iterantionB2(iter, range, increment + 1)
        else:
            return iterantionB3((iter-range)*2) + str(increment)
    elif increment<range:
        return str(increment) + " " + iterantionB2(iter, range, increment+1)
    else:
        return str(increment)
    
def iterantionB3(increment):
    if increment!=0:
        return iterantionB3(increment-1) + " "
    else:
        return ""
#print(patternB(9))


import resource, sys

class FinalQ:
    def print(self,investment,control):
        if(control<len(investment)):
            profit = self.calcProfit(investment[control])
            if control == 0:
                print("{}. Investment: {}; Profit: {}".format(control + 1, investment[control], profit) + "\n" + self.print(investment,control + 1))
            else:
                return "{}. Investment: {}; Profit: {}".format(control + 1, investment[control], profit) + "\n" + self.print(investment,control + 1)
        else:
            return ""

    def calcProfit(self,investment,count=0,percentage=4.5):
        investment-=investment%100
        if count==0:
            if investment>100000:
                x=investment-100000
                return float(self.calcProfit(75000,1,4.5)+self.calcProfit(x,1,8))
            else:
                return float(self.calcProfit(investment-25000,1))
        elif count<investment:
            return percentage+self.calcProfit(investment,count+100,percentage)
        else:
            return 0

resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

array=[25000,100000,250000,350000]
f = FinalQ()
f.print(array,0)