inputs=open("alchemy_validation_input.txt","r")
outputs=open("output.txt","w")
printer=""
for a in range(int(inputs.readline()[:-1])):
    n=int(inputs.readline()[:-1])
    safe="Y"
    list1=list(inputs.readline()[:-1])
    s=0
    while ((len(list1)!=1) and (safe=="Y")):
        for b in range(s,len(list1)-2):
            if list1[b:b+3].count("A")==1:
                list1[b]="B"
                list1=list1[:b+1]+list1[b+3:]
                s=b-1
                break
            elif list1[b:b+3].count("A")==2:
                list1[b]="A"
                list1=list1[:b+1]+list1[b+3:]
                s=b-1
                break
        if (list1.count("A")==len(list1)) or (list1.count("B")==len(list1)) :
            safe="N"
    printer+="Case #"+str(a+1)+": "+safe+"\n"
outputs.write(printer)
inputs.close()
outputs.close()
