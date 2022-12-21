clc
clear all;
close all;
%Data to test linear log :
x= [50,50,50,70,70,70,80,80,80,90,90,90,100,100,100];
y= [3.3,2.8,2.9,2.3,2.6,2.1,2.5,2.9,2.4,3.0,3.1,2.8,3.3,3.5,3.0];

[a0,a1,a2]=second_order_regression(x,y);
s=  40: 0.1:110;
Y= a0+a1.*s +a2.*s.*s ;
[A1,A0]=linear_regression(x,y);
Y1=A0+A1.*s;

%plot the results
plot(s,Y,s,Y1,x,y,'*');
legend('Second order regression','Linear regression line ','Data Points');
title('Comparison between second order regression and Linear Regression');
