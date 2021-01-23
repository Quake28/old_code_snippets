#include<iostream>
#include<string>
#include<fstream>
#include<conio.h>

using namespace std;

int main()
{
    string enter;
    cout<<"Type anything and press \"Enter\" to start the INFINITY LOOP!!\n";
    cin>>enter;

    ofstream file ("My own Infinity Loop.txt");

    while(true)
    {
        file<<enter<<endl;
        cout<<enter<<endl;
    }

    getch();
    return 0;
}
