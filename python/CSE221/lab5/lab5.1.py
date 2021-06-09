"""
length(x,y)
    m=len(x)
    n=len(y)
    a=1
    b=1
    for a in range(1,m):
        c[i][0]=0
    for b in range(1,n):
        c[0][j]=0
    for c in range(1,m):
        for d in range(1,n):
            if x_i==y_j:
                c[i][j]=c[i-1][j-1]+1
                b[i][j]=NW
            elif c[i-1][j]>= c[i][j-1]:
                c[i][j]=c[i-1][j]
                b[i][j]=N
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = W
"""

"""
A B C D G H
A E D F H R

3

A B C
A C

2

C D E F G A B C
C E F D A B G A C

CEFABC
75% PASSED
"""

def lcs(x,y):
    m=len(x)
    n=len(y)
    c=[[None for aa in range(m+1)] for ab in range(n+1)]
    d=""
    for i in range(0,m+1):
        c[0][i]=0
    for j in range(1,n+1):
        c[j][0]=0
    #printer(x,y,c)
    #print(len(c[0]),len(c),m,n)
    #try:
    for i in range(m):
        for j in range(n):
            #print("i",i,x[i], end=" ")
            #print("j",j,y[j])
            #printer(x,y,c)
            if x[i]==y[j]:
                c[j+1][i+1]=c[j][i]+1
                #print(x[i])
                if len(d)!=0:
                    if x[i]!=d[-1] and i>=j:
                        d+=x[i]
                else:
                    d+=x[i]
                #b[i][j]= "NW"
            elif c[j][i+1] >= c[j+1][i]:
                c[j+1][i+1]=c[j][i+1]
                #b[i][j]= "N"
            else:
                c[j+1][i+1] = c[j+1][i]
                #b[i][j] = "W"
    #except:
    #    printer(x,y,c)
    return c,d

def printer(x,y,z):
    print("   "+", ".join(x))
    for a in range(len(y)):
        print(y[a],z[a])
    print(" ",z[-1])

if __name__=="__main__":
    x=input().split()
    y=input().split()
    #print(x,y)
    z,z1=lcs(x,y)
    print(z1)
    """
    printer(x,y,z)
    string1=""
    prev=0
    for a in range(len(z[-1])):
        if z[-1][a]!=prev:
            prev=z[-1][a]
            string1+=x[a-1]
    print(string1)
    """
    print(str(int(z[-1][-1]/len(x)*100))+"% PASSED")