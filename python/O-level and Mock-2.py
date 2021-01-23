#
#
####TASK@1####
#
#
interested=(int(input("Enter the number of senior citizens interested in the outing : ")))
while ((interested<10)or(interested>36)):
    interested=int(input("This is an invalid input.\nPlease re-enter the number of senior citizens interested in the outing : "))
if ((interested>9) and (interested<15)):
    cost=14+21
    costestimate=((interested+2)*cost+150)
elif ((interested>14) and (interested<25)):
    cost=13.5+20
    costestimate=((interested+2)*cost+190)
elif ((interested>24) and (interested<36)):
    cost=13+19
    costestimate=((interested+3)*cost+225)
costperhead=costestimate/interested
print("Estimated cost per head is $"+str(costperhead)+".")
#
#
####TASK@2####
#
#
if interested<=14:
    maxpeople=14
elif interested<=24:
    maxpeople=24
elif interested<=36:
    maxpeople=36
seniorcitizen=[""]*interested
for a in range (0,interested):
    seniorcitizen[a]=str(input("Enter the name of senior citizen no."+str(a+1)+" : "))
extra=int(input("Enter the number of extra people that have arrived (you only have space for "+str(maxpeople-len(seniorcitizen))+" extra people) : "))
while((extra<0)or(extra>(maxpeople-len(seniorcitizen)))):
    extra=int(input("This is an invalid input,\nPlease re-enter the number of extra people that have arrived (you only have space for "+str(maxpeople-len(seniorcitizen))+" extra people) : "))
extrapeople=[""]*extra
if len(extrapeople)>0:
    for b in range(0,len(extrapeople)):
        extrapeople[b]=str(input("Enter the name of extra person no."+str(b+1)+" : "))
totalpaid=(len(extrapeople)+len(seniorcitizen))*costperhead
print("Total amount recieved = $"+str(totalpaid))
for c in range(0,len(seniorcitizen)):
    print(str(c+1)+". "+seniorcitizen[c])
for d in range(0,len(extrapeople)):
    print(str(c+d+2)+". "+extrapeople[d])
#
#
####TASK@3####
#
#
if costestimate==totalpaid:
    print("This outing has borken even.")
elif costestimate<totalpaid:
    print("This outing has made a profit of $"+str(totalpaid-costestimate-(cost*extra))+".")
##.........The End.........##
