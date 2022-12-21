function [root,iter,error] = secant_modified(f,xk,delta,tol)

    iter = 0;
    while(1)
        xkplus1 = xk - ((delta*xk*f(xk))/(f(xk+delta*xk)-f(xk)));
        error = abs((xkplus1-xk)/xkplus1)*100;
        iter = iter + 1;
        if error < tol
            root = xkplus1;
            return
        end
        X = [xk xkplus1];
        Y = [f(xk) 0];
        line(X,Y);
        
        xk = xkplus1;
    end
end

