#include <iostream>
#include <fstream>

using namespace std;

string name;
char bell=7;

int main()
{
    cout<<"Please enter your name :";
    cin>>name;
    ofstream file ("file.txt");// can be merged to std::ofstream file("file.txt");
    file << "Hello "<<name<<bell<<" !\n";
    cout << "Hello "<<name<<" !\n";
    file.close();// is not necessary because the destructor closes the open file by default
    return 0;
}
