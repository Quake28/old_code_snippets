clear all
close all
clc

f1 = inline('cos(x)','x');
f2 = inline('(x.^2).*exp(-x)','x');
f3 = inline('x.*exp(-2*x.^2)','x');


%Randomly generate some data. You can input your own data here
x = sort(rand(1,100)*10);
%Get the function values for each segment
y = f3(x);%Y contains the function values

%You can also input a tabulated data instead of a function.
integration_result_trapezoid = trapezoidal_unequal(x,y)

