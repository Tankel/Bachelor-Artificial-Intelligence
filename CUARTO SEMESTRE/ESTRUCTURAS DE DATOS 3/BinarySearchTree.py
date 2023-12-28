class Node:
    def __init__(self, key, parent):
        self.key = key
        self.parent = parent
        self.leftChild = None
        self.rightChild = None


class binarySearchTree:
    def __init__(self):
        self.root = None

    def inorderTraversal(self, currentNode):
        # checamos que no lleguemos a un nodo vacio
        if currentNode is None:
            return

        # volver a hacer lo mismo con el hijo izq
        self.inorderTraversal(currentNode.leftChild)

        # imprimir nodo (marcarlo como visitado)
        print(currentNode.key, end=" ")

        # luego hacerlo con el hijo der
        self.inorderTraversal(currentNode.rightChild)

    def preorderTraversal(self, currentNode):
        # checamos que no lleguemos a un nodo vacio
        if currentNode is None:
            return
        # imprimir nodo (marcarlo como visitado)
        print(currentNode.key, end=" ")

        # volver a hacer lo mismo con el hijo izq
        self.preorderTraversal(currentNode.leftChild)

        # luego hacerlo con el hijo der
        self.preorderTraversal(currentNode.rightChild)

    def insert(self, parent, currentNode, key):
        # cuando la raiz es nula o ya llegue a donde deberia insertar el valor
        if currentNode is None:
            # si no tiene raiz
            if parent == None:
                self.root = Node(key, None)
            # si el nodo es mayor que el padre, se inserta a la derecha
            elif key > parent.key:
                parent.rightChild = Node(key, parent)
            # si el nodo es menor que el padre, se inserta a la izquierda
            else:
                parent.leftChild = Node(key, parent)
        # si aún sigo en algun nodo del arbol
        else:
            # si el nodo a insertar es mayor a su padre se inserta a la derecha
            if key > currentNode.key:
                self.insert(currentNode, currentNode.rightChild, key)
            # si el nodo a insertar es menor a su padre se inserta a la izquierda
            else:
                self.insert(currentNode, currentNode.leftChild, key)

    def search(self, currentNode, i):
        # si la raiz es nula no hay donde uscar
        if currentNode == None:
            return None
        # si la key del nodo es la que buscamos retornamos ese nodo
        elif i == currentNode.key:
            return currentNode
        # si la key es menor a la que buscamos, nos movemos hacia los mayores (la derecha)
        elif i > currentNode.key:
            return self.search(currentNode.rightChild, i)
        # si no (la key es mayor), nos movemos hacia los menores (la izquierda)
        else:
            return self.search(currentNode.leftChild, i)

    def maxKey(self, currentNode):
        # nos movemos hacia los hijos derechos hasta encontrar una hoja
        while currentNode.rightChild != None:
            currentNode = currentNode.rightChild
        return currentNode.key

    def minKey(self, currentNode):
        # nos movemos hacia los hijos izquierdos hasta encontrar una hoja
        while currentNode.leftChild != None:
            currentNode = currentNode.leftChild
        return currentNode.key

    def build(self, numbers):
        # insertamos cada uno de los nodos
        for i in numbers:
            self.insert(None, self.root, i)

    def successor(self, ckey):
        currentNode = self.search(self.root, ckey)
        # si es el nodo mayor de todo el arbol es el mismo
        if (currentNode.key == self.maxKey(self.root)):
            return currentNode.key
        # si el hijo derecho no es nulo, buscamos el menor de ese subarbol
        if currentNode.rightChild is not None:
            return self.minKey(currentNode.rightChild)
        # si el hijo der es nulo
        else:
            while (currentNode is not None):
                # si es hijo izquierdo retornamos al padre
                if (currentNode.parent.leftChild == currentNode):
                    return currentNode.parent.key
                # nos movemos al padre
                currentNode = currentNode.parent
        return currentNode.key

    def predecessor(self, ckey):
        currentNode = self.search(self.root, ckey)

        # si es el nodo mas pequeño de todo el arbol es el mismo
        if (currentNode.key == self.minKey(self.root)):
            return currentNode.key
        # si el hijo izq no es nulo, buscamos el mayor de dicho subarbol
        if currentNode.leftChild is not None:
            return self.maxKey(currentNode.leftChild)
        # si el hijo izq es nulo,
        else:
            # buscamos para arriba del arbol (en los padres)
            while (currentNode is not None):
                # si es hijo derecho retornamos al padre
                if (currentNode.parent.rightChild == currentNode):
                    return currentNode.parent.key
                # nos movemos al padre
                currentNode = currentNode.parent
        return currentNode.key

    def remove(self, ckey):
        # buscamos el nodo a remover
        currentNode = self.search(self.root, ckey)
        # si el nodo no es raiz
        if currentNode != self.root:
            # bool para saber si currentNode es hijo izquierdo o derecho
            isLeftChild = True if (
                currentNode.parent.leftChild == currentNode) else False

            # si el nodo no tiene hijos
            if (currentNode.rightChild == None and currentNode.leftChild == None):
                # cambiamos la referencia de su padre al hijo a nulo
                if (isLeftChild):
                    currentNode.parent.leftChild = None
                else:
                    currentNode.parent.rightChild = None

            # si el nodo solo tiene un hijo
            elif (currentNode.leftChild == None or currentNode.rightChild == None):
                # Cambiamos el hijo del padre por el hijo del nodo a remover
                if currentNode.parent.leftChild == currentNode:
                    if currentNode.leftChild is not None:
                        currentNode.parent.leftChild = currentNode.leftChild
                        currentNode.leftChild.parent = currentNode.parent
                    else:
                        currentNode.parent.leftChild = currentNode.rightChild
                        currentNode.rightChild.parent = currentNode.parent
                else:
                    if currentNode.leftChild is not None:
                        currentNode.parent.rightChild = currentNode.leftChild
                        currentNode.leftChild.parent = currentNode.parent
                    else:
                        currentNode.parent.rightChild = currentNode.rightChild
                        currentNode.rightChild.parent = currentNode.parent
            # si el nodo tiene dos hijos
            else:
                # buscamos el nodo sucesor
                succesor = self.search(
                    self.root, self.successor(currentNode.key))
                # si el sucesor es el hijo derecho
                if succesor == currentNode.rightChild:
                    # Cambiamos cambiamos el enlace del padre del nodo con su sucesor
                    if currentNode.parent.rightChild == currentNode:
                        currentNode.parent.rightChild = succesor
                        succesor.parent = currentNode.parent
                    else:
                        currentNode.parent.leftChild = succesor
                        succesor.parent = currentNode.parent
                    # Cambiamos el enlace del sucesor con el hijo izquierdo del nodo
                    succesor.leftChild = currentNode.leftChild
                # si el sucesor se ecnuentra en el subarbol derecho, pero no es directamente su hijo
                # elif (self.search(currentNode.rightChild, succesor.key) != None):
                else:
                    # Cambiamos el hijo del sucesor a la posición del sucesor
                    if (succesor.parent.leftChild == succesor):
                        succesor.parent.leftChild = succesor.rightChild
                    else:
                        succesor.parent.rightChild = succesor.rightChild

                    # Si el hijo del sucesor no es nulo, cambiamos su referencia de padre
                    if succesor.rightChild is not None:
                        succesor.rightChild.parent = succesor.parent

                    # Cambiamos el padre del sucesor al padre del nodo
                    succesor.parent = currentNode.parent
                    # Cambiamos los hijos del sucesor a los hijos del nodo
                    succesor.leftChild = currentNode.leftChild
                    succesor.rightChild = currentNode.rightChild
                    # Cambiamos las referencias de los hijos del nodo a su nuevo padre
                    currentNode.leftChild.parent = succesor
                    currentNode.rightChild.parent = succesor

                    # Cambiamos al sucesor al lugar del nodo que eliminamos
                    if currentNode.parent.leftChild == currentNode:
                        currentNode.parent.leftChild = currentNode
                    else:
                        currentNode.parent.rightChild = currentNode
                return
        # si es la raiz
        else:
            # si no tiene hijos eliminamos la raiz
            if (currentNode.rightChild == None and currentNode.leftChild == None):
                self.root = None
                return
            # si solo tiene hijos izquierdos, el mas grande es el primero
            elif currentNode.leftChild is None or currentNode.rightChild is None:
                if currentNode.leftChild is not None:
                    self.root = currentNode.leftChild
                else:
                    self.root = currentNode.rightChild
            # si tiene dos hijos
            else:
                ckey = self.successor(currentNode.key)
                succesor = self.search(self.root, ckey)

                # Cambiamos los enlaces con el hijo izquierdo de la raiz al nodo 'y'
                succesor.leftChild = currentNode.leftChild
                succesor.leftChild.parent = succesor

                # checamos que el sucesor no sea el hijo derecho de la raiz (para evitar que la raiz no se agregue a si misma como hijo)
                if succesor != currentNode.rightChild:
                    # Enlazamos al hijo derecho del sucesor con su padre
                    succesor.parent.leftChild = succesor.rightChild
                    # LOs hijos derechos del sucesor seran los hijos del raiz anteriori
                    succesor.rightChild = currentNode.rightChild
                    succesor.rightChild.parent = succesor

                # Hacemos nulo al padre
                succesor.parent = None
                # Actualizamos la raiz
                self.root = succesor


