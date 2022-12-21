t = 0 : 0.001 : 80;
y1 = 10*sin(t*(15*2*pi/80));
y2 = 2*sin(t*(30*2*pi/80));

figure(1)
plot(t,y1,'red', 'LineWidth',1)
axis([0 80 -10 10])
xlabel('x/ms')
ylabel('y')
title('Task 4: Curve of 10*sin(15*t)')
legend('10*sin(15*t)')

figure(2)
plot(t,y2,'blue','LineWidth',1)
axis([0 80 -2 2])
xlabel('x/ms')
ylabel('y')
title('Task 4: Curve of 2*sin(30*t)')
legend('2*sin(30*t)')

figure(3)
plot(t,y1,'red',t,y2,'blue','LineWidth',1)
axis([0 80 -10 10])
xlabel('x/ms')
ylabel('y')
title('Task 4: Curve of 10*sin(15*t) and 2*sin(30*t)')
legend('10*sin(15*t)','2*sin(30*t)')

figure(4)
subplot(2,1,1)
plot(t,y1,'red', 'LineWidth',1)
axis([0 80 -10 10])
xlabel('x/ms')
ylabel('y')
title('Task 4: Curve of 10*sin(15*t)')
legend('10*sin(15*t)')

subplot(2,1,2)
plot(t,y2,'blue','LineWidth',1)
axis([0 80 -2 2])
xlabel('x/ms')
ylabel('y')
title('Task 4: Curve of 2*sin(30*t)')
legend('2*sin(30*t)')
grid

figure(5)
subplot(2,1,1)
stem(t,y1,'red', 'LineWidth',1)
axis([0 80 -10 10])
xlabel('x/ms')
ylabel('y')
title('Task 4: Curve of 10*sin(15*t)')
legend('10*sin(15*t)')

subplot(2,1,2)
stem(t,y2,'blue','LineWidth',1)
axis([0 80 -2 2])
xlabel('x/ms')
ylabel('y')
title('Task 4: Curve of 2*sin(30*t)')
legend('2*sin(30*t)')

