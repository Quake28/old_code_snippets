#####################################################################
#TASK 2
sum=0
for a in range(1,20,2):
    print(a)
    sum+=a
print("Sum is:",sum)
#####################################################################
#TASK 3
num=int(input())
for a in range(1,11):
    print(num*a)
#####################################################################
#TASK 4
for a in range(1,31):
    if a%5==0:
        print(a)
    elif a%7==0:
        print(a)
    #I didn't do anything more because there is no interference between multiples 5 and 7 until 35, and our limit is at 30
#####################################################################
#TASK 5
power=int(input())
num=1
for a in range(power):
    num*=10
print(num)
#####################################################################
#TASK 6
for a in range(2,8):
    print(8*a)
