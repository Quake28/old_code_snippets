for a in range (0,5000):
    x=int(input("Input value house : $"))
    if x>200000:
        y=x*0.02
    elif x>100000:
        y=x*0.015
    elif x>50000:
        y=x*0.01
    print("You have to pay $" ,y," for tax.")
