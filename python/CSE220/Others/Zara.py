'''
#TASK 1

num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
if num1>num2:
    print("First is greater")
elif num2>num1:
    print("Second is greater")
else:
    print("The numbers are equal")

#TASK 2
num1=int(input("Enter a number: "))
if (num1%2==0 or num1%5==0) and not (num1%2==0 and num1%5==0):
    print(num1)
elif num1%2==0 and num1%5==0:
    print("multiple of 2 and 5 both")

#TASK 3
num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
if num1<num2:
    temp=num1
    num1=num2
    num2=temp
    type="odd"
    if num1%2==0:
        type="even"
print(str(num1)+" is an "+type+" number which is greater than "+str(num2))

#TASK 4
marks=int(input("Enter marks: "))
if marks>=0 and marks<=100:
    if marks>=90:
        print("A")
    elif marks>=80:
        print("B")
    elif marks>=70:
        print("C")
    elif marks>=60:
        print("D")
    elif marks>=50:
        print("E")
    else:
        print("F")
else:
    print("Invalid marks")

#TASK 5
time=int(input("Enter time in seconds: "))
hours=int(time/60/60)
time=time%(60*60)
minutes=int(time/60)
seconds=time%60
print("Hours: "+str(hours)+", Minutes: "+str(minutes)+", Seconds: "+str(seconds))

#TASK 6
hours=int(input("Enter number of hours worked: "))
if hours<=40:
    salary=hours*200
else:
    salary=8000+((hours-40)*300)
print(salary)
'''