def main():
    x=int(input("Enter a number : "))
    while x!=0:
        if error(x):
            n=(x * x)/(1-x)
            print("n =",n,",x =",x)
        x=int(input("Enter a number : "))

def error(x):
    if x==1:
        return False
    else:
        return True

main()
