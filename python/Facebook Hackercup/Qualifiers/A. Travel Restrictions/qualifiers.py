inputs = open("travel_restrictions_input.txt","r")
outputs = open("outputs.txt","w")
printer=""
s=""
for a in range(int(inputs.readline()[:-1])):
    printer+="Case #"+str(a+1)+": \n"
    n=int(inputs.readline()[:-1])
    list1=[]
    list2=[["" for c in range(n)] for b in range(n)]
    for b in range(2):
        i=inputs.readline()[:-1]
        list1.append(list(i))
    for d in range(n):
        for c in range(n):
            if c==d:
                list2[d][c]="Y"
            elif c+1==d or (c==d-n-1) or c-1==d:
                if list1[0][c]=="Y" and list1[1][d]=="Y":
                    list2[d][c]="Y"
                else:
                    list2[d][c]="N"
            else:
                list2[d][c]="N"
    for e in range(n):
        for f in range(n):
            if a>3 and e<f:
                if s.join(list1[0][e+1:f+1])=="Y"*(f-e):
                        if s.join(list1[1][e:f])=="Y"*(f-e):
                            list2[e][f]="Y"
            elif a>3 and f<e:
                if s.join(list1[1][f+1:e+1])=="Y"*(e-f):
                    if s.join(list1[0][f:e])=="Y"*(e-f):
                        list2[e][f]="Y"
    for g in range(len(list2)):
        printer+=s.join(list2[g])+"\n"
outputs.write(printer)
inputs.close()
outputs.close()
