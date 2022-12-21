function [result_new, iter, percent_error] = bisection(f,xlower,xupper,tol)
    
    if (f(xlower)*f(xupper) >= 0)
        disp('Please change the boundary locations')
        return
    end
    iter = 1;
    result_old = 0;
    percent_error = Inf;
    
    ylower = f(xlower);
    xmid = (xlower+xupper)/2;%Bisection Formula
    ymid = f(xmid);
    result_new = xmid;
    percent_error = abs((result_new - result_old)/result_new * 100);
    
    
    while(1)
        result_old = result_new;
        if(percent_error > tol)
            iter = iter+ 1;
            if(ylower*ymid > 0)
                xlower = xmid;
            elseif(ylower*ymid < 0)
                xupper = xmid;
            else
                result_new = xmid;
                percent_error = abs((result_new - result_old)/result_new * 100);%Percent relative approximate error calculation
                return;
            end
            xmid = (xlower+xupper)/2;%Bisection Formula
            result_new = xmid;
            ymid = f(xmid);
            percent_error = abs((result_new - result_old)/result_new * 100);%Percent relative approximate error calculation
        else
            return
        end
    end
end

