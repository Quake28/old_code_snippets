clear all
close all
clc

f = @(x,y) exp(2*x - y);

n_x = 1000;%number of segments along the x-dimension
n_y = 1000;%number of segments along the y-dimension
type = 'simpson_3_8';%Newton_Cotes Formulas. options = 'trapezoid','simpson_1_3','simpson_3_8'.
x_lower = 0;
x_upper = 3;
y_lower = 0;
y_upper = 3;
del_x = (x_upper - x_lower)/n_x;%step size(segment width) along the x-direction
del_y = (y_upper - y_lower)/n_y;%step size(segment width) along the y-direction

numerical_integral_value = double_integral(f,x_lower,x_upper,y_lower,y_upper,del_x,del_y,type)%compute the double integral

matlab_original = integral2(f,x_lower,x_upper,y_lower,y_upper)%Compute the result using built-in function in MATLAB
error = abs(abs(matlab_original) - abs(numerical_integral_value));%Calculate the error with the matlab result to verify our program.
error_percentage = error / abs(matlab_original)* 100
