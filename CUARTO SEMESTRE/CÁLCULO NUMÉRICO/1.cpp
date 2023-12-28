#include <iostream>

using namespace std;

int main()
{
    float suma=1;
    for (int i=1; 1<10001; i++)
    {
        suma = suma + 0.00001;
        //cout<<suma<<endl;
    }
    cout<<suma<<endl;
}