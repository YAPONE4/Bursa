#include <iostream>
#include <ctime>

using namespace std;

void sortv(int *m, int n)
{
    int t;
    int min;
    int count = 0;
    for (int i = 0; i < n; i++)
    {
        min = i;
        for (int j = i; j < n; j++)
        {
            if (m[min] > m[j])
            {
                min = j;
                count++;
            }
            count++;
        }
        t = m[min];
        m[min] = m[i];
        m[i] = t;
        count++;
    }
    cout << endl << "Operations: " << count << endl;
}

void sorto(int* m, int n)
{
    int t;
    int count = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < (n - 1); j++)
        {
            if (m[j] > m[j + 1])
            {
                t = m[j];
                m[j] = m[j + 1];
                m[j + 1] = t;
                count++;
            }
            count++;
        }
    }
    cout << endl << "Operations: " << count << endl;
}

void outp(int* m, int n)
{
    cout << "Your array: " << endl;
    for (int i = 0; i < n; i++)
    {
        cout << m[i] << ' ';
    }
}

void fillm(int* m, int n)
{
    cout << "Fill your array: " << endl;
    for (int i = 0; i < n; i++)
    {
        cin >> m[i];
    }
}

void fillr(int *m, int n)
{
    srand(time(NULL));
    for (int i = 0; i < n; i++)
    {
        m[i] = rand() % 200 -100;
    }
}

void fillb(int *m, int n)
{
    srand(time(NULL));
    for (int i = 0; i < n; i++)
    {
        m[i] = i;
    }
}

void fillw(int *m, int n)
{
    srand(time(NULL));
    for (int i = 0; i < n; i++)
    {
        m[i] = n - i;
    }
}

int main()
{
    int* m, n;
    float t1, t2;
    cout << "Type size of your array: ";
    cin >> n;
    m = new int[n];
    char c;
    cout << "How do you want to fill array? (R - Random; S - Self-Typed; W - worst; B - best): ";
    cin >> c;
    switch(c)
    {
        case 'S':
        {
            fillm(m, n);
            break;
        }
        case 'R':
        {
            fillr(m, n);
            break;
        }
        case 'W':
        {
            fillw(m, n);
            break;
        }
        case 'B':
        {
            fillb(m, n);
            break;
        }
    }
    cout << "Which type of sort do you want? Obmen/Vibor (O/V)? : ";
    cin >> c;
    switch (c)
    {
        case 'O' :
        {
            t1 = clock();
            sorto(m, n);
            t2 = clock();
            cout << endl << "Executing time: " << (t2 - t1) / 1000;
            break;
        }
        case 'V' :
        {
            t1 = clock();
            sortv(m, n);
            t2 = clock();
            cout << endl << "Executing time: " << (t2 - t1) / 1000;
            break;
        }
        default:
        {
            cout << endl << "ERROR";
            break;
        }
    }
    cout << endl << endl << "Do you want to reveal new array? (Y/N): ";
    cin >> c;
    if (c == 'Y')
        outp(m, n);
    return(0);
}