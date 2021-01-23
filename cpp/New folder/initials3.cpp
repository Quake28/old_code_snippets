#include<iostream>
#include<string>
#include<conio.h>

using namespace std;

int main()
{
    string start="";
    string in="";
    string first="";
    string second="";
    string third="";

    cout<<"Hello!! User."<<endl;
    cout<<"Do you want single letter initials or double letter initials?"<<endl;
    cin>>start;

    if(start=="single"||start=="SINGLE"||start=="Single"||start=="sINGLE"||start=="1")
    {
        cout<<"Do you have a middle name?"<<endl;
        cin>>in;

        if(in=="Yes"||in=="yES"||in=="YES"||in=="yes"||in=="y"||in=="Y")
        {
            cout<<"Enter your full name (First/Middle/Last)."<<endl;
            cin>>first>>second>>third;
            string initials=first.substr(0,1)+second.substr(0,1)+third.substr(0,1);
            cout<<"Your initials are "<<initials<<"."<<endl;
        }

        else if(in=="No"||in=="nO"||in=="NO"||in=="no"||in=="n"||in=="N")
        {
            cout<<"Enter your full name (First/Last)."<<endl;
            cin>>first>>third;
            string initials=first.substr(0,1)+third.substr(0,1);
            cout<<"Your initials are "<<initials<<"."<<endl;
        }
    }

    else if(start=="double"||start=="DOUBLE"||start=="Double"||start=="dOUBLE"||start=="2")
    {
        cout<<"Do you have a middle name?"<<endl;
        cin>>in;

        if(in=="Yes"||in=="yES"||in=="YES"||in=="yes"||in=="y"||in=="Y")
        {
            cout<<"Enter your full name (First/Middle/Last)."<<endl;
            cin>>first>>second>>third;
            string initials=first.substr(0,2)+second.substr(0,2)+third.substr(0,2);
            cout<<"Your initials are "<<initials<<"."<<endl;
        }

        else if(in=="No"||in=="nO"||in=="NO"||in=="no"||in=="n"||in=="N")
        {
            cout<<"Enter your full name (First/Last)."<<endl;
            cin>>first>>third;
            string initials=first.substr(0,2)+third.substr(0,2);
            cout<<"Your initials are "<<initials<<"."<<endl;
        }

    }

    getch();

    return 0;
}
