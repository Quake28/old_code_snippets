function geometric_series = geometric_series(r,n)
    sum_of_series = 0;
    for counter = 0:1:n
        sum_of_series = sum_of_series + r^counter;
    end
    disp(sum_of_series)
end