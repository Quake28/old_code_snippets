function [root,iter,error] = secant(f,xk,xkminus1,tol)
    
    iter = 0;
    
    while(1)
        xkplus1 = xkminus1 - ((f(xkminus1)*(xk - xkminus1))/(f(xk) - f(xkminus1)));
        error = abs((xkplus1-xk)/xkplus1)*100;
        iter = iter + 1;
        if error < tol
            root = xkplus1;
            return
        end
        X = [xk xkplus1];
        Y = [f(xk) 0];
        line(X,Y);
        
        xk = xkminus1;
        xkminus1 = xkplus1;
        
        
    end
end

