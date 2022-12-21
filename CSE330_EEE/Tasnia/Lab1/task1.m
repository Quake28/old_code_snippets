x1 = -pi : 0.5 : pi;
y1 = sin(x1);

x2 = -pi : 0.1 : pi;
y2 = sin(x2);

x3 = -pi : 0.01 : pi;
y3 = sin(x3);

plot(x1,y1,'red', x2,y2,'green', x3,y3,'blue', 'LineWidth',0.5)
axis([-pi pi -1 1])

ylabel('y')
xlabel('x')
title('Task 1: Curve of Sin(x)')
legend('sin(x) 1','sin(x) 2','sin(x) 3')
