count = 0

def partition (arr, left, mid, right):
    #creating temporary array based on mid index
    a = arr[left:mid]
    b = arr[mid:right]
    n1 = len(a)
    n2 = len(b)
    n = n1 + n2
    #Create c[1.. n]
    c = []
    #Initialize two indices i,j to point to a and b
    i=0
    j=0
    while  (i<n1) and (j<n2):
        maxVal=a[i]
        if a[i]<b[j]:
            maxVal=b[j]
            j+=1
        else:
            i+=1
        c.append(maxVal)
        count=count+1
    #Advance the index that points to the bigger one
    if i< n1:
        c+=a[i+1:]
    if j< n2:
        c+=b[j+1:]
    return c


def sorting(arr, left, right):
    if left >= right: 
        return arr
    mid = (left+right)/2
    arr = sorting(arr, left, mid)
    arr = sorting(arr, mid+1, right)
    arr = partition(arr, left, mid, right)
    return arr



# Driver program to test above functions 

arrInput = [7,22,38,47,52,59]
sorting(arrInput, 0, len(arrInput)-1)
print("Total no. of comparisons ", count)