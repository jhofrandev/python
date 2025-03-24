################################################################################## ¿Qué es un Árbol de Búsqueda Binaria (BST)?
################################################################################
'''
Un árbol de búsqueda binaria es una estructura de datos en forma de árbol donde:
- Cada nodo tiene como máximo dos hijos (izquierdo y derecho)
- Para cualquier nodo, todos los elementos en su subárbol izquierdo son menores que él
- Para cualquier nodo, todos los elementos en su subárbol derecho son mayores que él

Esta organización permite búsquedas muy eficientes, ya que en cada paso podemos descartar aproximadamente la mitad de los elementos restantes.
'''

################################################################################## Implementación básica en Python
################################################################################

"""
  Árboles de Búsqueda Binaria en Python
  
  Este archivo explora la implementación y uso de árboles de búsqueda binaria,
  una estructura de datos fundamental para búsquedas eficientes.
"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)
    
    def _insertar_recursivo(self, nodo_actual, valor):
        # Si el valor es menor, vamos a la izquierda
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, valor)
        # Si el valor es mayor o igual, vamos a la derecha
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.derecho, valor)
    
    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)
    
    def _buscar_recursivo(self, nodo_actual, valor):
        # Caso base: no encontramos el valor o llegamos a un nodo vacío
        if nodo_actual is None:
            return False
        
        # Encontramos el valor
        if nodo_actual.valor == valor:
            return True
        
        # Si el valor es menor, buscamos a la izquierda
        if valor < nodo_actual.valor:
            return self._buscar_recursivo(nodo_actual.izquierdo, valor)
        # Si el valor es mayor, buscamos a la derecha
        else:
            return self._buscar_recursivo(nodo_actual.derecho, valor)
    
    def recorrido_inorden(self):
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado
    
    def _inorden_recursivo(self, nodo, resultado):
        if nodo:
            # Primero recorremos el subárbol izquierdo
            self._inorden_recursivo(nodo.izquierdo, resultado)
            # Luego visitamos el nodo actual
            resultado.append(nodo.valor)
            # Finalmente recorremos el subárbol derecho
            self._inorden_recursivo(nodo.derecho, resultado)
    
    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)
    
    def _eliminar_recursivo(self, nodo, valor):
        # Caso base: árbol vacío
        if nodo is None:
            return None
        
        # Buscar el nodo a eliminar
        if valor < nodo.valor:
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, valor)
        else:
            # Caso 1: Nodo hoja (sin hijos)
            if nodo.izquierdo is None and nodo.derecho is None:
                return None
            
            # Caso 2: Nodo con un solo hijo
            elif nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo
            
            # Caso 3: Nodo con dos hijos
            # Encontrar el sucesor inorden (el menor valor en el subárbol derecho)
            sucesor = self._encontrar_minimo(nodo.derecho)
            nodo.valor = sucesor.valor
            # Eliminar el sucesor
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, sucesor.valor)
        
        return nodo
    
    def _encontrar_minimo(self, nodo):
        actual = nodo
        # El valor mínimo siempre está en el extremo izquierdo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual

# Ejemplo de uso
arbol = ArbolBinarioBusqueda()

# Insertar elementos
print("Insertando elementos: 50, 30, 70, 20, 40, 60, 80")
arbol.insertar(50)
arbol.insertar(30)
arbol.insertar(70)
arbol.insertar(20)
arbol.insertar(40)
arbol.insertar(60)
arbol.insertar(80)

# Buscar elementos
print(f"¿Existe el valor 40? {arbol.buscar(40)}")
print(f"¿Existe el valor 90? {arbol.buscar(90)}")

# Recorrido inorden (debe mostrar los elementos ordenados)
print(f"Recorrido inorden: {arbol.recorrido_inorden()}")

# Eliminar un elemento
print("Eliminando el elemento 30...")
arbol.eliminar(30)
print(f"Recorrido inorden después de eliminar: {arbol.recorrido_inorden()}")

# Visualización simple del árbol (para árboles pequeños)
def visualizar_arbol(nodo, nivel=0, prefijo="Raíz: "):
    if nodo is not None:
        print(" " * (nivel * 4) + prefijo + str(nodo.valor))
        visualizar_arbol(nodo.izquierdo, nivel + 1, "Izq: ")
        visualizar_arbol(nodo.derecho, nivel + 1, "Der: ")

print("\nEstructura del árbol:")
visualizar_arbol(arbol.raiz)

# Aplicaciones prácticas
print("\nAplicaciones prácticas de los árboles de búsqueda binaria:")
print("1. Búsquedas eficientes en conjuntos de datos ordenados")
print("2. Implementación de diccionarios y conjuntos")
print("3. Bases de datos (índices)")
print("4. Algoritmos de compresión")
print("5. Sistemas de archivos")

################################################################################## Implementación básica en Python
################################################################################

'''
1. Estructura jerárquica : Los BST organizan los datos en una jerarquía que facilita la búsqueda.

2. Operaciones principales :
   - Inserción : Añadir un nuevo valor manteniendo la propiedad del BST
   - Búsqueda : Encontrar un valor específico
   - Eliminación : Quitar un valor manteniendo la estructura
   - Recorridos : Visitar todos los nodos en un orden específico (inorden, preorden, postorden)

3. Eficiencia :
   - En un árbol balanceado, las operaciones tienen una complejidad de O(log n)
   - En el peor caso (árbol degenerado), pueden llegar a O(n)

## Ventajas de los BST
- Búsquedas más rápidas que en listas o arrays (en promedio)
- Mantienen los datos ordenados
- Permiten encontrar el mínimo y máximo rápidamente
- Facilitan encontrar el "siguiente" o "anterior" elemento

## Aplicaciones reales
Los árboles de búsqueda binaria se utilizan en:
- Sistemas de bases de datos para índices
- Implementaciones de conjuntos y mapas en lenguajes de programación
- Algoritmos de compresión
- Sistemas de archivos
- Algoritmos de enrutamiento en redes
'''