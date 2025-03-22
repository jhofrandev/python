"""
  Montones, Pilas y Colas en Python
  
  Este archivo explora la implementación y uso de estas estructuras de datos
  fundamentales para algoritmos y aplicaciones.
"""

################################################################################
## Montones (Heaps)
################################################################################

print("\n--- Montones (Heaps) ---")

"""
Un montón (heap) es una estructura de datos de árbol especializada que satisface
la propiedad de montón: en un montón máximo, para cualquier nodo, el valor del
nodo es mayor o igual que los valores de sus hijos. En un montón mínimo, el valor
del nodo es menor o igual que los valores de sus hijos.

Python implementa montones mínimos a través del módulo 'heapq'.
"""

import heapq

# Crear un montón a partir de una lista
numeros = [10, 5, 15, 3, 8, 1, 20]
heapq.heapify(numeros)  # Convierte la lista en un montón mínimo in-place
print(f"Montón mínimo: {numeros}")  # La lista ahora está organizada como un montón

# Insertar elementos en el montón
heapq.heappush(numeros, 2)
print(f"Después de insertar 2: {numeros}")

# Extraer el elemento más pequeño
menor = heapq.heappop(numeros)
print(f"Elemento más pequeño: {menor}")
print(f"Montón después de extraer: {numeros}")

# Obtener el elemento más pequeño sin extraerlo
print(f"Elemento más pequeño actual: {numeros[0]}")

# Obtener los n elementos más pequeños
print(f"3 elementos más pequeños: {heapq.nsmallest(3, [10, 5, 15, 3, 8, 1, 20])}")

# Obtener los n elementos más grandes
print(f"3 elementos más grandes: {heapq.nlargest(3, [10, 5, 15, 3, 8, 1, 20])}")

# Implementación de un montón máximo usando heapq (negando los valores)
numeros_max = [10, 5, 15, 3, 8, 1, 20]
numeros_max = [-n for n in numeros_max]  # Negar todos los valores
heapq.heapify(numeros_max)

# Extraer el elemento más grande (negando el resultado)
mayor = -heapq.heappop(numeros_max)
print(f"Elemento más grande: {mayor}")

################################################################################
## Pilas (Stacks)
################################################################################

print("\n--- Pilas (Stacks) ---")

"""
Una pila es una estructura de datos que sigue el principio LIFO (Last In, First Out),
donde el último elemento añadido es el primero en ser eliminado.

En Python, las pilas se pueden implementar fácilmente usando listas.
"""

