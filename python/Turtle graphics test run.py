from turtle import *
color('blue', 'red')
begin_fill()
speed(5)
while True:
    circle(100,90)
    left(90)
    circle(50,180)
    left(90)
    fd(100)
    left(90)
    fd(100)
    left(90)
    if abs(pos())<1:
        break
end_fill()
done()
