charity = list()
charity_total = [0,0,0]
for i in range (3):
    charity.append(input("Enter name of Charity:"))
carry_on = True

while(carry_on):
    print("Names of Charities:")
    for i in range (3):
        
        print(i+1,".",charity[i])

    choice = int(input("From the list of charities, Enter the the number of corresponding Charity:"))
    if not (choice == 1 or choice == 2 or choice == 3 or choice == -1):
        print("Not a valid option.")
    else:
        if(choice == -1):
            for i in range (3):
                print("Total donation for", charity[i],"is",charity_total[i])
        else:
            
            value = float(input("Enter the value of customer's shopping bill:"))        
            donation = value * 0.01
            if(choice == 1):
                charity_total[0] = charity_total[0] + donation
            if(choice == 2):
                charity_total[1] = charity_total[1] + donation
            if(choice == 3):
                charity_total[2] = charity_total[2] + donation
        
    exit_op = input("Is this your last entry? (Y/N)")
    if (exit_op == "Y" or exit_op == "y"):
        carry_on = False
if (charity_total[0] == max(charity_total)):
    if (charity_total[1] > charity_total[2]):
        print(charity[0],"has a total donation of",charity_total[0])
        print(charity[1],"has a total donation of",charity_total[1])
        print(charity[2],"has a total donation of",charity_total[2])
    else:
        print(charity[0],"has a total donation of",charity_total[0])
        print(charity[2],"has a total donation of",charity_total[2])
        print(charity[1],"has a total donation of",charity_total[1])

if (charity_total[1] == max(charity_total)):
    if (charity_total[0] > charity_total[2]):
        print(charity[1],"has a total donation of",charity_total[1])
        print(charity[0],"has a total donation of",charity_total[0])
        print(charity[2],"has a total donation of",charity_total[2])
    else:
        print(charity[1],"has a total donation of",charity_total[1])
        print(charity[2],"has a total donation of",charity_total[2])
        print(charity[0],"has a total donation of",charity_total[0])
        
if (charity_total[2] == max(charity_total)):
    if (charity_total[1] > charity_total[0]):
        print(charity[2],"has a total donation of",charity_total[2])
        print(charity[1],"has a total donation of",charity_total[1])
        print(charity[0],"has a total donation of",charity_total[0])
    else:
        print(charity[2],"has a total donation of",charity_total[2])
        print(charity[0],"has a total donation of",charity_total[0])
        print(charity[1],"has a total donation of",charity_total[1])

grand_total = charity_total[0]+charity_total[1]+charity_total[2]
print("GRAND TOTAL DONATED TO CHARITY:",grand_total)
