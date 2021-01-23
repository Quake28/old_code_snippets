#include<iostream>
#include<string>
#include<conio.h>

using namespace std;

int main()
{
    double income;
    double tax;

    cout<<"Please enter your income: ";
    cin>>income;

    cout<<"Please enter 's' for single or 'm' for married: ";
    string marital_status;
    cin>>marital_status;

    if(marital_status=="s")
    {
        if(income<=21450.00)
            tax=0.15*income;
        else if(income<=51900.00)
            tax=3217.50+0.25*(income-21450.00);
        else
            tax=11743.50+0.31*(income-51900.00);
    }

    else
    {
        if(income<=35800.00)
            tax=0.15*(income);
        else if(income<=865100.00)
            tax=5370.00+0.28*(income-35800.00);
        else
            tax=19566.00+0.31*(income-86500.00);
    }

    cout<<"The amount of tax you have to pay for is $"<<tax<<"."<<endl;

    getch();

    return 0;
}
