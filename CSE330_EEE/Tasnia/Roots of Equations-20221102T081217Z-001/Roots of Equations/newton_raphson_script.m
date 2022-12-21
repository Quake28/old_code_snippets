clear all
close all
clc

% Different Function Definitions
f1 = inline('x.^5 + x + 1','x');
f2 = inline('exp(-x) - 1','x');
f3 = inline('3*x + sin(x) - exp(x)','x');
f4 = inline('x.^3 - 13.*x - 12','x');

%Defining the starting point and the tolerance limit
x_start = 50;
tol = 0.001;%Tolerance is given in percent

%Call the main newton-raphson function which is in newton_raphson.m
[root,iteration,percent_error] = newton_raphson(f4,x_start,tol)

%%Plot the function
x = -10:50;
y = f4(x);
plot(x,y)
grid on

