function repeater = task5(r,n)
    summation = 0;
    for a = 0:1:n
        summation = summation + r^a;
    end
    disp(summation)
end