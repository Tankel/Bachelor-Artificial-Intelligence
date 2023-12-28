#include <iostream>
#include <math.h>

using namespace std;

float f(float x)
{
    // return x-6;
    // return (x * x * x) + (2 * x * x) - (5 * x) - 6;
    //return exp(-x)-x;
    return log(x);
}

float x[] = {1, 4, 6};

void interpolation(int n)
{
    float r=0, p, l;
    for(int i=0;i<=n;i++)
    {
        l=1;
        for(int j=0;j<=n;j++)
        {
            if(i!=j)
            {
                l *= (n - x[j])/(x[i] - x[j]);
            }
        }
        r+= f(x[i])*l;
    }
    cout<<"Aproximacion: "<<r<<endl;
}
int main()
{
    interpolation(2);
}