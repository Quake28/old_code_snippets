function converter = task6(ti,tf)
    fprintf('celsius  | fahrenheit\n---------+------------\n')
    % fprintf('%f %f\n',ti,tf)
    for a = ti:1:tf
        fprintf('%f | %f\n', a ,a * ( 9 / 5 ) + 32)
    end
end