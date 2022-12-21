clear all
close all
clc

%%%%%%%% Secant Method
f = inline('exp(x)+x','x');
figure;
s = -2:0.1:2;
y = f(s);
plot(s,y);
grid on;
hold on
xk = 2;
xkminus1 = 1.8;
tol=1E-2;
[root,iter,error] = secant_modified_multiple(f,xk,xkminus1,tol)
hold off


%%% Modified Secant Method
f = inline('exp(x)+x','x');
figure
s = -2:0.1:2;
y = f(s);
plot(s,y);
grid on;
hold on
xk = 2;
delta = 0;
tol=1E-2;
[root,iter,error] = secant(f,xk,delta,tol)
hold off