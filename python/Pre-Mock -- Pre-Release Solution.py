day=[]
night=[]
a=1
totalday=0
totalnight=0
highday=-98
lownight=68
while a<=30 :
    while True :
        tempday=float(input("Enter the midday temperature for day "+str(a)+" :"))
        if ((tempday>-98)and(tempday<68)):
            break
        else :
            print("Sorry, this temperature is out of range.")
            continue
    while True :
        tempnight=float(input("Enter the midnight temperature for day "+str(a)+" :"))
        if ((tempnight>-98)and(tempnight<68)):
            break
        else :
            print("Sorry, this temperature is out of range.")
            continue
    day.append(tempday)
    night.append(tempnight)
    totalday+=tempday
    totalnight+=tempnight
    a+=1
dayavg=totalday/30
nightavg=totalnight/30
print("The Average tempratures for this month are :")
print("1. Midday - "+str(dayavg))
print("2. Midnight - "+str(nightavg))
for b in range(0,30):
    if day[b]>highday :
        highday=b
    if night[b]<lownight :
        lownight=b
print("The highest midday temperature for this month was in day "+str(highday+1)+" reaching "+str(day[highday]))
print("The lowest midnight temperature for this month was in day "+str(lownight+1)+" reaching "+str(night[lownight]))
