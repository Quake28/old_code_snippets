a=0
b=0
for i in range (0,100):
    x=int(input("Enter temperature : "))
    if x>=20:
        a=a+1
    elif x<20:
        b=b+1
print("The number of days temperature was above 20C is ",a)
print("The number of days temperature was lower 20C is ",b)
