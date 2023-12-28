#include <iostream>
#include <math.h>

using namespace std;

float g(float x)
{
    // f(x) = -x^2 + 1.8x +2.5
    // g(x) = 
    // f(x) = e^-x - x = 0 --> x = e^-x
    // g(x) = e^-x
    // return exp(-x);

    //return sqrt((10-(x*x*x))/4);
    // return x - (x*x*x) - (4*x*x) + 10;
    //return sqrt((10/x) -(4*x));
    //return -(x*x) +(2.8*x) + 2.5;
    //return (((x*x)-2.5))/1.8;
    return sqrt((1.8*x) + 2.5);
}

float error(float a, float b)
{
    // cout<<"a: "<<a<<"\tb: "<<b<<endl;
    return abs((a - b) / a);
}

void puntoFijo(float x)
{
    float p_h; // p_(i-1)
    float p_i = x;
    float er; // error
    do
    {
        //cout<<p_i<<"\n";
        p_h = p_i;
        p_i = g(p_i);
        er = error(p_i, p_h);

    } while (er > 0.00001);

    cout << "\nRAIZ DE f: " << p_i << endl;
    cout << "ERROR: " << er << endl << endl;
}

int main()
{

    cout<<"\nPUNTO FIJO:";
    puntoFijo(0.5);
}