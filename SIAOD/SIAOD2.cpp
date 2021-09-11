#include <iostream>

using namespace std;

struct List
{
    float field;
    struct List* next;
};

struct List* init(float i)
{
    struct List* frst;
    frst = (struct List*)malloc(sizeof(struct List));
    frst->field = i;
    frst->next = NULL;
    return(frst);
}

struct List* add(List* elem, float num)
{
    struct List* temp, * space;
    space = (struct List*)malloc(sizeof(struct List));
    temp = elem;
    while (temp->next != 0)
    {
        temp = temp->next;
    }

    temp->next = space;
    space->next = NULL;
    space->field = num;
    return(space);
}


void enter(List* elem, int n)
{
    int k;
    for (int i = 1; i < n; i++) {
        cin >> k;
        add(elem, k);
    }
}

void outp(List* elem)
{
    struct List* temp;
    temp = elem;
    int counter = 1;
    do
    {
        cout << counter << ": " << temp->field << endl;
        temp = temp->next;
        counter++;
    } while (temp != NULL);
}

struct List* finding(List* L1, List* L2, List* L3)
{
    struct List* t1, * t2, * t3, * L;
    int c;
    t1 = L1;
    t2 = L2;
    L = L3;
    while (t1 != NULL)
    {
        while (t2 != NULL)
        {
            c = 0;
            if (t1->field == t2->field)
            {
                t3 = L;
                do
                {
                    if (t3->field == t1->field)
                    {
                        c = 1;
                        break;
                    }
                    t3 = t3->next;
                } while (t3 != NULL);
                if (c != 1)
                {
                    add(L, t1->field);
                    t2 = t2->next;
                    break;
                }
            }
            t2 = t2->next;
        }
        t1 = t1->next;
        t2 = L2;
    }
    return(L);
}

struct List* del_minus(List* L2)
{
    struct List* L0, * L, *prev;
    L0 = L2;
    L = L0;
    prev = NULL;
    do
    {
        if (L0->next->field < 0)
        {
            if (prev != NULL)
                prev->next = L0->next;
            else
                L = L0->next;
        }
        prev = L0;
        L0 = L0->next;
    } while (L0->next != NULL);
    return (L);
}

List* insert_odd(List* list, int value)
{
    List* start = list, * prev = nullptr;

    while (list != nullptr)
    {
        if (int(list->field) % 2 == 1)
        {
            List* newNode = new List;
            newNode->field = value;
            newNode->next = list;

            if (prev != nullptr)
                prev->next = newNode;

            if (list == start)
                start = newNode;
        }
        prev = list;
        list = list->next;
    }
    return start;
}

int main()
{
    List* L1, * L2, * L;
    int n, v;
    L = init(-1);
    cout << "Enter size of the lists: "; cin >> n; cout << endl;
    float frst, frst2;
    cout << "First list: ";
    cin >> frst;
    L1 = init(frst);
    enter(L1, n);
    cout << "Type num for insert_odd: ";
    cin >> v;
    L1 = insert_odd(L1, v);
    outp(L1);
    cout << endl << "Second list: ";
    cin >> frst2;
    L2 = init(frst2);
    enter(L2, n);
    L2 = del_minus(L2);
    outp(L2);
    cout << endl;
    L = finding(L1, L2, L);
    L = L->next;
    if (L != NULL)
        outp(L);
    else
        cout << "No matches!";
    return 0;
}