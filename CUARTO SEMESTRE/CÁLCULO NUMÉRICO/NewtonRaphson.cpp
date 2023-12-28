#include <iostream>
#include <math.h>

using namespace std;

float f(float x)
{
    //return (x*x*x) - (2*x*x) - 5;
    //return 2*x*x*x -11.7*x*x + 17.7*x -5;
    return log(x) - (1.0/x);
}

// derivada de f
float df(float x)
{
    //return (3*x*x) - (4*x);
    //return 6*x*x - 23.4*x + 17.7;
    return log(x) + (1.0/(x*x));
}

float newtonraphson(float x_0)
{
    float x_1 = x_0 - (f(x_0) / df(x_0));
    float error = abs((x_1 - x_0) / x_1);

    while (error > 0.00001)
    {
        x_0 = x_1;
        x_1 = x_1 - (f(x_1) / df(x_1));
        error = abs((x_1 - x_0) / x_1);
    }

    cout << "RAIZ DE F: " << x_1 << endl;
    cout << "ERROR: " << error << endl;
}

int main()
{
    cout<<"\nNEWTON RAPHSON:\n";
    float x0 = 1;
    newtonraphson(x0);
    cout<<0.56714328<<endl<<endl;
}