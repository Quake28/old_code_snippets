import time
def ISBN13(x):
    #Splitting the string into single integer variables
    #The module does not care about removing the check digit so the entire ISBN-13 code can be sent to this module without any problems
    a=int(x[0])
    b=int(x[1])
    c=int(x[2])
    d=int(x[3])
    e=int(x[4])
    f=int(x[5])
    g=int(x[6])
    h=int(x[7])
    i=int(x[8])
    j=int(x[9])
    k=int(x[10])
    l=int(x[11])
    #Returning calculated check digit of ISBN-13 in integer form
    returnvalue=str(10-(((a+c+e+g+i+k)+(3*(b+d+f+h+j+l)))%10))
    if returnvalue=="10":
        return "0"
    else:
        return returnvalue

def ISBN13check(x):
    #Returns true if the ISBN13's calculated check digit value matches the check digit value entered by user, else returns false
    if ISBN13(x)==(x[12]):
        return True
    else:
        return False
    
def valid(x):
    #This module decides if the ISBN-13 is usable by the program
    if numbers(x):
        #The part below checks if the length is acceptable by the program
        if len(x)==12:
            return True
        elif len(x)==13:
            return True
        else:
            return False
    else:
        return False
    
    
def numbers(x):
    #This module checks that the user's input is all numeric or not
    if x.isnumeric():
        return True
    else:
        return False

def main():
    print("Hello, User!")
    print("This is a special program to determine the check digit of an ISBN13 code.")
    print("The program will automatically determine what you want to do.")
    print("To start with,")
    while True:
        #This is the primary loop used to restart the entire procedure as per user's consent
        #x is the variable used for taking an input of the ISBN-13 code as a string value
        x=str(input("Enter the ISBN13 code (you do not have to enter the hyphens):"))
        while True:
            #Here the program repeatedly reminds the user of a wrong input
            if valid(x):
                break
            else:
                print("Sorry User!")
                print("This is not a valid input.")
                x=str(input("Please re-enter correct ISBN13 : "))
        #y is used to print the check digit of the ISBN13 code in string form
        y=ISBN13(x)
        if len(x)==12:
            #The program prints these messages if the ISBN-13 code entered by the user is without the check digit
            #The message first shows the check digit only, later the entire ISBN-13 code is printed along with the correct check digit
            print("The check digit of",x," is",y,".")
            print("Resulting in :",x+y,".")
        elif len(x)==13:
            #Here the program checks if the check digit entered by the user in the ISBN-13 code is valid or not
            if ISBN13check(x):
                print("This ISBN13 code is correct.")
            else:
                #As the program does not have the entire book library,
                #So it assumes that the check digit is wrong and prints the correct check digit(assuming the first 12 charecters entered are correct) for the user
                print("This ISBN13 code is wrong.")
                print("If you have the check digit wrong then the correct check digit will be",y,".")
                print("Resulting in",x[0:12]+y)
        #a over here is the control variable
        a=str(input("Do you want to continue?(y/n) :"))
        #If someone enters "yes" or "y" even with common upper or lower case mistakes the program understands that the user wants to continue
        #Anything other than the strings mentioned  in the "if" line will be taken as negative
        if (a=="y")or(a=="yes")or(a=="Yes")or(a=="yES")or(a=="Y"):
            continue
        else:
            #The program's primary loop is broken with a message to user
            print("Thank you User for using this program.")
            break
    #The small time delay so that the user can read the last message printed
    time.sleep(1.5)
main()
