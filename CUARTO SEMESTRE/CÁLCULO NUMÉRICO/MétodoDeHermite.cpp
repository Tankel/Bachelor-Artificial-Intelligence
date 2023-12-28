#include <iostream>

using namespace std;

float f(float x) {
    return x * x + 2 * x + 1;
}

float df(float x) {
    return 2 * x + 2;
}

float hermite(float x0, float x[], float y[], float yd[], int n) {
    float result = 0;

    for (int i = 0; i < n; i++) {
        float temp = y[i];

        for (int j = 0; j < n; j++) {
            if (i != j) {
                temp = temp * (x0 - x[j]) / (x[i] - x[j]);
            }
        }

        float phi = 1;

        for (int j = 0; j < n; j++) {
            if (i != j) {
                phi = phi * (x0 - x[j]);
            }
        }

        result += temp * phi * yd[i];
    }

    return result;
}

int main() {
    const int n = 2;
    //float x[] = { 0, 1, 2 };
    float x[] = { 8.3, 8.6};
    float y[] = { 17.56492, 18.50515};
    float yd[] = { 3.116256, 3.151762};

    /*
    float y[n], yd[n];
    for (int i = 0; i < n; i++) {
        y[i] = f(x[i]);
        yd[i] = df(x[i]);
    }*/

    float x0 = 0;
    float result = hermite(x0, x, y, yd, n);

    cout << "\np(" << x0 << ") = " << result << endl<<endl;

    return 0;
}
