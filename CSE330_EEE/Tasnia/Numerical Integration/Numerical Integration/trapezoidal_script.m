clear all
close all
clc

f1 = inline('cos(x)','x');
f2 = inline('(x.^2).*exp(-x)','x');
f3 = inline('x.*exp(-2*x.^2)','x');

a = 0;%Lower limit
b = 2;%Upper limit
n = 100;%number of segments
h = (b-a)/n;%Width of each segment

%Get the function values for each segment
Y = [];%Y contains the function values
for x=a:h:b
    Y = [Y, f3(x)];
end
%You can also input a tabulated data instead of a function.
integration_result = trapezoidal(Y,h)
