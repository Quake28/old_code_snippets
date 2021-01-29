import time
x="1"
while x=="1":
    marks=int(input("Enter mark:"))
    if marks>100:
        while (marks>100):
            print("This is not a valid input.")
            marks=int(input("Please re-enter marks:"))
    if marks==100:
        print("Wonderful!!! You recieved full marks.")
    elif marks>=90:
        print("You got an A*. Excellent!!!")
    elif marks>=80:
        print("You got an A. Well done!!")
    elif marks>=70:
        print("You got an B. Better luck next time!")
    elif marks>=60:
        print("You got an C. Barely passed; Better luck next time!!")
    elif marks>=50:
        print("You got an D. You just failed!!")
    elif marks>=40:
        print("You got an E. Try Harder!!!!")
    else:
        print ("You got a U!!!!!You're purely worthless!!!!!!")
    x=(input("Enter 1 to continue and 0 to end program:"))
    if(x=="0"):
        break
    elif (x!="0") and (x!="1"):
        while (x!="0") and (x!="1"):
            print("This is not a valid input.")
            x=(input("Enter 1 to continue and 0 to end program:"))
