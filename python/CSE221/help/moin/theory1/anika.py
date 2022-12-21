f1=open("input.txt", "r")
inx=f1.readline()
arr1= f1.readline().split()
arr1=[int(a) for a in arr1]  
arr2= f1.readline().split()
arr2=[int(a) for a in arr2] 
f1.close()
def searching(arr1, search, end, start=0):
    mid=(start+end)/2
    mid=int(mid) 
    
    if arr1[mid] == search:
        count=0
        for i in range(mid+1, len(arr1)):
            if arr1[i]==arr1[mid]:
                count+=1
            else:
                break 
        return mid+count+1 
    elif mid==len(arr1)-1 and arr1[mid]<search:
        return mid+1
        
    elif arr1[mid]<search and arr1[mid+1]>search:
        return mid+1
    elif arr1[mid]>search:
        if mid==0:
            return 0
        return searching(arr1, search, mid-1,start)
    elif arr1[mid]<search:
        return searching(arr1, search, end, mid+1)
    else:
        return mid+1
f2=open("output.txt", "w") 
y=[searching(arr1, a, len(arr1)) for a in arr2]
print(y) 
for item in y:
    f2.write(str(item)+" ")
f2.close()