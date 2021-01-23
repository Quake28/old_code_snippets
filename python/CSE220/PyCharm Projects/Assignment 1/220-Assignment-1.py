def shiftLeft(source, k):
    for a in range(len(source)-k):
        source[a]=source[a+k]
    for b in range(k+1,len(source)):
        source[b]=0
    print(source)
    
def rotateLeft(source,k):
    temp=source[:k]
    for a in range(len(source)-k):
        source[a]=source[a+k]
    length=len(source)
    for b in range(k):
        source.pop(length-k)
    source+=temp
    print(source)

def remove(source, size, idx):
    for b in range(idx+size-1,idx-1,-1):
        source.pop(b)
        source.append(0)
    print(source)

def removeAll(source,size,element):
    while element in source:
        for a in range(size):
            if source[a]==element:
                source.pop(a)
                source.append(0)
                break
    print(source)

def splitArray(a):
    panLeft=a[:int(len(a)/2)]
    panRight=a[int(len(a)/2):]
    totalLeft=0
    totalRight=0
    for x in panLeft:
        totalLeft+=x
    for y in panRight:
        totalRight+=y
    if totalRight==totalLeft:
        print("true")
    else:
        print("false")

def series(n):
    final=[]
    temp=[0 for a in range(n)]
    for b in range(1,n+2):
        for c in range(b):
            temp[-c]=c
        final+=temp
    print(final)

def bunch(z):
    a=0
    while a<len(z):
        temp=z[a]
        maxCount=1
        while a<len(z)-1:
            if temp==z[a+1]:
                maxCount+=1
                a+=1
                continue
            else:
                break
        a+=1
    print(maxCount)

def repitition(z):
    list1=[]
    a=0
    b=0
    while a<len(z):
        list1.append([z[a],1])
        while a<len(z)-1:
            if list1[b][0]==z[a+1]:
                list1[b][1]+=1
                a+=1
                continue
            else:
                break
        a+=1
        b+=1
    
    status=False
    for c in range(1,len(list1)):
        temp=list1[c][1]
        for d in range(c,len(list1)):
            if temp==list1[d][1]:
                status=True
        if status:
            break
    print(status)
import math
def palindrome(list1,start,size):
    count=start
    list2=[]
    list3=[]
    while count<start+int(size/2):
        c=0
        if count+c>len(list1):
            c-=len(list1)
        list2.append(list1[count+c])
        count+=1
    count+=int(math.ceil(size/2))
    if count>len(list1):
        count-=len(list1)+1
    c=0
    while c<int(size/2):
        list3.append(list1[count-c])
        c+=1
    #print(list1,list2,list3)
    if list2==list3:
        print(True)
    else:
        print(False)

def intersection(list1,start1,size1,list2,start2,size2):
    list3=[]
    count1=start1
    while count1<start1+size1:
        c1=0
        if count1>=len(list1):
            c1=0-len(list1)
        count2=start2
        while count2<start2+size2:
            c2=0
            if count2>=len(list2):
                c2=0-len(list2)
            if (list1[count1+c1]==list2[count2+c2]) and (list1[count1+c1] not in list3):
                list3.append(list1[count1+c1])
            count2+=1
        count1+=1
    print(list3)


shiftLeft([10,20,30,40,50,60], 3)
rotateLeft([10,20,30,40,50,60],3)
remove([10,20,30,40,50,0,0], 5, 2)
removeAll([10,2,30,2,50,2,2,0,0],7,2)
splitArray([1, 1, 1, 2, 1])
series(2)
bunch([1, 2, 2, 3, 4, 4, 4])
repitition([4,5,6,6,4,3,6,4])
palindrome([10,20,0,0,0,10,20,30],5,5)
intersection( [40,50,0,0,0,10,20,30],5,5,[10,20,5,0,0,0,0,0,55,40,15,25],8,7)
