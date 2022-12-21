function value = simpson_3_8(f,h)
    
    value = 0;
    n=1;
    while((n+3)<=length(f))
        value = value + (3*h/8)*(f(n) + 3*f(n+1) + 3*f(n+2) + f(n+3));
        n = n+3;
    end
end

