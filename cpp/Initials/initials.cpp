#include<iostream>
#include<string>
#include<conio.h>

using namespace std;

int main()
{
    string first="";
    string middle="";
    string last="";
    string initials="";

    cout<<"Enter your full name(first,middle,last)";
    cin>>first>>middle>>last;
    if(last=="")
       {
          string initials=first.substr(0,1)+middle.substr(0,1);
          cout<<"Your initials are "<<initials<<"."<<endl;
       }
    else
       {
          string initials=first.substr(0,1)+middle.substr(0,1)+last.substr(0,1);
          cout<<"Your initials are "<<initials<<"."<<endl;
       }

    getch();

    return 0;
}
