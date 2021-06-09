/*
Basic plan for this
1. create 2d aray for chessboard,
2. set identifiers as strings, not int
    Self - 
        All other pieces - 10
        Knights - 11,12
    Opp -
        King – 21 
        Queen- 22 
        Rooks – 31, 32 
        Bishops – 41, 42 
        Knights - 51, 52 
        Pawns – (61 – 68)
3. Create linked list class with stack and queue pop methods, appending is the same for both 
4. History/Path will be in Stack, the next node lists will be in Queues, next node coords can be null or [-1,-1] to show it's inaccessible in some way
5. 2D array for storing result for all 12 opp pieces
6. Use recursive BFS to solve the problem
*/
#include <iostream>
#include <string>
#include <fstream>

using namespace std;

void showBoard(string board[8][8]);

int main()
{
    // creating chessboard (works like a charm)
    string chessboard[8][8];
    for (int a = 0; a < 8; a++)
    {
        for (int b = 0; b < 8; b++)
        {
            chessboard[a][b] = "__";
        }
    }
    //chessboard[0][1] = "11";
    //showBoard(chessboard);
    // using file input because I'm lazy
    ifstream inputFile;
    int whiteKnights[2][2] = {{-1, -1}, {-1, -1}};
    inputFile.open("input.txt");
    if (!inputFile)
    {
        cout << "No such file";
    }
    else
    {
        int temp, x = 0;
        int row, column;
        string piece;
        inputFile >> temp >> piece;
        while (x != temp)
        {
            inputFile >> row >> column;
            //cout << row << column << endl;
            whiteKnights[x][0] = row;
            whiteKnights[x][1] = column;
            chessboard[row][column] = piece + to_string(x + 1);
            x++;
        }
        x = 0;
        inputFile >> temp >> piece;
        while (x != temp)
        {
            inputFile >> row >> column;
            chessboard[row][column] = piece;
            x++;
        }
        x = 0;
        inputFile >> temp;
        while (x != temp)
        {
            inputFile >> row >> column >> piece;
            chessboard[row][column] = piece;
            x++;
        }

        inputFile.close();
    }
    showBoard(chessboard);
    return 0;
}

void showBoard(string board[8][8])
{
    cout << endl
         << "    ";
    for (int column = 0; column < 8; column++)
    {
        cout << column << "  ";
    }
    cout << endl;
    for (int row = 0; row < 8; row++)
    {
        cout << row << "  ";
        for (int column = 0; column < 8; column++)
        {
            cout << board[row][column] << " ";
        }
        cout << endl;
    }
}