function sum_y = double_integral(f,xl,xh,yl,yh,del_x,del_y,type)
    
    Y = [];
    sum_y = 0;
    if strcmp(type,'trapezoid')
        for j = yl:del_y:yh
            sum_x = ((f(xl,j)+f(xh,j))/2 + sum(f(xl+del_x:del_x:xh-del_x,j)))*del_x;
            Y = [Y sum_x];
        end

        sum_y = (Y(1)+Y(end)+2*sum(Y(2:end-1)))* (del_y/2);
    elseif strcmp(type,'simpson_1_3')
        for j = yl:del_y:yh
            value = 0;
            x_lower = xl;
            while((x_lower+2*del_x) <= xh)
                value = value + (del_x/3)*(f(x_lower,j) + 4*f(x_lower+del_x,j) + f(x_lower+2*del_x,j));
                x_lower = x_lower + 2*del_x;
            end
            Y = [Y value];
        end

        ind = 1;
        while((ind+2) <= length(Y))
            sum_y = sum_y + (del_y/3)*(Y(ind) + 4*Y(ind+1) + Y(ind+2));
            ind = ind + 2;
        end
    elseif strcmp(type,'simpson_3_8')
        for j = yl:del_y:yh
            value = 0;
            x_lower = xl;
            while((x_lower+3*del_x) <= xh)
                value = value + (3*del_x/8)*(f(x_lower,j) + 3*f(x_lower+del_x,j) + 3*f(x_lower+2*del_x,j) + f(x_lower+3*del_x,j));
                x_lower = x_lower + 3*del_x;
            end
            Y = [Y value];
        end

        ind = 1;
        while((ind+3) <= length(Y))
            sum_y = sum_y + (3*del_y/8)*(Y(ind) + 3*Y(ind+1) + 3*Y(ind+2) + Y(ind+3));
            ind = ind + 3;
        end
    end

end