# construimos varios ejemplos para verificar que funcionen todos los casos
# numbers = [6, 3, 5, 7, 2, 1, 0, 10]
# numbers = [5, 6, 7, 8, 9]
numbers = [10, 2, 12, 5, 7, 11, 15, 13]
# numbers = [10, 4, 14, 7, 9, 6, 17, 22, 11]

# creamos el arbol
tree = binarySearchTree()
tree.build(numbers)

# lo imprimimos en inorder
print("Tree inorder: ", end=" ")
tree.inorderTraversal(tree.root)

# imprimirmos maximos y minimos del tree
print("\nMax: ", tree.maxKey(tree.root))
print("Min: ", tree.minKey(tree.root))


# buscamos del 0 al 10 que numeros se encuentran
print()
for i in range(0, 11):
    if (tree.search(tree.root, i) != None):
        print(i, "Encontrado!")
    else:
        print(i, "No encontrado :(")

# buscamos el sucesor y predecesor de todos los nodos
print()
for i in numbers:
    print("Sucesor de", i, "->", tree.successor(i))
    print("Predecesor de", i, "->", tree.predecessor(i))

# borramos de uno por uno todos los nodos
for i in numbers:
    print("\n\n\tBORRAMOS", i)
    tree.remove(i)
    print("Inorder", end=" ")
    tree.inorderTraversal(tree.root)
    print()
    print("Preorder", end=" ")
    tree.preorderTraversal(tree.root)
