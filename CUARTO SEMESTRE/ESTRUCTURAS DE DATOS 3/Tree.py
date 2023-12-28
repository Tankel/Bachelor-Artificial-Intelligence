import random

#creamos nodo
class Node:
    def __init__(self, key, parent):
        self.key = key
        self.leftChild = None
        self.rightChild = None
        self.parent = parent

#creamos arbol
class Tree:
    def __init__(self):
        self.root = None
        
    def addLeftChild(self, newKey):
        if self.root is None:
            self.root = Node(newKey, None)
            return 

        currentNode = self.root
        while(currentNode.leftChild is not None):
            currentNode = currentNode.leftChild 
        currentNode.leftChild = Node(newKey, currentNode)
    
    def addRightChild(self, newKey):
        if self.root is None:
            self.root = Node(newKey, None)
            return 

        currentNode = self.root
        while(currentNode.rightChild is not None):
            currentNode = currentNode.rightChild 
        currentNode.rightChild = Node(newKey, currentNode)

    def addZigZag(self, newKey):
        if self.root is None:
            self.root = Node(newKey, None)
            return 
        currentNode = self.root

        while(currentNode.leftChild is not None or currentNode.rightChild is not None):
            if currentNode.leftChild is not None:
                currentNode = currentNode.leftChild
            else:
                currentNode = currentNode.rightChild 
        
        if currentNode is  self.root:
            currentNode.rightChild = Node(newKey, currentNode)
        elif currentNode.parent.leftChild is currentNode:
            currentNode.rightChild = Node(newKey, currentNode)
        elif currentNode.parent.rightChild is currentNode:
            currentNode.leftChild = Node(newKey, currentNode)

    def addRandom(self, newKey):
        #si la raiz no existe, la creamos
        if self.root is None:
            self.root = Node(newKey, None)
            return 

        #hacemos una copia de la raiz
        currentNode = self.root
        while(True):
            #creamos un radnom para definir si se va al hijo izq(0) o der(1) 
            rand = random.randint(0, 1)
            if rand == 0:
                #si se va al izq, primero preguntamos si existe, si no agregamos el hijo ahí
                if currentNode.leftChild is None:
                    currentNode.leftChild = Node(newKey, currentNode)
                    return 
                    #si se agregó un hijo terminamos el proceso
                #si si existe, nos movemos a el
                currentNode = currentNode.leftChild

            #si rand = 1, hacesmos lo mismo con el hijo der
            else:
                if currentNode.rightChild is  None:
                    currentNode.rightChild = Node(newKey, currentNode)
                    return
                currentNode = currentNode.rightChild

                # 3 maneras de recorrer arboles binarios
                # Inorder (DFS): Izq - Raíz - Der 
                # Preorder: Raíz - Izq - Der
                # Postorder: Izq - Der - Raíz

    def inorderTraversal(self, currentNode):
        #checamos que no lleguemos a un nodo vacio
        if currentNode is None:
            return
        
        #volver a hacer lo mismo con el hijo izq
        self.inorderTraversal(currentNode.leftChild)

        #imprimir nodo (marcarlo como visitado)
        print(currentNode.key, end=" ")

        #luego hacerlo con el hijo der
        self.inorderTraversal(currentNode.rightChild)

    def preorderTraversal(self, currentNode):
        #checamos que no lleguemos a un nodo vacio
        if currentNode is None:
            return
        
        #imprimir nodo (marcarlo como visitado)
        print(currentNode.key, end=" ")

        #volver a hacer lo mismo con el hijo izq
        self.preorderTraversal(currentNode.leftChild)

        #luego hacerlo con el hijo der
        self.preorderTraversal(currentNode.rightChild)

    def postorderTraversal(self, currentNode):
        #checamos que no lleguemos a un nodo vacio
        if currentNode is None:
            return

        #volver a hacer lo mismo con el hijo izq
        self.postorderTraversal(currentNode.leftChild)

        #luego hacerlo con el hijo der
        self.postorderTraversal(currentNode.rightChild)

        #imprimir nodo (marcarlo como visitado)
        print(currentNode.key, end=" ")

    def recoverTree(self, preorder, inorder):

        #si el subarbol ya no tiene nodos no regresamos nada
        if len(inorder) < 1:
            return None

        #la raiz será el nodo más a la izquierda
        currentNode = Node(preorder[0], None)
        #borramos el más a la izquierda para cuando se vuelva a llamar
        preorder.remove(preorder[0])
        #print para visualizar los subarboles
        print(inorder)

        #si el nodo es una hoja será retornado como hijo
        if len(inorder) == 1:
            return currentNode
        

        #encontramos el index de la raiz para dividir a los subarboles
        rootIdx = inorder.index(currentNode.key)
        #llamamos a la función con los hijos izq y der
        currentNode.leftChild = self.recoverTree(preorder, inorder[0:rootIdx])
        currentNode.rightChild = self.recoverTree(preorder, inorder[rootIdx+1:len(inorder)])

        return currentNode




tree = Tree()
#for i in range(0,20):
    #tree.addRandom(i)

'''
tree.addLeftChild("yo")
tree.addLeftChild("sam")
tree.addLeftChild("ray")
tree.addRightChild("kev")
tree.addRightChild("gerry")
'''

'''
for i in range(1,6):
    tree.addZigZag(i)

print("\nInorder (DFS): Izq - Raíz - Der ")
tree.inorderTraversal(tree.root)
print("\nPreorder: Raíz - Izq - Der ")
tree.preorderTraversal(tree.root)
print("\nPostorder: Izq - Der - Raíz")
tree.postorderTraversal(tree.root)
'''


preorder = [3,9,1,2,20,15,7]
inorder = [1,9,2,3,15,20,7]


print("Inorder array:", inorder)

tree.root = tree.recoverTree(preorder, inorder)
print("Recovered tree:", end=" ")
tree.inorderTraversal(tree.root)



