#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <conio.h>


using namespace std;

int main()
{
    char a=48;
    char b=48;
    char c=48;
    char d=48;
    char e=48;
    char f=48;
    char g=48;
    char h=48;
    char n;

    ofstream file ("Password 8 characters (0-9).txt");

    cout<<"Hello user!!"<<endl<<"Do you want to start?(Y/N)"<<endl;
    cin>>n;

    if(n==89||n==121)
    {
        file<<h<<g<<f<<e<<d<<c<<b<<a<<endl;
        cout<<h<<g<<f<<e<<d<<c<<b<<a<<endl;
        while((n==89||n==121)and(a<=57)and(b<=58)and(c<=58)and(d<=58)and(e<=58)and(f<=58)and(g<=58)and(h<=58)and(a>=48)and(b>=48)and(c>=48)and(d>=48)and(e>=48)and(f>=48)and(g>=48)and(h>=48))
        {
            if((a>=48)and(a<57))
            {
                a=a+1;
            }
            else if(a==57)
            {
                a=a-9;
                b=b+1;
            }
            if(b==58)
            {
                b=b-10;
                c=c+1;
            }
            if(c==58)
            {
                c=c-10;
                d=d+1;
            }
            if(d==58)
            {
                d=d-10;
                e=e+1;
            }
            if(e==58)
            {
                e=e-10;
                f=f+1;
            }
            if(f==58)
            {
                f=f-10;
                g=g+1;
            }
            if(g==58)
            {
                if((h==48)||(h==49)||(h==50)||(h==51)||(h==52)||(h==53)||(h==54)||(h==55)||(h==56)||(h==57))
                {
                    cout<<"Do you want to continue?(Y/N)"<<endl;
                    cin>>n;
                    if(n==89||n==121)
                    {
                        g=g-10;
                        h=h+1;
                    }
                    else if((n==78)||(n==110))
                    {
                        cout<<"Thank for using this program!"<<endl<<endl;
                        return 0;
                    }
                }
            }
            file<<h<<g<<f<<e<<d<<c<<b<<a<<endl;
            cout<<h<<g<<f<<e<<d<<c<<b<<a<<endl;
        }
    }
    else if(n!=89||n!=121)
    {
        cout<<"Thank for using this program!"<<endl<<endl;
        return 0;
    }
    getch();

    return 0;
}
