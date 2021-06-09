def smallest_dup_word(str):
    list1=str.split()
    list2=[]
    list3=[]
    for a in list1:
        status=True
        for b in range(len(list2)):
            if a == list2[b]:
                list3[b]+=1
                status=False
                break
        if status:
            list2.append(a)
            list3.append(1)
    #print(list1)
    #print(list2)
    #print(list3)
    returnVal=-1
    list4=[]
    for c in range(len(list3)):
        if list3[c]==2:
            list4.append(list2[c])
    print(list4)
    min=float("inf")
    for a in range(len(list4)):
        if ord(list4[a][0])<min:
            min=ord(list4[a][0])
            returnVal=list4[a]
    return returnVal
print(smallest_dup_word("ONE SIXTY ONE IS THE YEAR THE BOB MADE IS BOB BOB"))
print(smallest_dup_word("ONE SIXTY ONE IS THE YEAR THE BOB MADE IS BOB"))
print(smallest_dup_word("I CANNOT REALLY REMEMBER WHAT WAS THERE"))
print(smallest_dup_word(""))
