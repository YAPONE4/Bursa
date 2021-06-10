#include <iostream>
#include <string.h>

using namespace std;

void search(char* pat, char* txt) 
{
    int count = 0, counters = 0;
    int q = 101; 
    int M = strlen(pat);
    int N = strlen(txt); 
    int i, j;   
    int p = 0;
    int t = 0;
    int h = 1; 
    int d = 256;
    for (i = 0; i < M - 1; i++) 
        h = (h * d) % q; 
    for (i = 0; i < M; i++) 
    { 
        p = (d * p + pat[i]) % q; 
        t = (d * t + txt[i]) % q; 
    } 
    for (i = 0; i <= N - M; i++) 
    { 
        if ( p == t ) 
        { 
            for (j = 0; j < M; j++) 
            { 
                if (txt[i+j] != pat[j]) 
                    break;
                counters++;
            } 
            if (j == M) 
            {
                cout << "Pattern found at index: "<< i << endl;
                count++;
            }
            counters++;
        } 
        counters++;
        if ( i < N - M ) 
        { 
            t = (d * (t - txt[i] * h) + txt[i + M]) % q; 
            if (t < 0) 
            t = (t + q); 
        }
        counters++;
    }
    if (count == 0)
        cout << "Pattern not found" << endl;
    counters++;
    cout << "IF's : " << counters;
}

int findCountFirstWord(string m)
{
    int count = 0;
    int wordcounter = 0;
    int counters = 0;
    while(((m[count] >= 65) && (m[count] <= 90)) || ((m[count] >= 97) && (m[count] <= 122)))
        count++;
    string firstw = "";
    for(int i = 0; i < count; i++)
        firstw += m[i];
    string checkw = "";
    for(int i = count + 1; i <= m.length(); i++)
    {
        if (((m[i] >= 65) && (m[i] <= 90)) || ((m[i] >= 97) && (m[i] <= 122)))
            checkw += m[i];
        else
        {
            if (checkw == firstw)
                wordcounter++;
            counters++;
            checkw = "";
        }
        counters += 1;
    }
    cout << endl << "IF's in func: " << counters << endl;
    return wordcounter;
}

int main()
{
    char c;
    cout << "Type which algoritm you want to use (F - FIRST WORD; R - ROBIN-KARP): ";
    cin >> c;
    switch(c)
    {
        case 'F':
        {
            cout << "Type string: ";
            string mainstr;
            cin >> mainstr;
            cout << findCountFirstWord(mainstr);
            break;
        }
        case 'R':
        {
            char *pattern, *text;
            int cpat, ctext;    
            cout << "How many symbols in text?: "; 
            cin >> ctext;
            cout << "How many symbols in pattern?: "; 
            cin >> cpat;
            pattern = new char[cpat];
            text = new char[ctext];
            cout << "Type text: "; 
            cin >> text;
            cout << "Type pattern: ";
            cin >> pattern;
            search(pattern, text);
            break;
        }
    }
    return 0;
}