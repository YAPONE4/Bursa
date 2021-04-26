#include <iostream>

using namespace std;

int sch;

string ispali_iter(string str)
{
    int counter = 0;
    for (int i = 0; i < str.size() / 2; i++)
    {
        if (str[i] == str[str.size() - 1 - i])
            counter++;
        sch++;
    }
    if (counter == str.size() / 2)
        return "String is palindrom";
    else
        return "String is not palindrom";
    sch++;
}

string ispali_recur(string str, int start = 0)
{
    int counter = str.size() - start;
    if (start == str.size() / 2)
    {
        return "String is palindrom";
    }
    sch++;
    if (str[start] == str[counter - 1])
        return ispali_recur(str, start + 1);
    else
        return "String is not palindrom";
    sch++;
}

int main()
{
    string str;
    char c;
    cout << "Type your string: ";
    cin >> str;
    cout << "Type the checking method (Iteration - I/Recursion - R): ";
    cin >> c;
    switch(c)
    {
        case 'I' :
            cout << ispali_iter(str) << endl << sch;
        case 'R' :
            cout << ispali_recur(str) << endl << sch;
    }
    return 0;
}