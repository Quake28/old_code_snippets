studentname=["0"]
test1=[0]
test2=[0]
test3=[0]
total=[0]
nettotal=0
for i in range (1,31):
    while True:
        studentnamevar=str(input("Please enter student no."+str(i)+"'s name : "))
        if studentnamevar.isalpha():
            studentname.append(str(studentnamevar))
            break
        print("Sorry User!!!\nThis is an invalid input.")
    while True:
        test1var=str(input("Please enter student no."+str(i)+"'s first test results : "))
        if test1var.isnumeric():
            if int(test1var)<=20:
                test1.append(int(test1var))
                break
        print("Sorry User!!!\nThis is an invalid input.")
    while True:
        test2var=str(input("Please enter student no."+str(i)+"'s second test results : "))
        if test2var.isnumeric():
            if int(test2var)<=25:
                test2.append(int(test2var))
                break
        print("Sorry User!!!\nThis is an invalid input.")
    while True:
        test3var=str(input("Please enter student no."+str(i)+"'s third test results : "))
        if test3var.isnumeric():
            if int(test3var)<=35:
                test3.append(int(test3var))
                break
        print("Sorry User!!!\nThis is an invalid input.")
    total.append(int(test1var)+int(test2var)+int(test3var))
    nettotal=nettotal+int(test1var)+int(test2var)+int(test3var)
classtotalavg=nettotal/i
for j in range(1,31):
    print("No."+str(j),studentname[j],"-",total[j])
print("Class average",classtotalavg)
highest=""
highestscore=0
for k in range(1,31):
    if total[k]==highestscore:
         highest=highest+", "+studentname[k]
    elif total[k]>highestscore:
        highest=studentname[k]
        highestscore=total[k]
print(highest,"has/have scored the highest in class with a total of",highestscore)
