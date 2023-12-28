#include <iostream>
#include <time.h>
#include <algorithm>

using namespace std;

struct Node
{
    int key;
    Node *parent;
    Node *leftChild;
    Node *rightChild;
    Node(int key, Node *parent)
    {
        this->key = key;
        this->parent = parent;
        this->leftChild = nullptr;
        this->rightChild = nullptr;
    }
};
// binary search tree
class bst
{
public:
    Node *root;
    bst()
    {
        this->root = nullptr;
    }
    void inorderTraversal(Node *currentNode)
    {
        if (currentNode == nullptr)
            return;

        this->inorderTraversal(currentNode->leftChild);

        cout << currentNode->key << " ";

        this->inorderTraversal(currentNode->rightChild);
    }
    void insert(Node *parent, Node *currentNode, int key)
    {
        // cuando la raiz es nula o ya llegue a donde debería insertar el valor
        if (currentNode == nullptr)
        {
            // si no tiene raiz
            if (parent == nullptr)
                this->root = new Node(key, nullptr);
            // si el nodo es mayor que el padre, se inserta a la derecha
            else if (key > parent->key)
                parent->rightChild = new Node(key, parent);
            // si el nodo es menor que le padre, se inserta al aizquierda
            else
                parent->leftChild = new Node(key, parent);
        }
        // si aún sigo en algun nodo del arbol
        else
        {
            // si el nodo a insertar es mayor a su padre, se inserta a la der
            if (key > currentNode->key)
                this->insert(currentNode, currentNode->rightChild, key);
            // si el nodo a insertar es menor a us padre, se inserta a la izq
            else
                this->insert(currentNode, currentNode->leftChild, key);
        }
    }
    void build(int numbers[], int n)
    {
        for (int i = 0; i < n; i++)
            this->insert(nullptr, this->root, numbers[i]);
    }
    Node *search(Node *currentNode, int i)
    {
        if (currentNode == nullptr)
            return nullptr;
        else if (i == currentNode->key)
            return currentNode;
        else if (i > currentNode->key)
            return this->search(currentNode->rightChild, i);
        else
            return this->search(currentNode->leftChild, i);
    }
    int maxKey(Node *currentNode)
    {
        while (currentNode->rightChild != nullptr)
            currentNode = currentNode->rightChild;
        return currentNode->key;
    }
    int minKey(Node *currentNode)
    {
        while (currentNode->leftChild != nullptr)
            currentNode = currentNode->leftChild;
        return currentNode->key;
    }
    int successor(int ckey)
    {
        Node *currentNode = this->search(this->root, ckey);
        // si es el nodo mayor de todo el arbol es el mismo
        if (currentNode->key == this->maxKey(this->root))
            return currentNode->key;
        // si el hijo derecho no es nulo, buscamos el menor de ese subarbol
        else if (currentNode->rightChild != nullptr)
            return this->minKey(currentNode->rightChild);
        // si el hijo derecho es nulo
        else
        {
            while (currentNode != nullptr)
            {
                // si es hijo izquierdo retornamos al padre
                if (currentNode->parent->leftChild == currentNode)
                    return currentNode->parent->key;
                // nos movemos al padre
                currentNode = currentNode->parent;
            }
        }
        return currentNode->key;
    }
    int predecessor(int ckey)
    {
        Node *currentNode = this->search(this->root, ckey);
        // si es el nodo mas pequeño de todo el arbol es el mismo
        if (currentNode->key == this->minKey(this->root))
            return currentNode->key;
        // si el hijo izq exizte, buscamos el mayor de dicho subarbol
        else if (currentNode->leftChild != nullptr)
            return this->maxKey(currentNode->leftChild);
        // si el hijo izq no existe
        else
        {
            // buscamos para arriba del arbol (en los padres)
            while (currentNode != nullptr)
            {
                // si es hijo der retornamos al padre
                if (currentNode->parent->rightChild == currentNode)
                    return currentNode->parent->key;
                // nos movemos al padre
                currentNode = currentNode->parent;
            }
        }
        return currentNode->key;
    }

