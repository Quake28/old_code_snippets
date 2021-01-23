def shiftLeft(source,k):
    for a in range(len(source)-k):
        source[a]=source[a+k]
    for b in range(k):
        source[a+b+1]=0
    print(source)
##shiftLeft([10,20,30,40,50,60],3)

def rotateLeft(source,k):
    list1=[0 for a in range(len(source))]
    for a in range(len(source)):
        list1[a-k]=source[a]
    print(list1)
#rotateLeft([10,20,30,40,50,60],3)
   
##[10,20,30,40,50,60]
##[ 0, 0, 0, 0, 0, 0]
##  0  1  2  3  4  5
## -6 -5 -4 -3 -2 -1
## 0-3, -3

def remove(source, size, idx):
    for a in range(idx,size):
        source[a]=source[a+1]
    print(source)
"""
def remove(source, size, idx):
    source.pop(idx)
    source.append(0)
    print(source)
"""
#remove([10,20,30,40,50,0,0],5,2)

def removeAll(source, size, element):
    while element in source:
        for b in range(size):
            if source[b]==element:
                for a in range(b,size):
                    source[a]=source[a+1]
    print(source) 
#removeAll([10,2,30,2,50,2,2,0,0],7,2)

def splitArray(source):
    for a in range(1,len(source)-1):
        part1=0
        part2=0
        for b in range(a):
            part1+=source[b]
        for c in range(a,len(source)):
            part2+=source[c]
        if part1==part2:
            status=True
            break
        else:
            status=False
    if status:
        print("true")
    else:
        print("false")
#splitArray([10, 3, 1, 2, 10])

def arraySeries(n):
    array1=[]
    d=0
    for a in range(n):
        for b in range(n,0,-1):
            array1.append(b)
        for c in range(n-a-1):
            array1[c+d]=0
        d+=n
    print(array1)
#arraySeries(4)
def maxBunchCount(source):
    current=source[0]
    count=0
    maxBunch=0
    for a in range(len(source)):
        if current==source[a]:
            count+=1
            if maxBunch<count:
                maxBunch=count
        else:
            current=source[a]
            count=1
    print(maxBunch)
#maxBunchCount([1,1,2,2,1,1,1,1])

def repitition(source):
    list1=[[],[]]
    for a in range(len(source)):
        if source[a] in list1[0]:
            for b in range(len(list1[0])):
                if list1[0][b]==source[a]:
                    list1[1][b]+=1
        else:
            list1[0].append(source[a])
            list1[1].append(1)
    for c in range(len(list1[1])):
        for d in range(c+1,len(list1[1])):
            if list1[1][c]>1 and list1[1][c]==list1[1][d]:
                status=True
                break
            else:
                status=False
        if status:
            break
    print(status)
#repitition([4,5,6,6,4,3,6,4])
#repitition([3,4,6,3,4,7,4,6,8,6,6])

def palindrome(source, size, index):
    curVal=size+index-len(source)-1
    list1=[]
    list2=[]
    list3=[]
    for a in range(curVal,curVal-size,-1):
        list1.append(source[a])
    for b in range(int(len(list1)/2)+1):
        list2.append(list1[b])
    for c in range(-1,0-(int(len(list1)/2)+2),-1):
        list3.append(list1[c])
    if list2==list3:
        print(True)
    else:
        print(False)
#palindrome([20,10,0,0,0,10,20,30],5,5)
#palindrome([10,20,0,0,0,10,20,30],5,5)

def intersection(source1, size1, index1,source2, size2, index2):
    list1=[]
    list2=[]
    list3=[]
    
    curVal1=size1+index1-len(source1)-1
    for a in range(curVal1-size1+1,curVal1+1):
        list1.append(source1[a])

    curVal2=size2+index2-len(source2)-1
    for b in range(curVal2-size2+1,curVal2+1):
        list2.append(source2[b])

    for c in list1:
        for d in list2:
            if c==d:
                list3.append(c)
    
    print(list3)

intersection([40,50,0,0,0,10,20,30],5,5,[10,20,5,0,0,0,0,0,55,40,15,25],7,8)
