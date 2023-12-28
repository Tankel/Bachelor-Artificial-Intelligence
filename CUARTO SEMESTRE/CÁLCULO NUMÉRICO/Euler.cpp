#include <iostream>

using namespace std;

float fd(float t, float y)
{
    //return -2*t*t*t + 12*t*t -20*t +8.5;
    //return y - (t*t) + 1;
    //return -5*y + 5*t*t + 2*t; 
    float a = ((y/t)*(y/t)) + (y/t);
    //cout<<t<<y<<a<<endl;
    return a;
}

float euler(float a, float b, float N, float yi)
{
    //float h = (b-a)/N; 
    float h = 0.1; 
    cout<<endl;
    cout<<"y0 = "<<yi<<endl;
    for(int i=0; i<N; i++)
    {
        yi = yi + (h*fd(i*h+1, yi));
        cout<<"y"<<i+1<<" = "<<yi<<endl;
    }
    cout<<endl;
}

int main()
{
    //float a = 0, b = 1, N = 10, y0 = 0.3333333;
    float a = 1, b = 1.4, N = 4, y0 = 1;
    euler(a, b, N, y0);
}