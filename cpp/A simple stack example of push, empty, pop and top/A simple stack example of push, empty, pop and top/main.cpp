#include <iostream>
#include <stack>
#include<conio.h>

using namespace std;

int main()
{
    stack<char> stackObject;
    stackObject.push('A');
    stackObject.push('B');
    stackObject.push('C');
    stackObject.push('D');
    while(!stackObject.empty())
    {
        cout << "Popping: ";
        cout << stackObject.top() << endl;
        stackObject.pop();
     }
getch();
return 0;
}
