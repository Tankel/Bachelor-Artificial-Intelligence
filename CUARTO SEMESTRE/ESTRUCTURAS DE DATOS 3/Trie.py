class Node:
    def __init__(self):
        # Hijos del nodo
        self.children = [None] * 26
        # Bandera para ver si es hoja 
        self.isLeaf = False

class Trie:
    def __init__(self):
        self.root = Node()

    #convertimos un carcter a un int (a=0, b=1, c=2...)
    def __charToIndex(self, c):
        return ord(c) - ord('a')
    
    def insert(self, word):
        currentNode = self.root
        #recorremos cada letra de la palabra
        for c in word:
            # checar si el nodo actual tiene como hijo a c
            index = self.__charToIndex(c)
            # si no lo tiene lo creamos
            if currentNode.children[index] is None:
                currentNode.children[index] = Node()
            # nos movemos a ese nodo
            currentNode = currentNode.children[index]
        # Marcar como hoja
        currentNode.isLeaf = True

    def search(self, word):
        currentNode = self.root
        #recorremos cada letra de la palabra
        for c in word:
            # checar si el nodo actual tiene como hijo a c
            index = self.__charToIndex(c)
            # si si lo tiene nos movemos
            if currentNode.children[index] is not None:
                currentNode = currentNode.children[index]
            # si no lo tiene 
            else:
                return False
        #si terminamos de recorrer el la palabra y el ultimo nodo/caracter es hoja, lo hemos encontrado
        if currentNode.isLeaf is True:
            return True
        return False


t = Trie()
t.insert("hola")
t.insert("ray")
t.insert("loco")
t.insert("quibo")
t.insert("rayos")

print("Buscamos:\n(True si se encuentra, False si no)")
print("ra:",t.search("ra"))
print("ray:",t.search("ray"))
print("rayo:",t.search("rayo"))
print("rayos:",t.search("rayos"))

