def recursion(x):
    if x==1 or x==0:
        return 1
    else:
        y=x*(recursion(x-1))
        return y

def main():
    number=int(input("Enter a number : "))
    print("The factorial of ",number," is ",recursion(number),".")

main()
