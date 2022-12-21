function temperature_converter = temperature_converter(ti,tf)
    for counter = ti:1:tf
        celsius(counter - ti + 1) = counter;
    end
    fahrenheit = celsius.* ( 9 / 5 ) + 32;
    disp(celsius)
    disp(fahrenheit)
    celsius(2:2,1:tf-ti+1) = fahrenheit;
    disp('   celsius,  fahrenheit')
    disp(celsius')
end