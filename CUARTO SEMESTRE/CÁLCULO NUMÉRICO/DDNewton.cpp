#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

float f(float x)
{
    return log(x);
}

float dividedDifference(vector<float> x, vector<float> y, int a, int b)
{
    if (a - b == 1)
    {
        return (y[a] - y[b]) / (x[a] - x[b]);
    }
    return (dividedDifference(x, y, a, b + 1) - dividedDifference(x, y, a - 1, b)) / (x[a] - x[b]);
}

float newtonDividedDifference(vector<float> x, vector<float> y, float x_input, int n)
{
    cout << "\nP(x) =\t";
    float result = y[0];
    cout << y[0] << "\t";

    for (int i = 1; i < n; i++)
    {
        float prod = 1;

        float d = dividedDifference(x, y, i, 0);
        (d >= 0) ? cout << "+ " << d : cout <<"- " <<-d;

        for(int j=0; j<i; j++)
        {
            cout<<"(x";
            (-x[j] >= 0) ? cout<<"+"<<-x[j]<<")":cout<<-x[j]<<")";

            prod *= (x_input -x[j]);
        }
        cout<< " ";
        result+=d*prod;
    }
    cout<<endl;

    return result;
}

int main()
{
    vector<float> x = {8, 9, 11};
    vector<float> y;

    //vector<float> x = {1, 1.3, 1.6, 1.9, 2.2};
    //vector<float> y = {.7651, .62, .4554, .2818, .1103};


    for(int i=0; i<x.size(); i++)
        y.push_back(f(x[i]));

    float x_input = 10;

    //newtonDividedDifference(x, y, x_input, x.size());
    cout<<"\nf("<<x_input<<") = "<<newtonDividedDifference(x, y, x_input, x.size())<<endl<<endl;
}