#include <iostream>
#include <math.h>

using namespace std;

float f(float x)
{
    // return x-6;
    // return (x * x * x) + (2 * x * x) - (5 * x) - 6;
    // return exp(-x)-x;
    //return -(x*x) + 1.8*x + 2.5;
    return 2*x*x*x + -11.7*x*x +17.7*x -5;
}
void secantMethod(float p0, float p1)
{
    float res, er;
    do
    {
        res = p1 - ((f(p1) * (p0 - p1)) / (f(p0) - f(p1)));
        //cout<<"P0: "<<p0<<endl;
        p0 = p1;
        p1 = res;
        //cout<<"P1: "<<p1<<endl;
        er = abs(f(p1));
    } while (er > 0.000001);

    cout << "\nRAIZ DE f: " << p1 << endl;
    cout << "ERROR: " << er << endl
         << endl;
}
int main()
{
    cout<<"\nMETODO DE LA SECANTE:";
    secantMethod(3, 4);
}