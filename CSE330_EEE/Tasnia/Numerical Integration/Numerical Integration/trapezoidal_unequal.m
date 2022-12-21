function value = trapezoidal_unequal(x,y)

    value = 0;
    for i=1:length(x)-1
        h = x(i+1) - x(i);
        value = value + (h/2)*(y(i+1) + y(i));
    end
end

