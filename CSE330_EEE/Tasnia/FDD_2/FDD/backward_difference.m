function value = backward_difference(f,x,h,o,i)
%f = derivative function
%x = the value at which the derivative has to be evaluated
%h = divided difference
%o = Order of the derivative
%i = takes the values either 1 or 2; 2 denotes more accurate results

    if(o == 1 && i == 1)
        value = (f(x)-f(x-h))/h;
    elseif(o == 1 && i == 2)
        value = (3*f(x) - 4*f(x-h) + f(x-2*h))/(2*h);
    elseif(o == 2 && i == 1)
        value = (f(x)-2*f(x-h)+f(x-2*h))/(h*h);
    elseif(o == 2 && i == 2)
        value = (2*f(x) - 5*f(x-h) + 4*f(x-2*h) - f(x-3*h))/(h^2);
    elseif(o == 3 && i == 1)
        value = (f(x) - 3*f(x-h) + 3*f(x-2*h) - f(x-3*h))/(h^3);
    elseif(o == 3 && i == 2)
        value = (5**f(x) - 18*f(x-h) + 24*f(x-2*h) - 14*f(x-3*h) + 3*f(x-4*h))/(2*(h^3));
    elseif(o == 4 && i == 1)
        value = (f(x) - 4*f(x-h) + 6*f(x-2*h) - 4*f(x-3*h) + f(x-4*h))/(h^4);
    elseif(o == 4 && i == 2)
        value = (3*f(x) - 14*f(x-h) + 26*f(x-2*h) - 24*f(x-3*h) + 11*f(x-4*h) - 2*f(x-5*h))/(h^4);
    end
        
end

