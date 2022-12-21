x1 = -2*pi : 0.1 : 2*pi;

y1 = 5*cos(x1.^2+1);
y2 = 8*sin(x1.^3-8);

plot(x1,y1,'red', x1,y2,'blue','LineWidth',0.5)
axis([-2*pi 2*pi -8 8])

xlabel('x')
ylabel('y')
title('Task 2: Curve of 5cos(x^2+1) and 8sin(x^3-8)')
legend('5cos(x^2+1)','8sin(x^3-8)')