    void remove(int ckey)
    {
        Node *currentNode = this->search(this->root, ckey);
        bool isLeftChild = false;
        if (currentNode != this->root)
        {
            // boleano para saber si es hijo izq o der
            bool isLeftChild = true ? false : currentNode->parent->leftChild == currentNode;

            // si el nodo no tiene hojass
            if (currentNode->leftChild == nullptr && currentNode->rightChild == nullptr)
            {
                //cout<<"no me digas que aqui\n";
                if (currentNode->parent->leftChild == currentNode)
                    currentNode->parent->leftChild = nullptr;
                else
                    currentNode->parent->rightChild = nullptr;
            }
            // si solo tiene un hijo
            else if (currentNode->leftChild == nullptr || currentNode->rightChild == nullptr)
            {
                // cambiamos el hijo de padre, por el hijo del nodo a remover
                // si es hijo izquierdo
                if (currentNode->parent->leftChild == currentNode)
                {
                    // si solo tiene hijo izquierdo
                    if (currentNode->leftChild != nullptr)
                    {
                        currentNode->parent->leftChild = currentNode->leftChild;
                        currentNode->leftChild->parent = currentNode->parent;
                    } // si solo tiene hijo der
                    else
                    {
                        currentNode->parent->leftChild = currentNode->rightChild;
                        currentNode->rightChild->parent = currentNode->parent;
                    }
                }
                // si es el hijo der
                else
                {
                    // si solo tiene hijo izquierdo
                    if (currentNode->leftChild != nullptr)
                    {
                        currentNode->parent->rightChild = currentNode->leftChild;
                        currentNode->leftChild->parent = currentNode->parent;
                    } // si solo tiene hijo der
                    else
                    {
                        currentNode->parent->rightChild = currentNode->rightChild;
                        currentNode->rightChild->parent = currentNode->parent;
                    }
                }
            }
            // si el nodo tiene dos hijos
            else
            {
                // buscamos el nodo sucesor
                Node *succesor = this->search(this->root, this->successor(currentNode->key));
                // si el sucesor es el hijo derecho
                if (succesor == currentNode->rightChild)
                {
                    // Cambiamos cambiamos el enlace del padre del nodo con su sucesor
                    if (currentNode->parent->rightChild == currentNode)
                    {
                        currentNode->parent->rightChild = succesor;
                        succesor->parent = currentNode->parent;
                    }
                    else
                    {
                        currentNode->parent->leftChild = succesor;
                        succesor->parent = currentNode->parent;
                    }
                    // Cambiamos el enlace del sucesor con el hijo izquierdo del nodo
                    succesor->leftChild = currentNode->leftChild;
                }
                // si el sucesor se ecnuentra en el subarbol derecho, pero no es directamente su hijo
                // elif ( (this->search(currentNode->rightChild, succesor->key) != None):
                else
                {
                    // Cambiamos el hijo del sucesor a la posición del sucesor
                    if (succesor->parent->leftChild == succesor)
                        succesor->parent->leftChild = succesor->rightChild;
                    else
                        succesor->parent->rightChild = succesor->rightChild;

                    // Si el hijo del sucesor no es nulo, cambiamos su referencia de padre
                    if (succesor->rightChild != nullptr)
                        succesor->rightChild->parent = succesor->parent;

                    // Cambiamos el padre del sucesor al padre del nodo
                    succesor->parent = currentNode->parent;
                    // Cambiamos los hijos del sucesor a los hijos del nodo
                    succesor->leftChild = currentNode->leftChild;
                    succesor->rightChild = currentNode->rightChild;
                    // Cambiamos las referencias de los hijos del nodo a su nuevo padre
                    currentNode->leftChild->parent = succesor;
                    currentNode->rightChild->parent = succesor;

                    // Cambiamos al sucesor al lugar del nodo que eliminamos
                    if (currentNode->parent->leftChild == currentNode)
                        currentNode->parent->leftChild = currentNode;
                    else
                        currentNode->parent->rightChild = currentNode;
                }
            }
        }
        else
        {
            // si no tiene hijos eliminamos la raiz
            if (currentNode->rightChild == nullptr && currentNode->leftChild == nullptr)
                this->root = nullptr;
            // si solo tiene hijos izquierdos, el mas grande es el primero
            else if (currentNode->leftChild == nullptr || currentNode->rightChild == nullptr)
            {
                if (currentNode->leftChild != nullptr)
                    this->root = currentNode->leftChild;
                else
                    this->root = currentNode->rightChild;
            }
            // si tiene dos hijos
            else
            {
                ckey = this->successor(currentNode->key);
                Node *succesor = this->search(this->root, ckey);

                // Cambiamos los enlaces con el hijo izquierdo de la raiz al nodo 'y'
                succesor->leftChild = currentNode->leftChild;
                succesor->leftChild->parent = succesor;

                // checamos que el sucesor no sea el hijo derecho de la raiz (para evitar que la raiz no se agregue a si m==ma como hijo)
                if (succesor != currentNode->rightChild)
                {
                    // Enlazamos al hijo derecho del sucesor con su padre
                    succesor->parent->leftChild = succesor->rightChild;
                    // LOs hijos derechos del sucesor seran los hijos del raiz anteriori
                    succesor->rightChild = currentNode->rightChild;
                    succesor->rightChild->parent = succesor;
                }
                // Hacemos nulo al padre
                succesor->parent = nullptr;
                // Actualizamos la raiz
                this->root = succesor;
            }
        }
    }
};

int main()
{
    // construimos varios ejempls para verificar que funcionen todos los casos
    // int numbers[] = {6, 3, 5, 7, 2, 1, 0, 10};
    // int numbers[] = {5, 6, 7, 8, 9};
    // int numbers[] = {10, 2, 12, 5, 7, 11, 15, 13};
    int numbers[] = {10, 4, 14, 7, 9, 6, 17, 22, 11};

    // creamos el arbol
    int n = sizeof(numbers) / sizeof(numbers[0]);
    bst t;
    t.build(numbers, n);

    // imprimirmos el arbol inroder
    cout << "Tree inorder: \n";
    t.inorderTraversal(t.root);
    cout << endl;

    // imprimirmos maximos y minimos
    cout << "\nMax: " << t.maxKey(t.root) << endl;
    cout << "Min: " << t.minKey(t.root) << endl << endl;

    // buscamos dle 0 al 10 que numeros se encuentran
    for (int i = 0; i < 11; i++)
    {
        if (t.search(t.root, i) != nullptr)
            cout << i << " encontrado!\n";
        else
            cout << i << " no encontrado\n";
    }
    cout << endl;

    // buscamos el sucesor y predecesor de toods los nodos
    for (int i = 0; i < n; i++)
    {
        cout << "Sucesor de " << numbers[i] << " -> " << t.successor(numbers[i]) << endl;
        cout << "Predecesor de " << numbers[i] << " -> " << t.predecessor(numbers[i]) << endl;
    }
    cout << endl;

    // borramos uno por uno todos los nodos
    for (int i = 0; i < n; i++)
    {
        cout << "\n\tBORRAMOS " << numbers[i] << endl;
        t.remove(numbers[i]);
        cout << "Inorder: ";
        t.inorderTraversal(t.root);
        cout << endl;
    }
    cout << endl;
}