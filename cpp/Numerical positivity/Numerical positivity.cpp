#include <iostream>
#include <conio.h>

using namespace std;

int main()
{
    double n;
    cout<<"Please enter a number to determine if it is positive or negative.\nMake sure that the number is not \"0\" itself!!\n";
    cin>>n;

    while(n==0)
        if(n==0)
        {
            cout<<"Please re-enter any number other than \"0\" itself\n";
            cin>>n;
        }

    if(n>0)
    {
        cout<<n<<" is a positive number.\n";
    }
    else
    {
        cout<<n<<" is a negative number.\n";
    }

    getch();
    return 0;
}
