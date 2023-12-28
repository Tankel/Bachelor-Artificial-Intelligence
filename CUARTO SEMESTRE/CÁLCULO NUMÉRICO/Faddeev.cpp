#include <iostream>
#include <vector>

using namespace std;

vector<vector<float>> sumarMatrices(vector<vector<float>> matriz1, vector<vector<float>> matriz2) {
    int n = matriz1.size();
    
    vector<vector<float>> resultado(n, vector<float>(n, 0));
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            resultado[i][j] = matriz1[i][j] + matriz2[i][j];
        }
    }
    
    return resultado;
}

vector<vector<float>> multiplicarMatrices(vector<vector<float>> matriz1, vector<vector<float>> matriz2) {
    int n = matriz1.size();
    
    vector<vector<float>> resultado(n, vector<float>(n, 0));
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                resultado[i][j] += matriz1[i][k] * matriz2[k][j];
            }
        }
    }
    
    return resultado;
}

int calcularTraza(vector<vector<float>> matriz) {
    int traza = 0;
    int n = matriz.size();

    for (int i = 0; i < n; i++) {
        traza += matriz[i][i];
    }
    return traza;
}

vector<vector<float>> matrizIdentidad(int n) {
    vector<vector<float>> identidad(n, vector<float>(n, 0));
    for (int i = 0; i < n; i++)
        identidad[i][i] = 1;
    return identidad;
}

vector<vector<float>> multiplicarEscalar(float l, vector<vector<float>> matriz) {
    int n = matriz.size();

    vector<vector<float>> resultado(n, vector<float>(n, 0));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++)
            resultado[i][j] = matriz[i][j] * l;
    }
    return resultado;
}

void printMatriz(vector<vector<float>> matrix)
{
    for (int i = 0; i < matrix.size(); i++)
    {
        for (int j = 0; j < matrix[i].size(); j++)
            cout << matrix[i][j] << " ";
        cout << endl;
    }
}

vector<float> faddeev(vector<vector<float>> A, vector<vector<float>> B, int n)
{
    float bi = 1;
    vector<float> bi_vector;
    bi_vector.push_back(bi);
    //cout<<"b"<<n<<" = "<<bi<<endl;

    for(float k=1; k<=n; k++)
    {
        B = sumarMatrices(multiplicarMatrices(A,B), multiplicarEscalar(bi, matrizIdentidad(n)));
        bi = -1/k * calcularTraza(multiplicarMatrices(A,B));
        //cout<<"b"<<n-k<<" = "<<bi<<endl;
        bi_vector.push_back(bi);
    }

    return bi_vector;
}

int main()
{
    /*
    vector<vector<float>> A =
        {
            {3, 1, 5},
            {3, 3, 1},
            {4, 6, 4}};
    */
    
    vector<vector<float>> A = {
        {3, 2, 4},
        {2, 0, 2},
        {4, 2, 3}};
    

    int n = A.size();
    vector<vector<float>> B(n, vector<float>(n, 0));

    vector<float> bi_vector = faddeev(A, B, n);

    cout<<endl;
    for(int i=0; i<=n; i++)
    {
        cout<<"b"<<n-i<<" = "<<bi_vector[i]<<endl;
    }
    cout<<endl;
    for(int i=0; i<=n; i++)
    {
        if(bi_vector[i]!=1)
            cout<<bi_vector[i];
        
        if(n-i == 1)
            cout<<"x";
        else if (n-i > 1)
            cout<<"x^"<<n-i;
        
        if(i!=n)
            cout<<" + ";
    }
    cout<<endl<<endl;
}
