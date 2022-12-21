function [root,iter,error] = secant_modified_multiple(f,xk,xkminus1,tol)

    iter = 1;
    while(1)
        u = f(xk) / forward_difference(f,xk,0.001,1,2);
        v = f(xkminus1) / forward_difference(f,xkminus1,0.001,1,2);
        xkplus1 = xk - (u*(xkminus1-xk))/(v - u);
        error = abs((xkplus1-xk)/xkplus1)*100;
        iter = iter + 1;
        if error < tol
            root = xkplus1;
            return
        end
        
        xk = xkminus1;
        xkminus1 = xkplus1; 
    end
end

