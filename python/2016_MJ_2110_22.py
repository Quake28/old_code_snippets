def gsvalidation(x):
    if (x<49.9):
        return (49.9-x)
    elif (x>50.1):
        return (50.1-x)
    else:
        return True
def cvalidation(x):
    if (x<24.9):
        return (24.9-x)
    elif (x>25.1):
        return (25.1-x)
    else:
        return True
def orders():
    print("Warning! Do not enter any random value even by accident, this may cause the program to crash! So be careful about what you type.")
    order=int(input("Hello Manager!\nHow many orders do you have today?(Numeric only) : "))
    completed=0
    #Was too tired for any kind of validation/verification, whatever it is.............
    while (order!=completed):
        csacks=int(input("Enter the number of sacks of cement required for order no."+str(completed+1)+" (Numeric only) : "))
        _csacks=csacks
        wcsacks=0
        rcsacks=0
        gsacks=int(input("Enter the number of sacks of gravel required for order no."+str(completed+1)+" (Numeric only) : "))
        _gsacks=gsacks
        wgsacks=0
        rgsacks=0
        ssacks=int(input("Enter the number of sacks of sand required for order no."+str(completed+1)+" (Numeric only) : "))
        _ssacks=ssacks
        wssacks=0
        rssacks=0
        while (csacks!=0):
            sackweight=float(input("Please enter the weight of the sack of cement(in Kgs) (Numeric only) :"))
            if (cvalidation(sackweight)!=True):
               print("Sorry Manager!\nBut this sack of Cement is rejected.")
               if (cvalidation(sackweight)>0):
                   print("The sack of cement is "+str(cvalidation(sackweight))+"Kgs underweighted.")
               elif (cvalidation(sackweight)<0):
                   print("The sack of cement is "+str(cvalidation(sackweight)*-1)+"Kgs overweighted.")
               rcsacks+=1
            else:
                print("This sack has ben accepted for delivery, it is a "+str(sackweight)+"Kgs sack of Cement.")
                wcsacks+=sackweight
                csacks-=1
        print(str(rcsacks)+" sacks of Cement have been rejected.")
        while (gsacks!=0):
            sackweight=float(input("Please enter the weight of the sack of Gravel(in Kgs) (Numeric only) :"))
            if (gsvalidation(sackweight)!=True):
               print("Sorry Manager!\nBut this sack of Gravel is rejected.")
               if (gsvalidation(sackweight)>0):
                   print("The sack of Gravel is "+str(gsvalidation(sackweight))+"Kgs underweighted.")
               elif (gsvalidation(sackweight)<0):
                   print("The sack of Gravel is "+str(gsvalidation(sackweight)*-1)+"Kgs overweighted.")
               rgsacks+=1
            else:
               print("This sack has ben accepted for delivery, it is a "+str(sackweight)+"Kgs sack of Gravel.")
               wgsacks+=sackweight
               gsacks-=1
        print(str(rcsacks)+" sacks of Gravel have been rejected.")
        while (ssacks!=0):
            sackweight=float(input("Please enter the weight of the sack of Sand(in Kgs) (Numeric only) :"))
            if (gsvalidation(sackweight)!=True):
               print("Sorry Manager!\nBut this sack of Sand is rejected.")
               if (gsvalidation(sackweight)>0):
                   print("The sack of Sand is "+str(gsvalidation(sackweight))+"Kgs underweighted.")
               elif (cvalidation(sackweight)<0):
                   print("The sack of Sand is "+str(gsvalidation(sackweight)*-1)+"Kgs overweighted.")
               rssacks+=1
            else:
               print("This sack has ben accepted for delivery, it is a "+str(sackweight)+"Kgs sack of Sand.")
               wssacks+=sackweight
               ssacks-=1
        print(str(rcsacks)+" sacks of Sand have been rejected.")
        print("This order has : ")
        
        completed+=1
        
orders()
