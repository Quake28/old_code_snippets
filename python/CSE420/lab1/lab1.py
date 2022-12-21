file1=open("input.txt","r")
x=file1.read().split("\n")
for a in range(len(x)):
    y=x.pop(0)
    x+=y.split()
print(x)
arr=[[] for a in range(6)]
for a in x:
    len_a=len(a)
    try:
        if a.isnumeric():
