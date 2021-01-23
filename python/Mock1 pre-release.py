#Sorry guys, I was a bit too lazy for the validation stuff, if you want it, try it out yourselves
rejected=0
accepted=0
tweight=0
a="y"
while(a=="y"):
    l=int(input("Enter the length of the parcel (in cm) : "))
    b=int(input("Enter the breadth of the parcel (in cm) : "))
    w=int(input("Enter the width of the parcel (in cm) : "))
    weight=float(input("Enter the weight of the parcel (in Kgs) : "))
    if ((l>80)or(b>80)or(w>80)or((l+b+w)>200)or((weight>10)and(weight<1))):
        rejected+=1
        print("This parcel is rejected because -")
        if l>80:
            print("it's length is "+str(l-80)+"cm longer")
        if b>80:
            print("it's breadth is "+str(b-80)+"cm longer")
        if w>80:
            print("it's width is "+str(w-80)+"cm longer")
        if ((l+b+w)>200):
            print("the total of the three dimensions are "+str((l+b+w)-200)+" more")
        if (weight>10):
            print("the parcel is overweighted by "+str(weight-10)+"Kgs")
        elif (weight<1):
            print("the parcel is underweighted by "+str(1-weight)+"Kgs")
        continue
    else :
        accepted+=1
        tweight+=weight
        print("This parcel is accepted for delivery.")
        if weight>5:
            weight-=5
            while weight>0.1:
                weight-=0.1
                grams+=1
            cost=(10+(grams*0.1))
            print("The cost of delivering this parcel is $"+cost)
    a=str(input("Are there any more parcels left (y/n) :"))
print(accepted+" parcels are to be delivered.")
print(rejected+" parcels have been canceled for delivery.")
