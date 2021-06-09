"""
1, 17, 22, 38, 5, 11
5

1, 5, 9, 15, 74
4

1, 5, 9, 13
5

"""
"""
['1', ' 17', ' 22', ' 38', ' 5', ' 11']
17, 22


['1', ' 5', ' 9', ' 15', ' 74']
1, 5

['1', ' 5', ' 9', ' 13']
Not Possible
"""



z=input()
y=int(input())
s=0
x=[]
for e in range(1,len(z)):
    if z[e]==",":
        x.append(z[s:e])
        e+=3
        s=e-1
x.append(z[s:e+1])
print(x)
status=False
for a in range(len(x)-1):
    for b in range(a, len(x)):
        if abs(int(x[a])-int(x[b]))==y:
            print(x[a]+", "+x[b])
            status=True
            break
    if status:
        break
if not status:
    print("Not Possible")