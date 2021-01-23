string=str(input("Please enter a string to be reversed :"))
def reverse(x):
    if len(x)==0 or len(x)==0:
        return x
    return (x[len(x)-1]+reverse(x[0:len(x)-1]))
print(reverse(string))
