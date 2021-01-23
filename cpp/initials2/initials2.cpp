#include<iostream>
#include<string>
#include<conio.h>

using namespace std;

int main()
{
    string first="";
    string second="";
    string third="";
    string fourth="";
    string fifth="";
    string sixth="";
    string in="";

    cout<<"Please enter the number of words you have in your name(2-6): ";
    cin>>in;

    if(in=="2"||in=="02"||in=="002"||in=="two"||in=="Two"||in=="tWO"||in=="TWO")
    {
        cout<<"Enter your full name: ";
        cin>>first>>second;
        string initials=first.substr(0,1)+second.substr(0,1);
        cout<<"Your initials are "<<initials<<"."<<endl;
    }

    else if(in=="3"||in=="03"||in=="003"||in=="three"||in=="Three"||in=="tHREE"||in=="THREE")
    {
        cout<<"Enter your full name: ";
        cin>>first>>second>>third;
        string initials=first.substr(0,1)+second.substr(0,1)+third.substr(0,1);
        cout<<"Your initials are "<<initials<<"."<<endl;
    }

    else if(in=="4"||in=="04"||in=="004"||in=="four"||in=="Four"||in=="fOUR"||in=="FOUR")
    {
        cout<<"Enter your full name: ";
        cin>>first>>second>>third>>fourth;
        string initials=first.substr(0,1)+second.substr(0,1)+third.substr(0,1)+fourth.substr(0,1);
        cout<<"Your initials are "<<initials<<"."<<endl;
    }

    else if(in=="5"||in=="05"||in=="005"||in=="five"||in=="Five"||in=="fIVE"||in=="FIVE")
    {
        cout<<"Enter your full name: ";
        cin>>first>>second>>third>>fourth>>fifth;
        string initials=first.substr(0,1)+second.substr(0,1)+third.substr(0,1)+fourth.substr(0,1)+fifth.substr(0,1);
        cout<<"Your initials are "<<initials<<"."<<endl;
    }

    else
    {
        cout<<"Enter your full name: ";
        cin>>first>>second>>third>>fourth>>fifth>>sixth;
        string initials=first.substr(0,1)+second.substr(0,1)+third.substr(0,1)+fourth.substr(0,1)+fifth.substr(0,1)+sixth.substr(0,1);
        cout<<"Your initials are "<<initials<<"."<<endl;
    }

    getch();

    return 0;
}
