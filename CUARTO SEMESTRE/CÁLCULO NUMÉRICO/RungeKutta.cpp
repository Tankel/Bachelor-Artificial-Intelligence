#include <iostream>
#include <vector>

using namespace std;

float yd(float t, float y)
{
    float a = ((y/t)*(y/t)) + (y/t);
    //cout<<t<<y<<a<<endl;
    return a;
}

void rungeKutta(float N, float h, float y0)
{
    const int n = 10; // n = N

    float k[4], t[100], y[100];
    y[0] = y0;
    //cout<<"y0 = "<<y[0]<<endl;
    cout<<endl;
    for(int i=0; i<N; i++)
    {
        t[i] = i*h+1;

        k[0] = h*yd(t[i],y[i]);
        k[1] = h*yd(t[i] + h*.5, y[i] + .5*k[0]);
        k[2] = h*yd(t[i] + h*.5, y[i] + .5*k[1]);
        k[3] = h*yd(t[i] + h, y[i] + k[2]);

        //cout<<k[0]<<k[1]<<k[2]<<k[3]<<endl;
        y[i+1] = y[i] + (k[0] + 2*k[1] + 2*k[2] + k[3])/6;
        cout<<"y"<<i<<" = "<<y[i]<<endl;
    }
    cout<<endl;
}

int main()
{
    float a=1, b=1.4, N=4, y0= 1.0, h=0.1;
    h = (b-a)/N;
    
    rungeKutta(N,h,y0);
}