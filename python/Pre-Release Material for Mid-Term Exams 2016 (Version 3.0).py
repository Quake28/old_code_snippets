#This is the program I made myself
charityt=[0,0,0,0]
charityn=["","","",""]
print("Hello Manager!")
for a in range(1,4):
    charityn[a]=str(input("Please enter name for charity no."+str(a)+" : "))
print("\nTherefore,\nThe names of the charities are :")
for b in range(1,4):
    print(str(b)+"."+charityn[b])
print("You may enter -1 to see how much charity has been accumulated.")
print("\n")
while True:
    print("\n\n\n")
    for c in range(1,4):
        print(str(c)+"."+charityn[c])
    charity=str(input("\nHello costomer! \nPlease type in the number corresponding to the charity names to donate 1% of your bill  : "))
    while((charity!="1")and(charity!="2")and(charity!="3")and(charity!="-1")):
        charity=str(input("\nSorry costomer, \nYou have entered an invalid input, \nPlease re-enter the value properly : "))
    if(charity=="-1"):
        print("\n")
        control_1=[0,0,0,0]
        control_2=charityt
        max(control_2)
        print("\n1."+charityn[no1]+" recieved donations of Tk."+str(charityt[no1])+"\n2."+charityn[no2]+" recieved donations of Tk."+str(charityt[no2])+"\n3."+charityn[no3]+" recieved donations of Tk."+str(charityt[no3]))
        print("\nGRAND TOTAL DONATED TO CHARITY Tk."+str(charityt[1]+charityt[2]+charityt[3]))
        continue
    bill=str(input("\nPlease enter the bill amount (Tk.): "))
    while(bill.isnumeric()==False):
        bill=str(input("\nSorry costomer, \nYou have entered an invalid input, \nPlease re-enter the value properly : "))
    bill=int(bill)
    donatebill=bill/100
    if(charity=="1"):
        charityt[int(charity)]+=donatebill
    elif(charity=="2"):
        charityt[int(charity)]+=donatebill
    elif(charity=="3"):
        charityt[int(charity)]+=donatebill
