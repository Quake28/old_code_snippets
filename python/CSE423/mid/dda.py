x1=12
y1=55
x2=50
y2=81

g=(y2-y1)/(x2-x1)


xm=1
ym=1
if x2-x1<0:
    xm=-1
if y2-y1<0:
    ym=-1
xo=x1
yo=y1
ig=1/g
yc=yo
xc=xo
print("gradient",g)
for a in range(52):
    if g<=1:
        xo+=1
        xc=xo
        yo+=g
        yc=round(yo)
    else:
        yo+=1
        yc=yo
        xo+=ig
        xc=(round(xo))
    print(xc,yc)
