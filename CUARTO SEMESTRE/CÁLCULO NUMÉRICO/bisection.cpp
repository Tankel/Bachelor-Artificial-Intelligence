#include <iostream>
#include <cmath>

using namespace std;

// función a evaluar
float myFunc(float x)
{
    return (x * x * x * x) - (2 * x * x * x) - (4 * x * x) + (4*x) + 4;
}

// margen de error
float error(float a, float b)
{
    // cout<<"a: "<<a<<"\tb: "<<b<<endl;
    return abs((a - b) / a);
}

// raiz en un intervalo (a,b)
void raiz(float a, float b)
{
    float p = 0;
    float er;
    // numero de iteraciones para que no cicle eternamente si no tiene
    // solución real o es un numero con muchos decimales
    int i = 100;
    while (i--)
    {
        p = (a + b) / 2;
        // cout << p << endl;
        float fp = myFunc(p);
        float fa = myFunc(a);
        float fb = myFunc(b);

        // si tienen mismo signo, moevemos el limite izquierdo al de enmedio (agarramos la mitad derecha)
        if (fa * fp > 0)
        {
            er = error(a, p);
            a = p;
        }
        // si tienen mismo signo, moevemos el limite derecho al de enmedio (agarramos la mitad izquierda)
        else
        {
            er = error(b, p);
            b = p;
        }

        // si el error ya es muy minimo o 0, o polinimio ya da 0
        if (er == 0 || fp == 0)
            break;
    }

    cout << "RAIZ DE f: "<< p << endl;
    cout << "ERROR: "<<er<<endl<<endl;
}

int main()
{
    cout<<"\nBISECCION:\n";
    int a = 0;
    int b = 2;
    raiz(a, b);
}
