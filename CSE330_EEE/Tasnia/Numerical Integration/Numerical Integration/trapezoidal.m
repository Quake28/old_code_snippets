function value = trapezoidal(f,h)

    value = (((f(1) + f(end))/2) + sum(f(2:end-1)))*h;

end

