#include <iostream>

using namespace std;

struct List
{
    int field;
    struct List* next;
};

struct List* add_elem(List* L, int m)
{
    struct List* t1;
    t1->field = m;
    t1->next = L;
    return(t1);
}

struct List* del_iter(List* L, int n, int m)
{
    struct List* t1, tp;
    t1 = L;
    for(int i = 0; i < n; i++)
    {
        if (t1->field = m)
        {
            tp->next = 
        }
    }
}

int main()
{

}