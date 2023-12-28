import random


class Node:
    def __init__(self, key, leftIdx, rightIdx):
        self.key = key
        self.leftChild = None
        self.rightChild = None
        # rango del nodo
        self.leftIdx = leftIdx
        self.rightIdx = rightIdx


class segmentTree:
    def __init__(self, numbers):
        self.root = Node(0, 0, len(numbers)-1)
        self.numbers = numbers

    def build(self, currentNode):
        # cuando encontramos una hoja le asignamos el valor del index que apunta en la lista
        if currentNode.leftIdx == currentNode.rightIdx:
            currentNode.key = self.numbers[currentNode.leftIdx]
            return

        # Encontrar la mitad del rango, // para redondear a int
        midIdx = (currentNode.leftIdx + currentNode.rightIdx)//2

        # Creamos el nodo izq y der
        currentNode.leftChild = Node(0, currentNode.leftIdx, midIdx)
        currentNode.rightChild = Node(0, midIdx+1, currentNode.rightIdx)

        # Creamos el subarabol izq y der
        # llamamos la función build con el hijo izq y der
        self.build(currentNode.leftChild)
        self.build(currentNode.rightChild)

        # Mezclamos los valores de los dos hijos en el nodo actuals
        currentNode.key = currentNode.leftChild.key + currentNode.rightChild.key

    def __build(self):
        self.build(self.root)

    def update(self, currentNode, addValue, idx):
        # Si terminamos de recorrer la rama
        if currentNode == None:
            return

        # Chechar si el rango del actual contiene al indicie a modifcar
        if idx < currentNode.leftIdx or idx > currentNode.rightIdx:
            return

        # Modificar el valor del nodo
        # Hacer llamada recurisva para modificiar el valor de sus hijos
        currentNode.key += addValue
        self.update(currentNode.leftChild, addValue, idx)
        self.update(currentNode.rightChild, addValue, idx)

    def update2(self, currentNode, newValue, idx):
        # Si terminamos de recorrer la rama
        if currentNode == None:
            return
        # Chechar si el rango del actual contiene al indicie a modifcar
        if idx < currentNode.leftIdx or idx > currentNode.rightIdx:
            return

        if currentNode.leftIdx == currentNode.rightIdx:
            currentNode.key = newValue
            return

        # Modificar el valor del nodo
        # Hacer llamada recurisva para modificiar el valor de sus hijos
        self.update2(currentNode.leftChild, newValue, idx)
        self.update2(currentNode.rightChild, newValue, idx)

        currentNode.key = currentNode.leftChild.key + currentNode.rightChild.key

    def getSum(self, currentNode, l, r):
        if currentNode is None:
            return 0
        # si el indice del nodo este fuera del rango no sumamos nada
        if r < currentNode.leftIdx or l > currentNode.rightIdx:
            return 0
        # si el indice del nodo está dentro del rango retornamos el valor del nodo
        elif l <= currentNode.leftIdx and r >= currentNode.rightIdx:
            return currentNode.key
        # si el nodo está parcialmente dentro del rango, volvermos a llamar la función tanto con el hijo izquierdo como el derecho
        else:
            return self.getSum(currentNode.leftChild, l, r)+self.getSum(currentNode.rightChild, l, r)


numbers = [5, 4, 3, 2, 10, 0, 3, 4]
print("Arreglo orginal: ", numbers)

st = segmentTree(numbers)
st.build(st.root)
print("Obtenemos suma del 2-5: ", st.getSum(st.root, 2, 5))

st.update(st.root, 6, 4)
print("\nSumanos 6 al nodo 4\nVolvemos a obtener la suma del 2-5: ",
      st.getSum(st.root, 2, 5))

st.update2(st.root, 0, 3)
print("\nCambiamos al nodo 3 dandole el valor de 0\nVolvemos a obtener la suma del 2-5: ",
      st.getSum(st.root, 2, 5), "\n")
