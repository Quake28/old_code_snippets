 %This script is for  multiple linear regression for 2 independent
%vriables.This is certainly for visualizing the data in 3-D plot
clear all
close all
clc
tic

%x    =    multiple independent variable sample matrix each column of which is the values of a single independent variable
%y    =    sample values of the dependent variable
x = [1.7400    5.3000  10.8;
    6.3200    5.4200   9.4;
    6.2200    8.4100   7.2;
   10.5200    4.6300   8.5;
    1.1900   11.6000   9.4;
    1.2200    5.8500   9.9;
    4.1000    6.6200   8;
    6.3200    8.7200   9.1;
    4.0800    4.4200   8.7;
    4.1500    7.6000   9.2;
   10.1500    4.8300   9.4;
    1.7200    3.1200   7.6;
    1.7000    5.3000   8.2];
y = [25.5000   31.2000   25.9000   38.4000  ...
    18.4000   26.7000   26.4000   25.9000 ...
    32.0000   25.2000   39.7000   35.7000   26.5000];

n = 2;%Specify the number of independent variables
P = multiple_linear_regression(x,y,n);%P = Regression Cooefficients as b0,b1,b2,b3 etc in a single row
x1 = 1.1:0.5:11.7;%Sample data space


[M,N] = meshgrid(x1,x1);%Construct the 2-D independent variable space
Y = M*P(1,2) + N*P(1,3) + P(1,1);%Get the approximated function values using regression
surf(M,N,Y);%Plot the approximated results
hold on
stem3(x(:,1),x(:,2),y);%Stem plot of true data points
colormap jet
colorbar
lighting gouraud
title('Multiple Linear Regression')
xlabel('X1');
ylabel('X2');
zlabel('Y');
hold off;

toc