#include <iostream>
#include <time.h>
#include <algorithm>

using namespace std;

struct Node
{
    int key;
    int height;
    int rollFactor;
    Node *parent;
    Node *leftChild;
    Node *rightChild;

    Node(int key, Node *parent)
    {
        this->key = key;
        this->height = 1;
        this->parent = parent;
        this->leftChild = nullptr;
        this->rightChild = nullptr;
        this->rollFactor = 0;
    }
};
// binary search tree
class AVL
{
public:
    Node *root;
    AVL()
    {
        this->root = nullptr;
    }
    void inorderTraversal(Node *node)
    {
        if (node == nullptr)
            return;

        // this->updateHeight(node);
        // this->updateRollFactor(node);

        this->inorderTraversal(node->leftChild);

        /*
        cout << node->key <<" - "<<node->rollFactor;
        if(node->leftChild!= nullptr)
            cout<<"\tlc: " << node->leftChild->key;
        if(node->rightChild!= nullptr)
            cout<<"\trc: "<< node->rightChild->key;
        cout<<endl;*/
        cout << node->key << " ";

        this->inorderTraversal(node->rightChild);
    }
    void leftRotation(Node *x)
    {
        // x = 4
        // y = 7
        Node *y = x->rightChild;
        x->rightChild = nullptr;
        // Si y contiene un subárbol izquierdo, asignamos x como el padre del subárbol izquierdo de y.
        if (y->leftChild != nullptr)
        {
            x->leftChild = y->leftChild;
            y->leftChild->parent = x;
        }
        else
        {
            x->leftChild = nullptr;
        }
        // Si el padre de x es None, entonces y se convierte en la raíz del árbol.
        if (x->parent == nullptr)
        {
            y->parent = nullptr;
            // cout<<"existp? "<<x->key;
            this->root = y;
            // cout<<"NEW ROOT "<<this->root->key<<endl;
        }
        else
        {
            // p = 10
            Node *p = x->parent;
            // si x es hijo izquierdo de p, hacemos y el hijo izquierdo de p
            y->parent = p;
            if (p->leftChild == x)
                p->leftChild = y;
            // sino, asignamos y como el hijo derecho de p.
            else
                p->rightChild = y;
        }

        // Hacemos y el padre de x
        x->parent = y;
        y->leftChild = x;
        // this->inorderTraversal(this->root);
        this->updateHeight(y);
        this->updateHeight(x);
    }

    void rightRotation(Node *y)
    {
        Node *x = y->leftChild;
        y->leftChild = nullptr;
        // Si x tiene un subárbol derecho, asignamos y como el padre del subárbol derecho de x.
        if (x->rightChild != nullptr)
        {
            y->rightChild = x->rightChild;
            x->rightChild->parent = y;
        }
        else
            y->rightChild == nullptr;
        // Si el padre de y es None, entonces x se convierte en la raíz del árbol.
        if (y->parent == nullptr)
        {
            x->parent = nullptr;
            this->root = x;
        }
        else
        {
            Node *p = y->parent;
            // si y es el hijo derecho de p, convertimos a x en el hijo derecho de p.
            x->parent = p;
            if (p->rightChild == y)
                p->rightChild = x;
            // Sino, asignamos a x como el hijo izquierdo de p
            else
                p->leftChild = x;
        }

        // Hacemos y el padre de x
        y->parent = x;
        x->rightChild = y;

        this->updateHeight(y);
        this->updateHeight(x);

        // y->height = max(y->leftChild->height, y->rightChild->height) + 1;
        // x->height = max(x->leftChild->height, x->rightChild->height) + 1;
    }

