def arraySeries(n):
    #made a new array to store data, first of all, set the array size to n^2
    #traversed the array in groups of n, and then went for the n-th element to the 0-th element of that group to set the values from 1 to n
    list1=[]
    for x in range(n):
        for y in range(n):
            list1+=[0]
    for a in range(1,n+1):
        for b in range(1,a+1):
            list1[a*n-b]=b
    print(list1)
#arraySeries(4)

def repitition(source):
    list1=[]
    for a in range(len(source)):
        temp=source[a]
        source[a]=0
        if temp==0:
            continue
        list1.append(1)
        count=a+1
        while (temp in source) and (count<len(source)):
            if source[count]==temp:
                list1[-1]+=1
                source[count]=0
            count+=1
    for b in range(len(list1)-1):
        temp=list1[b]
        if temp>1:
            if temp in list1[b+1:len(list1)]:
                status=True
                break
            else:
                status=False
    print(status)
repitition([4,5,6,6,4,3,6,4])
repitition([3,4,6,3,4,7,4,6,8,6,6])
#Made an empty list, traversed the source list to find duplicates and note the individual counts in the list created previously. Traversed the new list to find instances where there were duplicate counts. If found, prints "True", else prints "False".
