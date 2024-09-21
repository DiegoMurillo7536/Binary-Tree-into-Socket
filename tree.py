from node import Node


class ArbolBinario:
    def __init__(self):
        self.root = None

    def insertar(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insertar_recursivo(value, self.root)

    def _insertar_recursivo(self, value, actual_node):
        if value < actual_node.value:
            if actual_node.left is None:
                actual_node.left = Node(value)
            else:
                self._insertar_recursivo(value, actual_node.left)
        elif value > actual_node.value:
            if actual_node.right is None:
                actual_node.right = Node(value)
            else:
                self._insertar_recursivo(value, actual_node.right)
        elif value == actual_node.value:
            print(f"El valor {value} ya está en el árbol.")

    def buscar(self, value):
        return self._buscar_recursivo(value, self.root)

    def _buscar_recursivo(self, value, actual_node):
        if actual_node is None:
            return False
        elif value == actual_node.value:
            return True
        elif value < actual_node.value:
            return self._buscar_recursivo(value, actual_node.left)
        else:
            return self._buscar_recursivo(value, actual_node.right)

    def recorrer_inorden(self):
        elementos = []
        self._recorrer_inorden_recursivo(self.root, elementos)
        print(f"Árbol sin números repetidos {elementos}")

        return elementos

    def _recorrer_inorden_recursivo(self, actual_node, elementos):
        if actual_node:
            self._recorrer_inorden_recursivo(actual_node.left, elementos)
            elementos.append(actual_node.value)
            self._recorrer_inorden_recursivo(actual_node.right, elementos)

    def recorrer_preorden(self):
        elementos = []
        self._recorrer_preorden_recursivo(self.root, elementos)
        return elementos

    def _recorrer_preorden_recursivo(self, actual_node, elementos):
        if actual_node:
            elementos.append(actual_node.value)
            self._recorrer_preorden_recursivo(actual_node.left, elementos)
            self._recorrer_preorden_recursivo(actual_node.right, elementos)

    def recorrer_postorden(self):
        elementos = []
        self._recorrer_postorden_recursivo(self.root, elementos)
        return elementos

    def _recorrer_postorden_recursivo(self, actual_node, elementos):
        if actual_node:
            self._recorrer_postorden_recursivo(actual_node.left, elementos)
            self._recorrer_postorden_recursivo(actual_node.right, elementos)
            elementos.append(actual_node.value)
