#include <iostream>

using namespace std;

void bubblesort(int *m, int n)
{
    int t;
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n - 1; j++)
        {
            if (m[j] > m[j + 1])
            {
                t = m[j];
                m[j] = m[j + 1];
                m[j + 1] = t;
            }
        }
    }
}

void shakersort(int *m, int n)
{
    int LM = 0, RM = n - 1;
    int t;
    int f = 1;
    while ((LM < RM) && (f == 1))
    {
        f = 0;
        for (int i = LM; i < RM; i++)
        {
            if (m[i] > m[i + 1])
            {
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
                t = m[i];
                m[i] = m[i - 1];
                m[i - 1] = t;
                f = 1;
            }
        }
        LM++;
    }
}

void mergesort(int *m1, int *m2, int *m3, int n)
{
    int i = n, j = n, c = 0;
    while (i != 0 && j != 0)
    {
        if (m1[n - i] < m2[n - j])
        {
            m3[c] = m1[n - i];
            i--;
        }
        else
        {
            m3[c] = m2[n - j];
            j--;
        }
        c++;
    }
    if (i == 0)
    {
        while (j != 0)
        {
            m3[c] = m2[n - j];
            j--;
            c++;
        }
    }
    else
    {
        while (i != 0)
        {
            m3[c] = m1[n - i];
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
    m3 = new int[2 * n];
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
    outmass(m3, 2 * n);
    return 0;
}
