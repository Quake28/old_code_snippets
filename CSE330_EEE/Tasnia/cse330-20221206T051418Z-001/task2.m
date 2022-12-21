clc
clear all;
close all;
%Data to test linear log :
x= [1,2,3,4,5];
y= [.5,1.7,3.4,5.7,8];

%implement the linearize version
[a,b1]=linear_regression_using_log(x,y);
%Find the approximate values for the data points
s=  1: 0.1:5;
Y = b1*(s.^a);
%y = contains true function points
%Y= contains approximated function points using the regarding line

plot(s,Y,x,y,'*');
legend('Regression line','Data Point');