    void leftRightRotation(Node *x)
    {
        Node *z = x->parent;
        // hacemos una rotación izquierda en x-y
        this->leftRotation(x);
        this->rightRotation(z);
    }
    int getBalance(Node *node)
    {
        if (node == nullptr)
            return 0;
        if (node->rightChild != nullptr && node->leftChild != nullptr)
            return node->rollFactor = node->leftChild->height - node->rightChild->height;
        else if (node->rightChild != nullptr)
            return -node->rightChild->height;
        else if (node->leftChild != nullptr)
            return node->leftChild->height;
        else
            return 0;
        // return node->leftChild->height - node->rightChild->height;
    }
    void rightLeftRotation(Node *x)
    {

        Node *z = x->parent;
        // Hacemos una rotación izquierda en x-y
        this->rightRotation(x);
        this->leftRotation(z);
    }
    void updateHeight(Node *node)
    {
        // cout<<"soy el problema?";
        if (node == nullptr)
            return;
        if (node->rightChild != nullptr && node->leftChild != nullptr)
        {
            node->height = max(node->leftChild->height, node->rightChild->height) + 1;
        }
        else if (node->rightChild != nullptr)
            node->height = node->rightChild->height + 1;
        else if (node->leftChild != nullptr)
            node->height = node->leftChild->height + 1;
        else
            node->height = 1;
        this->updateHeight(node->leftChild);
        this->updateHeight(node->rightChild);
    }
    void updateRollFactor(Node *node)
    {
        this->updateHeight(this->root);
        if (node == nullptr)
            return;
        // actualizamos el factor de balanceo (difrencia de la altura del subarbol izq menos la altura del subarbol der)
        if (node->rightChild != nullptr && node->leftChild != nullptr)
        {
            // cout<<"node "<<node->key<<"\tlh "<<node->leftChild->height<<"\trg "<<node->rightChild->height;
            node->rollFactor = node->leftChild->height - node->rightChild->height;
        }
        else if (node->rightChild != nullptr)
        {
            // cout<<"node "<<node->key<<"\tr: "<<node->rightChild->key<<"-"<<node->rightChild->height<<endl;
            node->rollFactor = -node->rightChild->height;
        }
        else if (node->leftChild != nullptr)
        {
            // cout<<"node "<<node->key<<"\tl: "<<node->leftChild->key<<"-"<<node->leftChild->height<<endl;
            node->rollFactor = node->leftChild->height;
        }
        else
            node->rollFactor = 0;
        // cout<<"NODE "<<node->key<<"\t f "<<node->rollFactor<<endl;

        // cout<<"After update rollfactor: "<<endl;
        // this->inorderTraversal(this->root);
        // this->balanceNode(node);
        this->updateRollFactor(node->leftChild);
        this->updateRollFactor(node->rightChild);
    }
    void insert(Node *parent, Node *node, int key)
    {
        // cout<<key<<endl;
        //  cuando la raiz es nula o ya llegue a donde debería insertar el valor
        if (node == nullptr)
        {
            // si no tiene raiz
            if (parent == nullptr)
                this->root = new Node(key, nullptr);
            // si el nodo es mayor que el padre, se inserta a la derecha
            else if (key > parent->key)
            {
                parent->rightChild = new Node(key, parent);
                this->updateHeight(parent);
            }
            // si el nodo es menor que le padre, se inserta al aizquierda
            else
            {
                parent->leftChild = new Node(key, parent);
                this->updateHeight(parent);
            }
        }
        // si aún sigo en algun nodo del arbol
        else
        {
            // si el nodo a insertar es mayor a su padre, se inserta a la der
            if (key > node->key)
                this->insert(node, node->rightChild, key);
            // si el nodo a insertar es menor a us padre, se inserta a la izq
            else
                this->insert(node, node->leftChild, key);
        }
        // cout<<endl;
        // this->inorderTraversal(this->root);
        // cout<<endl;
        //  actualizamos el valor de balance de todos los nodos
        //  this->updateHeight(parent);
        this->updateRollFactor(this->root);

        // buscamos el primer nodo desbalanceado, yendo hacia arriba desde el nuevo nodo insertado.
        this->balanceNode(node, key);
    }
    void balanceNode(Node *currentNode, int newNode)
    {
        if (currentNode == nullptr)
            return;

        // cout<<currentNode->key;
        //  a altura del subárbol izquierdo es mayor que la del subárbol derecho
        // cout<<"new node "<<newNode<<endl;
        // cout<<" k: "<<currentNode->key<<" b "<<currentNode->rollFactor<<endl;
        if (currentNode->rollFactor > 1)
        {
            // Si el valor del nuevo nodo es menor que el valor del hijo izquierdo, hacemos una rotación derecha.
            if (newNode < currentNode->leftChild->key)
            {
                // cout << "\na\n";
                this->rightRotation(currentNode->leftChild);
            }
            // Sino, hacemos una rotación izquierda-derecha
            else
            {
                // cout << "\nb\n";
                this->leftRightRotation(currentNode->leftChild);
            }
            return;
        }
        else if (currentNode->rollFactor < -1)
        {
            // Si el valor del nuevo nodo es mayor que el valor del hijo derecho, hacemos una rotación izquierda.
            // cout<<"KKKKKKKKK"<<endl;
            if (newNode > currentNode->rightChild->key)
            {
                // cout << "\nc\nx: "<<currentNode->key<<endl;
                this->leftRotation(currentNode);
            }
            // Sino, hacemos una rotación derecha-izquierda.
            else
            {
                // cout << "\nd\n";
                this->rightLeftRotation(currentNode->rightChild);
            }
            return;
        }
        else
        {
            this->balanceNode(currentNode->parent, newNode);
            /*
            if(currentNode->parent->leftChild == currentNode)
                this->balanceNode(currentNode->parent->rightChild, newNode);
            else
                this->balanceNode(currentNode->parent->leftChild, newNode); */
        }
        this->updateRollFactor(this->root);
        // this->updateRollFactor(this->root);
        return;
    }
    void build(int numbers[], int n)
    {
        for (int i = 0; i < n; i++)
            this->insert(nullptr, this->root, numbers[i]);
    }
};

int main()
{
    int numbers[] = {9, 7, 8, 3, 5};
    // creamos el arbol
    int n = sizeof(numbers) / sizeof(numbers[0]);
    AVL t;
    t.build(numbers, n);
    t.inorderTraversal(t.root);
    cout << "RAIZ: " << t.root->key;
}
