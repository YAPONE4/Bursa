#include <iostream>

using namespace std;

void bubblesort(int *m, int n)
{
    int t;
    for(int i = 0; i < n; i++)
    {
        int d = 0;
        for(int j = 0; j < n - 1; j++)
        {
            if (m[j] > m[j + 1])
            {
                d++;
                t = m[j];
                m[j] = m[j + 1];
                m[j + 1] = t;
            }
        }
        if (d == 0)
            break;
    }
}

void shakersort(int *m, int n)
{
    int LM = 0, RM = n - 1;
    int t;
    int f = 1;
    while ((LM < RM) && (f == 1))
    {
        int d = 0;
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
            }
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
            }
        }
        if (d == 0)
            break;
        LM++;
    }
}

void mergesort(int *m1, int *m2, int *m3, int n)
{
    int i = n / 2, j = n / 2, c = 0;
    while (i != 0 && j != 0)
    {
        cout << m1[n / 2 - i] << ' ' << m2[n / 2 - j] << endl;
        if (m1[n / 2 - i] < m2[n / 2 - j])
        {
            m3[c] = m1[n / 2 - i];
            i--;
        }
        else
        {
            m3[c] = m2[n / 2 - j];
            j--;
        }
        c++;
    }
    if (i == 0)
    {
        while (j != 0)
        {
            m3[c] = m2[n / 2 - j];
            j--;
            c++;
        }
    }
    else
    {
        while (i != 0)
        {
            m3[c] = m1[n / 2 - i];
            i--;
            c++;
        }
    }
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

void outmass(int *m, int n)
{
    for(int i = 0; i < n; i++)
        cout << i << ": " << m[i] << endl;
}
int main()
{
    int *m1, *m2, *m3;
    int n;
    cout << "Type number of elements: ";
    cin >> n;
    m1 = new int[n];
    m2 = new int[n];
    m3 = new int[n];
    cout << "Type elements for m1" << endl << endl;
    fillmass(m1, n);
    cout << "Type elements for m2" << endl << endl;
    fillmass(m2, n);
    shakersort(m1, n);
    bubblesort(m2, n);
    mergesort(m1, m2, m3, n);
    cout << "M1 : " << endl << endl;
    outmass(m1, n);
    cout << endl << "M2 : " << endl << endl;
    outmass(m2, n);
    cout << endl << "M3 : " << endl << endl;
    outmass(m3, n);
    return 0;
}
