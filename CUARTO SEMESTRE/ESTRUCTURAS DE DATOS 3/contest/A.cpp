#include <iostream>

using namespace std;

int main()
{
    int n, m, cont=0;
    cin>>n>>m;
    if(m<n)
        cout<<n-m;
    else
    {
        while(m>n)
        {
            if(m%2==1)
                m++; 
            else
                m/=2;
            cont++;
            //cout<<"n: "<<n<<endl;
            //cout<<"m: "<<m<<endl;
        }
        cout<<cont + n-m;
    }
}