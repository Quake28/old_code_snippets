controlinput=0
input1=0
input2=0
input3=0
input4=0
answer=0
x="1"
print("1-Additions")
print("2-Subtraction")
print ("3-Multiplication")
print("4-Division")
print("Note : In case division and multiplication please do not enter any empty values ( like 0 ) until neccessary. Incase if you don't want a third or fourth value enter 1.")
while(x=="1"):
    controlinput=int(input("Enter the corresponding values for operations :"))
    input1=int(input("Enter first value :"))
    input2=int(input("Enter second value :"))
    input3=int(input("Enter third value :"))
    input4=int(input("Enter fourth value :"))
    if(controlinput==1):
        answer=input1+input2+input3+input4
        print("The total is :",answer)
    elif(controlinput==2):
        answer=input1-input2-input3-input4
        print("The total is :",answer)
    elif(controlinput==3):
        answer=input1*input2*input3*input4
        print("The product is :",answer)
    elif(controlinput==4):
        answer=input1/input2/input3/input4
        print("The product is :",answer)
    x=(input("Enter 1 to continue and 0 to end program :"))
    if(x=="0"):
        break
    elif (x!="0") and (x!="1"):
        while (x!="0") and (x!="1"):
            print("This is not a valid input.")
            x=(input("Enter 1 to continue and 0 to end program :"))
