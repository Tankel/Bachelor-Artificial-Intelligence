#include <iostream>
#include <time.h>
#include <algorithm>

using namespace std;

struct Node
{
    int key;
    // Node* parent;
    Node *leftChild;
    Node *rightChild;
    int leftIdx;
    int rightIdx;
    Node(int key, int leftIdx, int rightIdx)
    {
        this->key = key;
        // this->parent = parent;
        this->leftChild = nullptr;
        this->rightChild = nullptr;
        // rango del nodo
        this->leftIdx = leftIdx;
        this->rightIdx = rightIdx;
    }
};

class segmentTree
{
public:
    Node *root;
    int numbers[];
    segmentTree(int numbers[], int n)
    {
        this->root = new Node(0, 0, n - 1);
        for (int i = 0; i < n; i++)
            this->numbers[i] = numbers[i];
    }
    void build(Node *currentNode)
    {
        // cuando encontramos una hoja le asignamos el valor del index que apunta en la lista
        if (currentNode->leftIdx == currentNode->rightIdx)
        {
            currentNode->key = this->numbers[currentNode->leftIdx];
            return;
        }
        // Encontrar la mitad del rango,
        int midIdx = (currentNode->leftIdx + currentNode->rightIdx) / 2;

        //  Creamos el nodo izq y der 
        currentNode->leftChild = new Node(0, currentNode->leftIdx, midIdx);
        currentNode->rightChild = new Node(0, midIdx + 1, currentNode->rightIdx);

        // Creamos el subarabol izq y der
        // llamamos la función build con el hijo izq y der
        this->build(currentNode->leftChild);
        this->build(currentNode->rightChild);

        // Mezclamos los valores de los dos hijos en el nodo actual
        currentNode->key = currentNode->leftChild->key + currentNode->rightChild->key;
    };

    //update que agrega el valor dado
    void update(Node *currentNode, int addValue, int idx)
    {
        // Si terminamos de recorrer la rama
        if (currentNode == nullptr)
            return;

        // Chechar si el rango del actual contiene al indicie a modifcar
        else if (idx < currentNode->leftIdx || idx > currentNode->rightIdx)
            return;

        // Modificar el valor del nodo
        // Hacer llamada recurisva para modificiar el valor de sus hijos
        currentNode->key += addValue;
        this->update(currentNode->leftChild, addValue, idx);
        this->update(currentNode->rightChild, addValue, idx);
    }

    //update que cambia el valor dado
    void update2(Node *currentNode, int newValue, int idx)
    {
        // Si terminamos de recorrer la rama
        if (currentNode == nullptr)
            return;

        // Chechar si el rango del actual contiene al indicie a modifcar 
        if (idx < currentNode->leftIdx || idx > currentNode->rightIdx)
            return;

        // si se llegamos a una hoja cambiamos su valor
        if (currentNode->leftIdx == currentNode->rightIdx)
        {
            currentNode->key = newValue;
            return;
        }

        // Modificar el valor del nodo
        // Hacer llamada recurisva para modificiar el valor de sus hijos
        this->update2(currentNode->leftChild, newValue, idx);
        this->update2(currentNode->rightChild, newValue, idx);

        // volvemos a calcular el valor de los otros nodos
        currentNode->key = currentNode->leftChild->key + currentNode->rightChild->key;
    }
    int getSum(Node *currentNode, int l, int r)
    {
        if (currentNode == nullptr)
            return 0;
        // si el indice del nodo este fuera del rango no sumamos nada
        else if (r < currentNode->leftIdx || l > currentNode->rightIdx)
            return 0;
        // si el indice del nodo está dentro del rango retornamos el valor del nodo
        else if (l <= currentNode->leftIdx && r >= currentNode->rightIdx)
            return currentNode->key;
        // si el nodo está parcialmente dentro del rango, volvermos a llamar la función tanto con el hijo izquierdo como el derecho
        else
            return this->getSum(currentNode->leftChild, l, r) + this->getSum(currentNode->rightChild, l, r);
    };
};

int main()
{
    int numbers[] = {5, 4, 3, 2, 10, 0, 3, 4};
    int n = sizeof(numbers) / sizeof(numbers[0]);
    segmentTree st(numbers, n);

    st.build(st.root);
    cout<<"Sumamos del 2-5: "<<st.getSum(st.root, 2, 5)<<endl;

    st.update(st.root, 6, 4);
    cout<<"Sumamos 6 al nodo 4: "<<st.getSum(st.root, 2, 5)<<endl;

    st.update2(st.root, 0, 3);
    cout<<"Cambiamos al nodo 3 dandole el valor de 0: "<<st.getSum(st.root, 2, 5)<<endl;
}