def palindrome(x):
    if reverse(x.lower())==x.lower():
        return True
    else:
        return False
def reverse(x):
    if len(x)==0 or len(x)==0:
        return x
    return (x[len(x)-1]+reverse(x[0:len(x)-1]))
def main():
    x=str(input("Enter a word/phrase to check for Palindrome : "))
    if palindrome(x):
        print(x," is a Palindrome")
    else:
        print(x," is not a Palindrome")
    print("The reverse of ",x," is ",reverse(x),".")
main()
