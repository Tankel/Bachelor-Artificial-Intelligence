#include <iostream>
#include <time.h>
#include <algorithm>

using namespace std;

int binarySearch(int arr[], int l, int r, int x)
{
	if (r >= l)
	{
		int mid = l + (r - l) / 2;
		if (arr[mid] == x)
			return mid;
		if (arr[mid] > x)
			return binarySearch(arr, l, mid - 1, x);
		return binarySearch(arr, mid + 1, r, x);
	}
	return -1;
}

template <typename T>
struct Node
{
	T key;
	Node *parent;
	Node *leftChild;
	Node *rightChild;
	Node(T key, Node *parent)
	{
		this->key = key;
		this->parent = parent;
		this->leftChild = nullptr;
		this->rightChild = nullptr;
	}
};

template <typename T>
class Tree
{
public:
	Node<T> *root;
	Tree()
	{
		this->root = nullptr;
	};
	~Tree(){};

	void addLeftChild(T newKey)
	{
		if (this->root == nullptr)
		{
			this->root = new Node<T>(newKey, nullptr);
			return;
		}

		Node<T> *currentNode = this->root;
		while (currentNode->leftChild != nullptr)
		{
			currentNode = currentNode->leftChild;
		}
		currentNode->leftChild = new Node<T>(newKey, nullptr);
	}
	void addRightChild(T newKey)
	{
		if (this->root == nullptr)
		{
			this->root = new Node<T>(newKey, nullptr);
			return;
		}

		Node<T> *currentNode = this->root;
		while (currentNode->rightChild != nullptr)
		{
			currentNode = currentNode->rightChild;
		}
		currentNode->rightChild = new Node<T>(newKey, nullptr);
	}
	void addZigZag(T newKey)
	{
		if (this->root == nullptr)
		{
			this->root = new Node<T>(newKey, nullptr);
			return;
		}

		Node<T> *currentNode = this->root;
		while (currentNode->leftChild != nullptr || currentNode->rightChild != nullptr)
		{
			if (currentNode->leftChild != nullptr)
				currentNode = currentNode->leftChild;
			else
				currentNode = currentNode->rightChild;
		}

		if (currentNode == this->root)
			currentNode->rightChild = new Node<T>(newKey, currentNode);
		else if (currentNode->parent->leftChild == currentNode)
			currentNode->rightChild = new Node<T>(newKey, currentNode);
		else if (currentNode->parent->rightChild == currentNode)
			currentNode->leftChild = new Node<T>(newKey, currentNode);
	}
	void addRandom(T newKey)
	{
		if (this->root == nullptr)
		{
			this->root = new Node<T>(newKey, nullptr);
			return;
		}

		Node<T> *currentNode = this->root;
		while (true)
		{
			int r = rand() % 2;
			if (r) // r = 1
			{
				if (currentNode->rightChild == nullptr)
				{
					currentNode->rightChild = new Node<T>(newKey, currentNode);
					return;
				}
				currentNode = currentNode->rightChild;
			}
			else
			{
				if (currentNode->leftChild == nullptr)
				{
					currentNode->leftChild = new Node<T>(newKey, currentNode);
					return;
				}
				currentNode = currentNode->leftChild;
			}
		}
	}
	void preorderTraversal(Node<T> *currentNode)
	{
		if (currentNode == nullptr)
			return;

		cout << currentNode->key << " ";

		this->preorderTraversal(currentNode->leftChild);

		this->preorderTraversal(currentNode->rightChild);
	}
	void inorderTraversal(Node<T> *currentNode)
	{
		if (currentNode == nullptr)
			return;

		this->inorderTraversal(currentNode->leftChild);

		cout << currentNode->key << " ";

		this->inorderTraversal(currentNode->rightChild);
	}
	void postorderTraversal(Node<T> *currentNode)
	{
		if (currentNode == nullptr)
			return;

		this->postorderTraversal(currentNode->leftChild);

		this->postorderTraversal(currentNode->rightChild);

		cout << currentNode->key << " ";
	}

	// pasamos el indice del preorder (para llevar en cuenta las raices)
	// por referencia, ya que al ser recursiva, de lo contrario se mandarían copias
	// Necesitamos que el contador avance tras cada iteración
	Node<T> *recoverTree(int preorder[], int inorder[], int l, int r, int *x)
	{
		if (l > r)
			return nullptr;

		Node<T> *currentNode = new Node<T>(preorder[*x], nullptr);
		(*x)++;

		if (l == r)
			return currentNode;

		int rootIdx = binarySearch(inorder, l, r, currentNode->key);

		currentNode->leftChild = this->recoverTree(preorder, inorder, l, rootIdx - 1, x);
		currentNode->rightChild = this->recoverTree(preorder, inorder, rootIdx + 1, r, x);

		return currentNode;
	}
};

int main()
{
	srand(time(NULL));
	Tree<int> t;

	/*
	t.addLeftChild(1);
	t.addRightChild(2);
	t.addRandom(3);
	for(int i=1; i<6; i++)
	{
		t.addZigZag(i);
	}*/

	int preorder[] = {3, 9, 1, 2, 20, 15, 7};
	int inorder[] = {1, 9, 2, 3, 15, 20, 7};
	int n = sizeof(preorder) / sizeof(preorder[0]);
	int m = 0;

	t.root = t.recoverTree(preorder, inorder, 0, n - 1, &(m));
	cout << "\nPreorder: ";
	t.preorderTraversal(t.root);
	cout << "\nInorder: ";
	t.inorderTraversal(t.root);
	cout << "\nPostorder: ";
	t.postorderTraversal(t.root);
}