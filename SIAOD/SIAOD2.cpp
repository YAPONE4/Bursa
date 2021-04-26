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

    temp->next = space; // elem->next = space;
    space->next = NULL;
    space->field = num;
    return(space);
}


void enter(List* elem, int n)
{
    int k;
    for (int i = 1; i < n; i++)
    {
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

struct List* sortv(List* L1, int n)
{
    struct List *t1, *t2, *t3;
	t1 = L1;
	for (int i = 0; i < n; i++)
	{   
        t2 = t1->next;
		for (int j = i; j < (n - 1); j++)
		{
			if (t1->field > t2->field)
			{
				t1->next = t2->next;
				t2->next = t1;
            }

		}
	}
    return(L1);
}

struct List* finding(List* L1, List* L2, List* L3, int n)
{
    struct List *t1, *t2, *L;
    t1 = L1;
    t2 = L2;
    L = L3;
    float t;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (t1->field == t2->field)
            {
                add(L, t1->field);
                t2 = t2->next;
                break;
            }
            t2 = t2->next;
        }
        t1 = t1->next;
        t2 = L2;
    }   
    return(L);
}


int main()
{
    List* L1, * L2, * L;
    int n;
    L = init(-1);
    cout << "Enter size of the lists: "; cin >> n; cout << endl;
    float frst, frst2;
    cout << "First list: ";
    cin >> frst;
    L1 = init(frst);
    enter(L1, n);
    L1 = sortv(L1, n);
    outp(L1);
    /*cout << endl << "Second list: ";
    cin >> frst2;
    L2 = init(frst2);
    enter(L2, n);
    cout << endl;
    L = finding(L1, L2, L, n);
    L = L->next;
    outp(L);*/
    return 0;
}