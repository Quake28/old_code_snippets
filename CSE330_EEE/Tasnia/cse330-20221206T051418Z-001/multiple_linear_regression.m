function B = multiple_linear_regression(x,y,n)
    %x    =    multiple independent variable sample matrix each column of
    %          which is the values of a single variable
    %y    =    sample values of the dependent variable
    %n    =    number of independent variables
    %B    =    Regression Cooefficients as b0,b1,b2,b3 etc in a single row
    X = zeros(n+1,n+1);
    X(1,1) = length(x(:,1));
    
    for i = 2:n+1 % diagonal elements
        X(i,i) = x(:,i-1)' * (x(:,i-1)); % or, X(i,i) = sum(x(:,i-1) .* x(:,i-1))
    end
    
    for i = 1:n+1
        if(i == 1) % first column
            for j = i+1:n+1
                X(j,i) = sum(x(:,j-1));
            end
        elseif i>1 % all others except the first row
            for j = i+1:n+1
                X(j,i) = (x(:,i-1))' * (x(:,j-1)); % or, X(j,i) = sum(x(:,i-1) .* x(:,j-1))
            end
        end
    end

    % need to make the other elements of the first row
    X1 = X';
    for i = 1:n+1
        X1(i,i) = 0;
    end
    
    final_X = X + X1;
    
    Y = zeros(n+1,1);
    Y(1,1) = sum(y(:));
    for j = 2:n+1
        Y(j) = y(1,:) * x(:,j-1);
    end
    
    B = inv(final_X)*Y;
    B = B';
end

