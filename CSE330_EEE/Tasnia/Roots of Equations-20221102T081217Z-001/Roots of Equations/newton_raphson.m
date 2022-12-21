function [root, iter, error] = newton_raphson(f,x,tol)
    
    s = -10:0.1:10;
    y = f(s);
    plot(s,y);
    hold on
    
    old_root = x;
    root = x - (f(x)/forward_difference(f,x,0.001,1,2));
    error = abs(((root - old_root)/root)) * 100;
    X = [x root];
    Y = [f(x) 0];
    plot(X,Y)
    
    iter = 1;
    while(1)
        if(error > tol)
            x = root;
            old_root = root;
            iter =iter +1;
            root = x - (f(x)/forward_difference(f,x,0.0001,1,2));
            error = abs(((root - old_root)/root)) * 100;
            X = [x root];
            Y = [f(x) 0];
            plot(X,Y)
        else
            error = abs(((root - old_root)/root)) * 100;
            return
        end
    end
end

