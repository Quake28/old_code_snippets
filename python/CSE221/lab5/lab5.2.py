"""
M W C A D B O E
D M W C A R O P

5
monkeys wearing coats are of
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
                    if x[i]!=d[-1] and i<=j:
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
    return d

def printer(x,y,z):
    print("   "+", ".join(x))
    for a in range(len(y)):
        print(y[a],z[a])
    print(" ",z[-1])

if __name__=="__main__":
    x=input().split()
    y=input().split()
    #print(x,y)
    z=lcs(x,y)
    print(len(z))
    #printer(x,y,z)
    list1={
        "A":"are",
        "B":"because",
        "C":"coats",
        "D":"doctors",
        "E":"evolution",
        "M":"monkeys",
        "O":"of",
        "P":"eruption",
        "R":"results",
        "W":"wearing"
        }
    for a in z:
        print(list1[a], end=" ")