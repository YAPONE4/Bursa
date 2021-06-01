#include <iostream>
#include <time.h>
#include <ctime>

using namespace std;

void bubblesort(int *m, int n)
{
    int t;
    long long int count = 0;
    for(int i = 0; i < n; i++)
    {
        int d = 0;
        count++;
        for(int j = 0; j < n - 1; j++)
        {
            if (m[j] > m[j + 1])
            {
                d++;
                t = m[j];
                m[j] = m[j + 1];
                m[j + 1] = t;
                count += 4;
            }
            count++;
        }
        if (d == 0)
            break;
        count++;
    }
    cout << "Operations in function of bubblesort: " << count << endl;
}

void shakersort(int *m, int n)
{
    int LM = 0, RM = n - 1;
    int t;
    int f = 1;
    long long int count = 0;
    while ((LM < RM) && (f == 1))
    {
        int d = 0;
        count++;
        f = 0;
        for (int i = LM; i < RM; i++)
        {
            if (m[i] > m[i + 1])
            {
                d++;
                t = m[i];
                m[i] = m[i + 1];
                m[i + 1] = t;
                f = 1;
                count += 5;
            }
            count++;
        }
        RM--;
        for (int i = RM; i > LM; i--)
        {
            if (m[i] < m[i - 1])
            {
                d++;
                t = m[i];
                m[i] = m[i - 1];
                m[i - 1] = t;
                f = 1;
                count += 5;
            }
        }
        if (d == 0)
            break;
        count++;
        LM++;
    }
    cout << "Operations in function of shakersort: " << count << endl;
}

void mergesort(int *m1, int *m2, int *m3, int n)
{
    shakersort(m1, n / 2);
    shakersort(m2, n / 2);
    int i = n, j = n, c = 0;
    long long int count = 0;
    while (i != 0 && j != 0)
    {
        if (m1[n - i] < m2[n - j])
        {
            m3[c] = m1[n - i];
            i--;
            count += 2;
        }
        else
        {
            m3[c] = m2[n - j];
            j--;
        }
        c++;
        count += 2;
    }
    if (i == 0)
    {
        while (j != 0)
        {
            m3[c] = m2[n - j];
            j--;
            c++;
            count += 3;
        }
    }
    else
    {
        while (i != 0)
        {
            m3[c] = m1[ - i];
            i--;
            c++;
            count += 3;
        }
    }
    cout << "Operations in function of mergesort: " << count << endl;
}

void fillmass(int *m, int n)
{
    int num;
    for(int i = 0; i < n; i++)
    {
        cin >> num;
        m[i] = num;
    }
}

void fillrandommass(int *m, int n)
{
    srand (time(NULL));
    for (int i = 0; i < n; i++)
    {
        m[i] = rand() % 20 -10;
    }
}

void outmass(int *m, int n)
{
    for(int i = 0; i < n; i++)
        cout << i << ": " << m[i] << endl;
}
int main()
{
    float t1, t2;
    int *m1, *m2, *m3, *m4, *m5;
    int n;
    char c;
    cout << "Type number of elements: ";
    cin >> n;
    m1 = new int[n];
    m2 = new int[n];
    m3 = new int[n];
    m4 = new int[n / 2];
    m5 = new int[n / 2];
    cout << "Enter the type of filling (S: Self-Typed test; P: Multiple prepared tests + random): ";
    cin >> c;
    switch(c)
    {
        case 'S':
        {
            cout << "Type elements for m1" << endl << endl;
            fillmass(m1, n);
            cout << "Type elements for m2" << endl << endl;
            fillmass(m2, n);
            bubblesort(m1, n);
            shakersort(m2, n);
            cout << "Type elements for mergesort m4" << endl << endl;
            fillmass(m4, n / 2);
            cout << "Type elements for mergesort m5" << endl << endl;
            fillmass(m5, n / 2);
            mergesort(m4, m5, m3, n);
            cout << "M1 : " << endl << endl;
            outmass(m1, n);
            cout << endl << "M2 : " << endl << endl;
            outmass(m2, n);
            cout << endl << "M3 : " << endl << endl;
            outmass(m3, n);
            break;
        }
        case 'P':
        {
            cout << "Type the which situation you want to see (W - worst, B - best, R - Random): ";
            char c2;
            cin >> c2;
            switch(c2)
            {
                case 'W' :
                {
                    for (int i = 0; i < n; i++)
                    {
                        m1[i] = n - i;
                        m2[i] = n * 2 - i * 2;
                    }
                    for (int i = 0; i < n / 2; i++)
                    {
                        m4[i] = n - i;
                        m5[i] = n * 2 - i * 2;
                    }
                    t1 = clock();
                    bubblesort(m1, n);
                    t2 = clock();
                    cout << "Time: " << (t2 - t1) / 1000 << endl;
                    t1 = clock();
                    shakersort(m2, n);
                    t2 = clock();
                    cout << "Time: " << (t2 - t1) / 1000 << endl;
                    t1 = clock();
                    mergesort(m4, m5, m3, n / 2);
                    t2 = clock();
                    cout << "Time: " << (t2 - t1) / 1000 << endl;
                    break;
                }
                case 'B' :
                {
                    for (int i = 0; i < n; i++)
                    {
                        m1[i] = i;
                        m2[i] = i * 2;
                    }
                    for (int i = 0; i < n / 2; i++)
                    {
                        m4[i] = i;
                        m5[i] = i * 2;
                    }
                    t1 = clock();
                    bubblesort(m1, n);
                    t2 = clock();
                    cout << "Time: " << (t2 - t1) / 1000 << endl;
                    t1 = clock();
                    shakersort(m2, n);
                    t2 = clock();
                    cout << "Time: " << (t2 - t1) / 1000 << endl;
                    t1 = clock();
                    mergesort(m4, m5, m3, n / 2);
                    t2 = clock();
                    cout << "Time: " << (t2 - t1) / 1000 << endl;
                    break;
                }
                case 'R':
                {
                    fillrandommass(m1, n);
                    fillrandommass(m2, n);
                    fillrandommass(m4, n / 2);
                    fillrandommass(m5, n / 2);
                    t1 = clock();
                    bubblesort(m1, n);
                    t2 = clock();
                    cout << "Time: " << (t2 - t1) / 1000 << endl;
                    t1 = clock();
                    shakersort(m2, n);
                    t2 = clock();
                    cout << "Time: " << (t2 - t1) / 1000 << endl;
                    t1 = clock();
                    mergesort(m4, m5, m3, n / 2);
                    t2 = clock();
                    cout << "Time: " << (t2 - t1) / 1000 << endl;
                    break;
                }
                break;
            }
        }
    }
    return 0;
}
