import math
def prime(x):
    if(x==2):
        return True
    elif(x==1):
        return False
    elif(x==0):
        return False
    else :
        for i in range(2,math.ceil(math.sqrt(x))+1):
            if(x%i!=0):
                break
            else:
                return False
        return True
def main():
    while(True):
        num=int(input("Enter a number:"))
        if(prime(num)):
            print("Congratulations!! ",num," is a prime number.")
        else:
            print("Sorry!! ",num," is not a prime number.")
main()
