#include <iostream>
#include <cstring>

using namespace std;

void paliIter(string m)
{
    int c = 0;
    for (int i = 0; i < m.length() / 2; i++)
        if (m[i] == m[m.length() - i - 1])
            c++;
        else
            break;
    if (c == m.length() / 2)
        cout << endl << "It's palindrom!";
    else
        cout << endl << "It's not palindrom!";
}

bool paliRec(string m, int start, int end)
{
    if (m[start] != m[end])
        return false;
    else
        if (start == end)
            return true;
        else
            return paliRec(m, start + 1, end - 1);
    return false;
}

struct Elem
{
    int field;
    struct Elem* next;
};

struct Elem* init(struct Elem* m, int el)
{
    m = new Elem;
    m->field = el;
    m->next = NULL;
    return m;
}

struct Elem* add(struct Elem* m, int el)
{
    struct Elem* newuz, * temp;
    newuz = new Elem;
    temp = new Elem;
    temp = m;
    while (temp->next != NULL)
    {
        temp = temp->next;
    }
    newuz->field = el;
    newuz->next = NULL;
    temp->next = newuz;
    return m;
}

struct Elem* delem(struct Elem* m, struct Elem* temp, int el, int c = 0)
{
    if (c == 0 && temp->field == el)
    {
        m = m->next;
        temp = m;
        return delem(m, temp, el);
    }
    else
    {
        if (temp->next == NULL)
            return m;
        else
        {
            c++;
            if (temp->next->field == el)
            {
                if (temp->next->next == NULL)
                {
                    temp->next = NULL;
                    return m;
                }
                temp->next = temp->next->next;
            }
            else
                temp = temp->next;
        }
    }
    return delem(m, temp, el, c);
}

void outp(struct Elem* m)
{
    do
    {
        cout << m->field << ' ';
        m = m->next;
    } while (m != NULL);
    cout << endl;
}

struct Elem* fillList(struct Elem* m, int n)
{
    n--;
    int k;
    for (int i = 0; i < n; i++)
    {
        cin >> k;
        add(m, k);
    }
    return m;
}

int main()
{
    char c;
    cout << "What algorithm you want to watch? (F - First, S - Second): ";
    cin >> c;
    switch(c)
    {
        case 'F':
        {
            cout << "Type which algorithm you want to use (I - iteration, R - recursive): ";
            cin >> c;
            switch(c)
            {
                case 'R':
                {
                    string m;
                    cout << "Type your string: ";
                    cin >> m;
                    if (paliRec(m, 0, m.length() - 1) == true)
                        cout << endl << "It's palindrom!";
                    else
                        cout << endl << "It's not palindrom!";
                    break;
                }
                case 'I':
                {
                    string m;
                    cout << "Type your string: ";
                    cin >> m;
                    paliIter(m);
                    break;
                }
            }
            break;
        }
        case 'S':
        {
            struct Elem* L;
            L = new Elem;
            int n, k, d;
            cout << "Type size of list: ";
            cin >> n;
            cout << "Type elements of list: ";
            cin >> k;
            L = init(L, k);
            L = fillList(L, n);
            cout << "Type element you want to delete: ";
            cin >> d;
            cout << endl << "Elements after deleting: ";
            L = delem(L, L, d);
            outp(L);
            break;
        }
    }
    return 0;
}