# Question 7

def binary(x,y,start=0,end=None):
    if end==None:
        end=len(y)-1
    mid=int((start+end)/2)
    if y[mid]==x:
        while mid<len(y)-1:
            mid+=1
            if y[mid]>x:
                return mid
        return mid+1
    elif y[mid]<x and y[mid+1]>x:
        return mid+1
    elif y[mid]<x:
        return binary(x,y,mid+1,end)
    elif y[mid]>x:
        return binary(x,y,start,mid-1)
    
if __name__=="__main__":
    x=input().split()
    y=input().split()
    z=input().split()
    x=[int(a) for a in x]
    y=[int(a) for a in y]
    z=[int(a) for a in z]
    location=[]
    for a in range(x[1]):
        location.append(binary(z[a],y))
    for b in location:
        print(b,end=" ")
