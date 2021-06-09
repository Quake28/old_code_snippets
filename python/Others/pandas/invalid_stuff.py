list1 = [[1, 7, 48, 99],[1, None, 48, 99],[1, 7, 48,None],[1, 7, 48, 99],[None, 7, 48, 99],[1, 7, 48, None],[None, 7, None, 99],[1, None, 48, None],[1, 7, 48, 99],]
# A*B/C +D
for a in range(len(list1)):
    total=1
    if(list1[a][0]==None):
        pass
    elif(list1[a][0]<=0):
        pass
    else:
        total*=list1[a][0]
    if (list1[a][1]==None):
        pass
    elif(list1[a][1]<=0):
        pass
    else:
        total*=list1[a][1]
    if(list1[a][2]==None):
        pass
    elif(list1[a][2]<=0):
        pass
    else:
        total/=list1[a][2]
    if(list1[a][3]==None):
        pass
    else:
        total+=list1[a][3]
        
    print(round(total,2))