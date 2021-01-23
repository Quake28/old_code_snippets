#include <iostream>
#include <fstream>
#include <string>
#include <conio.h>

using namespace std;

int main()
{
    int a=0;
    int b=0;
    int c=0;
    int d=0;
    int e=0;
    int f=0;
    int g=0;
    int h=0;
    int x=1;

    ofstream file ("Password 8 characters (0-9).txt");

    file<<h<<g<<f<<e<<d<<c<<b<<a<<endl;
    cout<<h<<g<<f<<e<<d<<c<<b<<a<<endl;

    while(h<10)
    {
        x=x+1;
        if((a>=0)and(a<9))
        {
            a=a+1;
        }
        else if(a==9)
        {
            a=a-9;
            b=b+1;
        }
        if(b==10)
        {
            b=b-10;
            c=c+1;
        }
        if(c==10)
        {
            c=c-10;
            d=d+1;
        }
        if(d==10)
        {
            d=d-10;
            e=e+1;
        }
        if(e==10)
        {
            e=e-10;
            f=f+1;
        }
        if(f==10)
        {
            f=f-10;
            g=g+1;
        }
        if(g==10)
        {
            g=g-10;
            h=h+1;
        }

        file<<h<<g<<f<<e<<d<<c<<b<<a<<endl;
        if(x%10000==0)
        {
            cout<<h<<g<<f<<e<<d<<c<<b<<a<<endl;
        }
    }

    getch();

    return 0;
}
