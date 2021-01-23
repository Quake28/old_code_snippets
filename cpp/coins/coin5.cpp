#include <iostream>
#include <conio.h>

using namespace std;

int main()
{
    cout<<"How many pennies do you have?";
    int pennies;
    cin>>pennies;


    cout<<"How many nickels do you have?";
    int nickels;
    cin>>nickels;


    cout<<"How many dimes do you have?";
    int dimes;
    cin>>dimes;


    cout<<"How many quarters do you have?";
    int quaters;
    cin>>quaters;


    int value=pennies+5*nickels+10*dimes+25*quaters;
    int dollar=value/100;
    int cents=value%100;

    cout<<"Total value = "<<dollar<<" dollar(s) and "<<cents<<" cents."<<endl;
    getch();
    return 0;
}
