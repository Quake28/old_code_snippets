clear all
close all
clc

% Different Function Definitions
f1 = inline('x.^5 + x + 1','x');
f2 = inline('exp(-x) - 1','x');
f3 = inline('3*x + sin(x) - exp(x)','x');
f4 = inline('x.^3 - 13.*x - 12','x');

%Defining the upper, lower boundary and the tolerance limit
xlower =-7;
xupper = 9;
tol = 10^(-4);

%Call the main bisection function which is in bisection.m
[r,i,e] = bisection(f4,xlower,xupper,tol)

%%Plot the function
x = -10:10;
y = f4(x);
plot(x,y)
grid on

