#include<iostream>
#include<numeric>
#include<string>
#include<sstream>


using namespace std;

int main()
{
    int num;
    cin.imbue ( locale() new numeric_only() );

    while (cin >> num)
    {
        cout << num << endl;
    }
    return 0;
}
