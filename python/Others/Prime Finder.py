import math
f=open('Prime numbers.txt','w')

def prime(x):
    for i in range(2,(math.ceil(math.sqrt(x))+1)):
        if(x%i==0):
            return False
    return True

def numbers(y):
    x=1
    while(True):
        if (prime(y)):
            x=x+1
            a=str(x)+". "+str(y)
            f.write(a+"\n")
            print(a)
        y=y+1

def main():
    num=2
    numbers(num)

main()
