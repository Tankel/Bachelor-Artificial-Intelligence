#include <iostream>
#include <vector>
#include <math.h>
#include <numeric>

using namespace std;

vector<float> solve(vector<vector<float>> equations, bool isGS)
{
    vector<float> result(equations.size());
    vector<float> previousResult(equations.size());
    float error, sumResults = 0, sumPrevResults = 0;

    int iterations=0;
    do
    {
        iterations++; 
        for (int i = 0; i < result.size(); i++)
        {
            previousResult[i] = result[i];
            result[i] = equations[i][equations[0].size() - 1];
            for (int j = 0; j < result.size(); j++)
            {
                if (i != j)
                {
                    if (isGS)
                        result[i] -= (result[j] * equations[i][j]);
                    else
                        result[i] -= (previousResult[j] * equations[i][j]);
                }
            }
            result[i] /= equations[i][i];
        }

        sumResults = accumulate(result.begin(), result.end(), 0);
        sumPrevResults = accumulate(previousResult.begin(), previousResult.end(), 0);
        error = abs((sumResults - sumPrevResults) / sumResults);
    } while (iterations < 1000);

    return result;
}

int main()
{
    char variables[] = {'x', 'y', 'z', 'a', 'b', 'c', 'p', 'q', 'r'};

    /*
    vector<vector<float>> equations =
        {
            {1, -0.1, -0.2, 7.85},
            {0.1, 7, -0.3, -19.3},
            {0.3, -0.2, 10, 71.4}};*/

    vector<vector<float>> equations2 = {
        {7, 3, 0,  -29},
        {3, 2, 0,  -16},
        {6, 1, 1, -11}};

    vector<vector<float>> equations =
        {
            {4, 1, 1, 6},
            {2, -5, 1, -2},
            {1, 2, 7, 10}};

    vector<float> valuesGS = solve(equations, true);
    vector<float> valuesJacobi = solve(equations, false);

    cout << "Gauss Seidel:\n";
    for (int i = 0; i < valuesGS.size(); i++)
        cout << "b"<<i << " = " << valuesGS[i] << endl;
    cout << "\nJacobi:\n";
    for (int i = 0; i < valuesJacobi.size(); i++)
        cout << "b"<<i << " = " << valuesJacobi[i] << endl;
}
