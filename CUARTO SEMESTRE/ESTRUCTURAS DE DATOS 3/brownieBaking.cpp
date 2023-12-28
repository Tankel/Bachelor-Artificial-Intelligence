#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool myFunc(long long a, long long b)
{
    return a>b;
}

int main()
{
    int n, m;
    long long aux, cont=0;
    vector<long long> s, t;
    cin>>n>>m;
    for(long long i=0; i<n; i++)
    {
        cin>>aux;
        s.push_back(aux);
    }
    for(long long i=0; i<m; i++)
    {
        cin>>aux;
        t.push_back(aux);
    }55
    
    sort(s.begin(), s.end(), myFunc);
    sort(t.begin(), t.end(), myFunc);

    for(long long i=0; i<n; i++)
    {
        for(long long j=cont; j<m; j++)
            if(t[j]>=s[i])
            {
                //cout<<t[j]<<" >= "<<s[i]<<endl;
                cont++;
                break;
            }
    }
    cout<<cont;
}