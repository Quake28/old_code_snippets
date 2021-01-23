#inputs = open("inputs.txt","r")
#inputs = open("inputs - Copy.txt","r")
inputs = open("travel_restrictions_input (2).txt","r")
outputs = open("outputs.txt","w")
printer=""
s=""
for a in range(int(inputs.readline()[:-1])):
    printer+="Case #"+str(a+1)+": \n"
    n=int(inputs.readline()[:-1])
    list1=[]
    list2=[["N" for c in range(n)] for b in range(n)]
    for b in range(2):
        i=inputs.readline()[:-1]
        list1.append(list(i))
    for c in range(n):
        list2[c][c]="Y"
    for e in range(0,n-1):
        a=e
        for f in range(e+1,n):
            b=f
            status=False
            for g in range(0,f-e):
                if list1[1][e+g]=="Y" and list1[0][e+g+1]=="Y":
                    a=e
                    b=e+g+1
                    status=True
                else:
                    break
            if status:
                list2[a][b]="Y"
    for e in range(-1,-n-1,-1):
        a=e
        for f in range(e-1,-n-2,-1):
            b=f
            status=False
            for g in range(0,e-f-1):
                if list1[1][e-g]=="Y" and list1[0][e-g-1]=="Y":
                    a=e
                    b=e-g-1
                    status=True
                else:
                    break
            if status:
                list2[a][b]="Y"
    for z in range(len(list2)):
        printer+=s.join(list2[z])+"\n"
outputs.write(printer)
inputs.close()
outputs.close()
