id = [2 2 1 2 1 0 9 7];
y = [1 2 3 4 5 6 7 8];

element_mult = id.*y;
norm_mult = id*(y');
final_value = element_mult.*norm_mult;
root_fv = sqrt(final_value);
sz = size(element_mult);
p = root_fv.^id(end);
summation = 0;
for a = 1:1:length(p)
    summation = summation + p(a);
end
summation = summation + sz(2);

disp('id : ')
disp(id)
disp('element_mult : ')
disp(element_mult)
disp('norm_mult : ')
disp(norm_mult)
disp('final_value : ')
disp(final_value)
disp('root_fv : ')
disp(root_fv)
disp('sz : ')
disp(sz)
disp('p : ')
disp(p)
disp('summation : ')
disp(summation)