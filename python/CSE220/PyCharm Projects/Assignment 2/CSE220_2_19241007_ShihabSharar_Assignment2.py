#######################################################################################################################
#Question 1
def powerN(m,n):
    if n == 0:
        return 1
    elif n < 0:
        return 1/powerN(m,-n)
    else:
        return m * powerN(m, n - 1)
#print(power(3,-2))
#######################################################################################################################
#Question 3
def hocBuilder(height,count=0):
    if height==0:
        return 0
    elif count==0:
        return 3 + hocBuilder(height, count+1)
    elif count<height:
        return 5 + hocBuilder(height, count+1)
    else:
        return 5
#print(hocBuilder(4))
#######################################################################################################################
#Question 5 - (a)
def patternA(length,count=0):
    if count<length:
        count+=1
        return subLoopA1(count) + "\n" + patternA(length,count)
    else:
        return ""
def subLoopA1(length,count=1):
    if count<length:
        return str(count) + " " + subLoopA1(length, count+1)
    else:
        return str(count)
#print(patternA(5))
#######################################################################################################################
#Question 5 - (b)
def patternB(length,count=0):
    if count < length:
        count += 1
        return subLoopB1(length, count) + "\n" + patternB(length, count)
    else:
        return ""
def subLoopB1(loop, length, count=1):
    if count == 1 :
        if length>1:
            return subLoopB2((loop-length)*2) + str(count) + " " + subLoopB1(loop, length, count + 1)
        else:
            return subLoopB2((loop-length)*2) + str(count)
    elif count<length:
        return str(count) + " " + subLoopB1(loop, length, count+1)
    else:
        return str(count)
def subLoopB2(count):
    if count!=0:
        return subLoopB2(count-1) + " "
    else:
        return ""
#print(patternB(5))
#######################################################################################################################
#Question 6
class FinalQ:
    def print(self,array,idx):
        if(idx<len(array)):
            profit = self.calcProfit(array[idx])
            if idx == 0:
                print("{}. Investment: {}; Profit: {}".format(idx + 1, array[idx], profit) + "\n" + self.print(array,idx + 1))
            else:
                return "{}. Investment: {}; Profit: {}".format(idx + 1, array[idx], profit) + "\n" + self.print(array,idx + 1)
        else:
            return ""

    def calcProfit(self,investment,curr=0,profit=4.5,increment=100):
        investment-=investment%100
        if curr==0:
            if investment>100000:
                x=investment-100000
                return float(self.calcProfit(75000,1,45,1000)+self.calcProfit(x,1,800,10000)+self.calcProfit(x%10000,1,8))
            else:
                return float(self.calcProfit(investment-25000,1))
        elif curr<investment:
            return profit+self.calcProfit(investment,curr+increment,profit,increment)
        else:
            return 0

# Tester
array=[25000,100000,250000,350000,10010000]
# Last input is for limit testing, and is the highest value this algorithm can take in
# I could just remove the limit, that would allow me to enter higher values, but it's completely unnecessary because the values I can reach is already pretty high.
f = FinalQ()
f.print(array,0)

# Expected -
# 1. Investment: 25000; Profit: 0.0
# 2. Investment: 100000; Profit: 3375.0
# 3. Investment: 250000; Profit: 15375.0
# 4. Investment: 350000; Profit: 23375.0

# Result -
# 1. Investment: 25000; Profit: 0.0
# 2. Investment: 100000; Profit: 3375.0
# 3. Investment: 250000; Profit: 15375.0
# 4. Investment: 350000; Profit: 23375.0
