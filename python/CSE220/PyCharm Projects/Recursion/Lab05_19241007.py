class Node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next

def factorial(n):
    if n!=1:
        return n*factorial(n-1)
    else:
        return 1

def fibonacci(n,prev=0,curr=1):
    if n>1:
        return fibonacci(n-1,curr,prev+curr)
    else:
        return curr

def array(n,pos=0):
    if pos<len(n):
        return str(n[pos])+" "+array(n,pos+1)
    else:
        return ""

def binary(n,count=0):
    x="0"
    y="0"
    if n==0 and count==0:
        return "0"
    elif n==0:
        return ""
    if int(n)%2==1:
        x="1"
    if int(n)==n:
        return binary(int((n - n % 2) / 2), count+1) + x
    elif count==0:
        return binary(int((n - n % 2) / 2), count+1) + x + "." + binary(n-int(n), count+1)
    elif int(n)==0 and (n-int(n))!=0:
        if n-int(n)!=0:
            z=1 / (2 ** count)
            if z<=n:
                y="1"
                return y + binary(n-z,count+1)
            else:
                return y + binary(n,count+1)
    
def power(m,n):
    if n==0:
        return 1
    else:
        return m*power(m,n-1)

def addition(n):
    if n.next==None:
        return n.value
    else:
        return n.value+addition(n.next)

def reverse(n):
    if n.next == None:
        return str(n.value)
    else:
        return reverse(n.next) + "\n" + str(n.value)

###task1
##print(factorial(10))
###task2
##print(fibonacci(6))
###task3
print(array([1,2,3,4,5]))
###task4
###Literally tested all test cases this time
##print(binary(12.875))
##'''
##print(binary(1))
##print(binary(5))
##print(binary(64))
##print(binary(0))
##print(binary(0.875))
##print(binary(52.54))
###1100.11
##print(binary(12.12))
##'''
###                1100.00011110101110000101
### answer found = 1100.0001111010111000010100011110101110000101000111101
##
###task5
##print(power(5,4))
###task6
##z=Node(10,Node(20,Node(30,Node(40))))
##print(addition(z))
###task7
##print(reverse(z))
