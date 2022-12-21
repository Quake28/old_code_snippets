function value = simpson_1_3(f,h)
    
    value = 0;
    n=1;
    while((n+2) <= length(f))
        value = value + (h/3)*(f(n) + 4*f(n+1) + f(n+2));
        n = n+2;
    end
end

