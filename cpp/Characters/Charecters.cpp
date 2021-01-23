#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <conio.h>

using namespace std;

int main()
{
    char a=32;
    int n=1;

    ofstream file ("Characters.txt");

    file<<n<<"."<<a<<endl;
    cout<<n<<"."<<a<<endl;

    while((n<1000)and(a>=32)and(a<=126))
    {
        if((a>=32)and(a<126))
        {
            a=a+1;
        }
        else if(a==126)
        {
            a=a-95;
            a=a+1;
        }

        n=n+1;

        file<<n<<"."<<a<<endl;
        cout<<n<<"."<<a<<endl;

    }

    getch();

    return 0;
}
