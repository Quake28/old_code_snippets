n=int(input())
a=n
sum=0
while n>0:
    r=n%10
    sum=sum+r*r*r
    n=n/10
if a==sum:
    print("Armstrong Number")
else:
    print("It is not an Armstrong Number")
