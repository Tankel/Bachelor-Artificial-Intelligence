#include <iostream>
#include <vector>
#include <math.h>
#include <numeric>

using namespace std;

vector<float> jacobi(vector<vector<float>> equations)
{
    vector<float> result(equations.size());
    vector<float> previousResult(equations.size());
    float error, sumResults = 0, sumPrevResults = 0;
    int cont;
    do
    {
        for (int i = 0; i < result.size(); i++)
        {
            previousResult[i] = result[i];
            result[i] = equations[i][equations[0].size() - 1];
            for (int j = 0; j < result.size(); j++)
            {
                if (i != j)
                    result[i] -= (previousResult[j] * equations[i][j]);
            }
            result[i] /= equations[i][i];
        }

        sumResults = accumulate(result.begin(), result.end(), 0);
        sumPrevResults = accumulate(previousResult.begin(), previousResult.end(), 0);
        error = abs((sumResults - sumPrevResults) / sumResults);
    } while (error > 0.000001);

    return result;
}
vector<float> GS(vector<vector<float>> equations)
{
    vector<float> result(equations.size());
    vector<float> previousResult(equations.size());
    float error, sumResults = 0, sumPrevResults = 0;
    int cont = 0;
    do
    {
        for (int i = 0; i < result.size(); i++)
        {
            previousResult[i] = result[i];
            result[i] = equations[i][equations[0].size() - 1];
            for (int j = 0; j < result.size(); j++)
            {
                if (i != j)
                    result[i] -= (result[j] * equations[i][j]);
            }
            result[i] /= equations[i][i];
        }

        sumResults = accumulate(result.begin(), result.end(), 0);
        sumPrevResults = accumulate(previousResult.begin(), previousResult.end(), 0);
        error = abs((sumResults - sumPrevResults) / sumResults);
        cont++;
    } while (cont<100);

    return result;
}
void printMatrix(vector<vector<float>> matrix)
{
    for(int i = 0; i < matrix.size(); i++)
    {
        for(int j = 0; j < matrix[i].size(); j++)
            cout << matrix[i][j] << " ";
        cout << endl;
    }
}

#include <vector>
#include <cmath>

using namespace std;

// Función para comprobar si una matriz es diagonalmente dominante
bool isDiagonallyDominant(vector<vector<float>> A) {
    int n = A.size();
    for (int i = 0; i < n; i++) {
        float diagonal = abs(A[i][i]);
        float sum = 0;
        for (int j = 0; j < n; j++) {
            if (i != j) {
                sum += abs(A[i][j]);
            }
        }
        if (diagonal <= sum) {
            return false;
        }
    }
    return true;
}

// Función para convertir una matriz en diagonalmente dominante
void makeDiagonallyDominant(vector<vector<float>>& A) {
    int n = A.size();
    for (int i = 0; i < n; i++) {
        float maxVal = abs(A[i][i]);
        int maxIdx = i;
        for (int j = i + 1; j < n; j++) {
            if (abs(A[j][i]) > maxVal) {
                maxVal = abs(A[j][i]);
                maxIdx = j;
            }
        }
        // Intercambia la fila actual con la fila que contiene el elemento máximo
        if (maxIdx != i) {
            swap(A[i], A[maxIdx]);
        }
    }
}

// Función que convierte una matriz en diagonalmente dominante si es posible
bool convertToDiagonallyDominant(vector<vector<float>>& A) {
    if (isDiagonallyDominant(A)) {
        // La matriz ya es diagonalmente dominante, no hace falta hacer nada
        return true;
    }
    // Intenta hacer la matriz diagonalmente dominante
    makeDiagonallyDominant(A);
    if (isDiagonallyDominant(A)) {
        return true;
    }
    // La matriz no se pudo convertir en diagonalmente dominante
    return false;
}




int main()
{

    char variables[] = {'x', 'y', 'z', 'a', 'b', 'c', 'p', 'q', 'r'};

    vector<vector<float>> equations2 =
        {
            {3, -0.1, -0.2, 7.85},
            {0.1, 7, -0.3, -19.3},
            {0.3, -0.2, 10, 71.4}};

    vector<vector<float>> equations =
        {
            {7, 1, -2, 5},
            {-3, -5, 1, -20},
            {2, 2, -6, -8}};

    vector<vector<float>> equations3 =
        {
            {7, 3, 0, -29},
            {3, 2, 0, -16},
            {6, 1, 1, -11}};
    //printMatrix(equations3);

    convertToDiagonallyDominant(equations3);
    //printMatrix(equations3);
    if(convertToDiagonallyDominant(equations3))
        printMatrix(equations3);
    else
        cout<<"No se puede resolver el sistema de ecuaciones, la matriz no es dominante";

    vector<float> valuesGS = GS(equations3);
    vector<float> valuesJacobi = jacobi(equations3);

    cout<<endl<<endl;
    cout << "Gauss-Seidel:\n";
    for (int i = 0; i < valuesGS.size(); i++)
        cout << " " << variables[i] << " = " << valuesGS[i] << endl;
    cout<<endl;
    /*
    cout << "\nJacobi:\n";
    for (int i = 0; i < valuesJacobi.size(); i++)
        cout << " " << variables[i] << " = " << valuesJacobi[i] << endl;
    cout<<endl;
    */
}