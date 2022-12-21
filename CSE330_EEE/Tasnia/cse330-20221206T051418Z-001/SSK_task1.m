clc
clear all;
close all;
%Define  the data :
x= [1,2,3,4,5,6,7];
y= [.5,2.5,2.0,4,3.5,6,5.5];

%Implementing simple least square Linear Regression:
[a1,a0]= linear_regression(x,y);
%For Loop Different Approach
s=  1: 0.1:20;
Y= a0+a1.*s;

plot(s,Y,x,y,'*');
legend('Regression line','Data Point');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%Data to test linear log:
%Define  the data :
x= [1,2,3,4,5];
y= [.5,1.7,3.4,5.7,8];


%y = contains true function points
%Y= contains approximated function points using the regarding line

%implement the linearize version
[a,b1]=linear_regression_using_log(x,y);
%Find the approximate values for the data points

for i = 1: 0.1:20
    c= a0+a1*i;
        c=b1*(i^a);
    Y=[Y c];
end

Y = b1*(s.^a);

plot(s,Y,x,y,'*');
legend('Regression line','Data Point');