# Implementación de una pila usando una lista
class Pila:
    def __init__(self):
        self.items = []
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.items.pop()
    
    def ver_tope(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.items[-1]
    
    def tamaño(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)

# Ejemplo de uso de la pila
pila = Pila()
print(f"¿La pila está vacía? {pila.esta_vacia()}")

# Apilar elementos
pila.apilar("A")
pila.apilar("B")
pila.apilar("C")
print(f"Pila después de apilar: {pila}")

# Ver el elemento en el tope
print(f"Elemento en el tope: {pila.ver_tope()}")

# Desapilar elementos
elemento = pila.desapilar()
print(f"Elemento desapilado: {elemento}")
print(f"Pila después de desapilar: {pila}")

# Ejemplo práctico: verificar paréntesis balanceados
def parentesis_balanceados(expresion):
    pila = []
    for char in expresion:
        if char in "([{":
            pila.append(char)
        elif char in ")]}":
            if not pila:
                return False
            
            tope = pila.pop()
            if (char == ")" and tope != "(") or \
               (char == "]" and tope != "[") or \
               (char == "}" and tope != "{"):
                return False
    
    return len(pila) == 0

print(f"¿'(a+b)' tiene paréntesis balanceados? {parentesis_balanceados('(a+b)')}")
print(f"¿'[(a+b)]' tiene paréntesis balanceados? {parentesis_balanceados('[(a+b)]')}")
print(f"¿'[(a+b)](' tiene paréntesis balanceados? {parentesis_balanceados('[(a+b)](')}")
print(f"¿'[(a+b]' tiene paréntesis balanceados? {parentesis_balanceados('[(a+b]')}")

################################################################################
## Colas (Queues)
################################################################################

print("\n--- Colas (Queues) ---")

"""
Una cola es una estructura de datos que sigue el principio FIFO (First In, First Out),
donde el primer elemento añadido es el primero en ser eliminado.

Python ofrece varias implementaciones de colas en sus módulos estándar.
"""

# 1. Implementación básica de una cola usando una lista
class Cola:
    def __init__(self):
        self.items = []
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def encolar(self, item):
        self.items.append(item)
    
    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self.items.pop(0)  # Ineficiente para colas grandes
    
    def ver_frente(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self.items[0]
    
    def tamaño(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)

# Ejemplo de uso de la cola
cola = Cola()
print(f"¿La cola está vacía? {cola.esta_vacia()}")

# Encolar elementos
cola.encolar("A")
cola.encolar("B")
cola.encolar("C")
print(f"Cola después de encolar: {cola}")

# Ver el elemento en el frente
print(f"Elemento en el frente: {cola.ver_frente()}")

# Desencolar elementos
elemento = cola.desencolar()
print(f"Elemento desencolado: {elemento}")
print(f"Cola después de desencolar: {cola}")

# 2. Implementación eficiente usando collections.deque
from collections import deque

print("\n--- Cola con deque ---")

# deque es una implementación de cola de doble extremo más eficiente
cola_deque = deque()

# Encolar elementos
cola_deque.append("A")
cola_deque.append("B")
cola_deque.append("C")
print(f"Cola deque: {cola_deque}")

# Desencolar elementos (desde la izquierda)
elemento = cola_deque.popleft()
print(f"Elemento desencolado: {elemento}")
print(f"Cola deque después de desencolar: {cola_deque}")

# 3. Cola de prioridad usando heapq
print("\n--- Cola de prioridad ---")

# Una cola de prioridad es una cola donde los elementos tienen prioridades asociadas
# y los elementos con mayor prioridad se procesan primero

class ColaPrioridad:
    def __init__(self):
        self.cola = []
        self.indice = 0  # Para desempatar elementos con la misma prioridad
    
    def encolar(self, item, prioridad):
        # Usamos prioridad negativa porque heapq implementa un montón mínimo
        heapq.heappush(self.cola, (prioridad, self.indice, item))
        self.indice += 1
    
    def desencolar(self):
        if not self.cola:
            raise IndexError("La cola de prioridad está vacía")
        return heapq.heappop(self.cola)[2]  # Devolver solo el item
    
    def esta_vacia(self):
        return len(self.cola) == 0
    
    def __str__(self):
        return str([(prioridad, item) for prioridad, _, item in self.cola])

# Ejemplo de uso de la cola de prioridad
cola_prioridad = ColaPrioridad()
cola_prioridad.encolar("Tarea A", 3)  # Menor número = mayor prioridad
cola_prioridad.encolar("Tarea B", 1)
cola_prioridad.encolar("Tarea C", 2)
print(f"Cola de prioridad: {cola_prioridad}")

# Desencolar elementos (primero los de mayor prioridad)
print(f"Elemento desencolado: {cola_prioridad.desencolar()}")
print(f"Elemento desencolado: {cola_prioridad.desencolar()}")
print(f"Cola de prioridad después de desencolar: {cola_prioridad}")

################################################################################
## Aplicaciones prácticas
################################################################################

print("\n--- Aplicaciones prácticas ---")

# 1. Búsqueda en anchura (BFS) usando una cola
print("\n1. Búsqueda en anchura (BFS)")

def bfs(grafo, inicio):
    visitados = set()
    cola = deque([inicio])
    visitados.add(inicio)
    
    while cola:
        vertice = cola.popleft()
        print(f"Visitando: {vertice}")
        
        for vecino in grafo[vertice]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
    
    return visitados

# Ejemplo de grafo representado como un diccionario de adyacencia
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("Recorrido BFS del grafo:")
bfs(grafo, 'A')

# 2. Búsqueda en profundidad (DFS) usando una pila
print("\n2. Búsqueda en profundidad (DFS)")

def dfs(grafo, inicio):
    visitados = set()
    pila = [inicio]
    
    while pila:
        vertice = pila.pop()
        if vertice not in visitados:
            print(f"Visitando: {vertice}")
            visitados.add(vertice)
            
            # Agregar vecinos no visitados a la pila (en orden inverso para mantener el orden original)
            for vecino in reversed(grafo[vertice]):
                if vecino not in visitados:
                    pila.append(vecino)
    
    return visitados

print("Recorrido DFS del grafo:")
dfs(grafo, 'A')

################################################################################
## Comparación de rendimiento
################################################################################

print("\n--- Comparación de rendimiento ---")

import time
import random

# Comparar operaciones de inserción y extracción en diferentes estructuras
def comparar_rendimiento():
    n = 10000
    datos = list(range(n))
    random.shuffle(datos)
    
    # 1. Montón (heap)
    print("\nRendimiento de un montón (heap):")
    
    # Inserción
    inicio = time.time()
    heap = []
    for item in datos:
        heapq.heappush(heap, item)
    fin = time.time()
    print(f"Tiempo de inserción de {n} elementos: {fin - inicio:.6f} segundos")
    
    # Extracción
    inicio = time.time()
    while heap:
        heapq.heappop(heap)
    fin = time.time()
    print(f"Tiempo de extracción de {n} elementos: {fin - inicio:.6f} segundos")
    
    # 2. Pila (usando lista)
    print("\nRendimiento de una pila (lista):")
    
    # Inserción
    inicio = time.time()
    pila = []
    for item in datos:
        pila.append(item)
    fin = time.time()
    print(f"Tiempo de inserción de {n} elementos: {fin - inicio:.6f} segundos")
    
    # Extracción
    inicio = time.time()
    while pila:
        pila.pop()
    fin = time.time()
    print(f"Tiempo de extracción de {n} elementos: {fin - inicio:.6f} segundos")
    
    # 3. Cola (usando deque)
    print("\nRendimiento de una cola (deque):")
    
    # Inserción
    inicio = time.time()
    cola = deque()
    for item in datos:
        cola.append(item)
    fin = time.time()
    print(f"Tiempo de inserción de {n} elementos: {fin - inicio:.6f} segundos")
    
    # Extracción
    inicio = time.time()
    while cola:
        cola.popleft()
    fin = time.time()
    print(f"Tiempo de extracción de {n} elementos: {fin - inicio:.6f} segundos")
    
    # 4. Cola (usando lista)
    print("\nRendimiento de una cola (lista):")
    
    # Inserción
    inicio = time.time()
    cola_lista = []
    for item in datos:
        cola_lista.append(item)
    fin = time.time()
    print(f"Tiempo de inserción de {n} elementos: {fin - inicio:.6f} segundos")
    
    # Extracción (ineficiente)
    inicio = time.time()
    for _ in range(min(1000, len(cola_lista))):  # Limitamos a 1000 para no esperar demasiado
        cola_lista.pop(0)
    fin = time.time()
    tiempo_por_elemento = (fin - inicio) / min(1000, len(cola_lista))
    tiempo_estimado = tiempo_por_elemento * n
    print(f"Tiempo estimado de extracción de {n} elementos: {tiempo_estimado:.6f} segundos (basado en {min(1000, len(cola_lista))} extracciones)")

# Ejecutar comparación de rendimiento
comparar_rendimiento()

################################################################################
## Conclusiones
################################################################################

print("\n--- Conclusiones ---")
print("""
1. Montones (Heaps):
   - Eficientes para mantener el elemento mínimo/máximo
   - Útiles para colas de prioridad y algoritmos como Dijkstra
   - Operaciones principales: O(log n)
   - En Python: módulo heapq implementa montones mínimos

2. Pilas (Stacks):
   - Estructura LIFO (Last In, First Out)
   - Aplicaciones: evaluación de expresiones, algoritmos DFS, manejo de llamadas
   - Operaciones principales: O(1)
   - En Python: se implementan fácilmente con listas

3. Colas (Queues):
   - Estructura FIFO (First In, First Out)
   - Aplicaciones: algoritmos BFS, programación concurrente, simulaciones
   - Operaciones principales: O(1) con implementación adecuada
   - En Python: collections.deque es la implementación más eficiente

4. Comparación de rendimiento:
   - Pilas con listas: muy eficientes
   - Colas con deque: muy eficientes
   - Colas con listas: ineficientes para extracciones (O(n))
   - Montones: eficientes para mantener orden parcial

5. Variantes especializadas:
   - Cola de prioridad: para procesar elementos según su prioridad
   - Cola de doble extremo (deque): permite operaciones en ambos extremos
   - Cola circular: útil para buffers circulares y sistemas de turnos
""")

################################################################################
## Ejercicios prácticos
################################################################################

print("\n--- Ejercicios prácticos ---")
print("""
1. Implementar un algoritmo de ordenamiento heapsort completo
2. Crear una calculadora que soporte operaciones con paréntesis usando pilas
3. Implementar un sistema de gestión de tareas con prioridades usando colas
4. Desarrollar un algoritmo para verificar si un grafo tiene ciclos usando DFS
5. Implementar un buffer circular usando una cola
""")

# Ejemplo de solución para el ejercicio 1: Heapsort completo
def heapsort_completo(arr):
    # Convertir el arreglo en un montón máximo
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    
    n = len(arr)
    
    # Construir un montón máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extraer elementos uno por uno
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Intercambiar
        heapify(arr, i, 0)
    
    return arr

# Probar heapsort
arr = [12, 11, 13, 5, 6, 7]
print(f"\nArreglo original: {arr}")
print(f"Arreglo ordenado con heapsort: {heapsort_completo(arr)}")

# Ejemplo de solución para el ejercicio 2: Calculadora con paréntesis
def evaluar_expresion(expresion):
    def aplicar_operador(operadores, valores):
        operador = operadores.pop()
        derecho = valores.pop()
        izquierdo = valores.pop()
        if operador == '+':
            valores.append(izquierdo + derecho)
        elif operador == '-':
            valores.append(izquierdo - derecho)
        elif operador == '*':
            valores.append(izquierdo * derecho)
        elif operador == '/':
            valores.append(izquierdo / derecho)
    
    # Precedencia de operadores
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}
    
    # Pilas para operadores y valores
    operadores = []
    valores = []
    i = 0
    
    while i < len(expresion):
        if expresion[i] == ' ':
            i += 1
            continue
        
        # Si es un dígito, obtener el número completo
        if expresion[i].isdigit():
            numero = 0
            while i < len(expresion) and expresion[i].isdigit():
                numero = numero * 10 + int(expresion[i])
                i += 1
            valores.append(numero)
            continue
        
        # Si es un paréntesis de apertura
        if expresion[i] == '(':
            operadores.append(expresion[i])
        
        # Si es un paréntesis de cierre
        elif expresion[i] == ')':
            while operadores and operadores[-1] != '(':
                aplicar_operador(operadores, valores)
            
            # Eliminar el paréntesis de apertura
            if operadores and operadores[-1] == '(':
                operadores.pop()
        
        # Si es un operador
        elif expresion[i] in ['+', '-', '*', '/']:
            while (operadores and operadores[-1] != '(' and
                   precedencia.get(operadores[-1], 0) >= precedencia.get(expresion[i], 0)):
                aplicar_operador(operadores, valores)
            
            operadores.append(expresion[i])
        
        i += 1
    
    # Procesar los operadores restantes
    while operadores:
        aplicar_operador(operadores, valores)
    
    # El resultado final estará en la cima de la pila de valores
    return valores[0]

# Probar la calculadora
expresion = "3 + 4 * 2 / ( 1 - 5 )"
print(f"\nResultado de '{expresion}': {evaluar_expresion(expresion)}")

print("\n--- Resumen final ---")
print("""
Los montones, pilas y colas son estructuras de datos fundamentales en la programación:

- Los montones son ideales cuando necesitamos acceder rápidamente al elemento mínimo o máximo.
- Las pilas son perfectas para problemas donde el último elemento añadido debe ser el primero en procesarse.
- Las colas son esenciales cuando queremos procesar elementos en el mismo orden en que llegaron.

La elección de la estructura correcta puede tener un impacto significativo en el rendimiento
y la claridad de nuestros algoritmos. Python ofrece implementaciones eficientes
para todas estas estructuras, ya sea directamente en el lenguaje o a través de módulos
como heapq y collections.
""")