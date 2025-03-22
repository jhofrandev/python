"""
  Matrices y Listas Enlazadas en Python
  
  Este archivo explora la implementación y uso de matrices (arrays multidimensionales)
  y listas enlazadas, dos estructuras de datos fundamentales en programación.
"""

################################################################################
## Matrices (Arrays Multidimensionales)
################################################################################

# En Python, las matrices se implementan comúnmente usando listas anidadas
# o bibliotecas especializadas como NumPy

# 1. Matrices usando listas anidadas
print("\n--- Matrices con listas anidadas ---")

# Crear una matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acceder a elementos
print(f"Elemento en posición [1][2]: {matriz[1][2]}")  # Fila 1, columna 2 (valor 6)

# Modificar un elemento
matriz[0][1] = 20
print(f"Matriz después de modificar [0][1]: {matriz}")

# Recorrer una matriz
print("Recorriendo la matriz:")
for fila in matriz:
    for elemento in fila:
        print(f"{elemento:2d}", end=" ")
    print()  # Nueva línea después de cada fila

# Crear una matriz con comprensión de listas
matriz_3x4 = [[i*4+j+1 for j in range(4)] for i in range(3)]
print(f"Matriz 3x4 creada con comprensión de listas:")
for fila in matriz_3x4:
    print(fila)

# 2. Matrices con NumPy (biblioteca especializada para cálculo numérico)
try:
    import numpy as np
    print("\n--- Matrices con NumPy ---")
    
    # Crear una matriz 3x3
    np_matriz = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    print(f"Matriz NumPy:\n{np_matriz}")
    
    # Crear matrices con funciones especiales
    zeros = np.zeros((2, 3))  # Matriz 2x3 de ceros
    print(f"Matriz de ceros:\n{zeros}")
    
    ones = np.ones((3, 2))  # Matriz 3x2 de unos
    print(f"Matriz de unos:\n{ones}")
    
    identidad = np.eye(3)  # Matriz identidad 3x3
    print(f"Matriz identidad:\n{identidad}")
    
    # Operaciones matriciales
    matriz_a = np.array([[1, 2], [3, 4]])
    matriz_b = np.array([[5, 6], [7, 8]])
    
    # Suma de matrices
    suma = matriz_a + matriz_b
    print(f"Suma de matrices:\n{suma}")
    
    # Multiplicación elemento a elemento
    mult_elem = matriz_a * matriz_b
    print(f"Multiplicación elemento a elemento:\n{mult_elem}")
    
    # Multiplicación matricial
    mult_mat = np.matmul(matriz_a, matriz_b)  # o matriz_a @ matriz_b en Python 3.5+
    print(f"Multiplicación matricial:\n{mult_mat}")
    
    # Transposición
    transpuesta = np_matriz.T
    print(f"Matriz transpuesta:\n{transpuesta}")
    
    # Reshape (cambiar forma)
    reshape = np.arange(1, 10).reshape(3, 3)
    print(f"Matriz con reshape:\n{reshape}")
    
except ImportError:
    print("NumPy no está instalado. Instálalo con 'pip install numpy'")

################################################################################
## Operaciones con matrices usando listas anidadas
################################################################################

print("\n--- Operaciones con matrices (listas anidadas) ---")

# Función para imprimir una matriz de forma legible
def imprimir_matriz(matriz, nombre="Matriz"):
    print(f"{nombre}:")
    for fila in matriz:
        print([f"{x:2d}" if isinstance(x, int) else f"{x:.2f}" for x in fila])

# Suma de matrices
def sumar_matrices(matriz_a, matriz_b):
    if len(matriz_a) != len(matriz_b) or len(matriz_a[0]) != len(matriz_b[0]):
        raise ValueError("Las matrices deben tener las mismas dimensiones")
    
    resultado = []
    for i in range(len(matriz_a)):
        fila = []
        for j in range(len(matriz_a[0])):
            fila.append(matriz_a[i][j] + matriz_b[i][j])
        resultado.append(fila)
    
    return resultado

# Multiplicación de matrices
def multiplicar_matrices(matriz_a, matriz_b):
    if len(matriz_a[0]) != len(matriz_b):
        raise ValueError("El número de columnas de A debe ser igual al número de filas de B")
    
    resultado = []
    for i in range(len(matriz_a)):
        fila = []
        for j in range(len(matriz_b[0])):
            suma = 0
            for k in range(len(matriz_b)):
                suma += matriz_a[i][k] * matriz_b[k][j]
            fila.append(suma)
        resultado.append(fila)
    
    return resultado

# Transponer una matriz
def transponer_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    
    resultado = []
    for j in range(columnas):
        fila = []
        for i in range(filas):
            fila.append(matriz[i][j])
        resultado.append(fila)
    
    return resultado

# Ejemplos de uso
matriz_a = [
    [1, 2],
    [3, 4]
]

matriz_b = [
    [5, 6],
    [7, 8]
]

imprimir_matriz(matriz_a, "Matriz A")
imprimir_matriz(matriz_b, "Matriz B")

# Suma
suma = sumar_matrices(matriz_a, matriz_b)
imprimir_matriz(suma, "A + B")

# Multiplicación
producto = multiplicar_matrices(matriz_a, matriz_b)
imprimir_matriz(producto, "A × B")

# Transposición
transpuesta = transponer_matriz(matriz_a)
imprimir_matriz(transpuesta, "Transpuesta de A")

################################################################################
## Listas Enlazadas
################################################################################

print("\n--- Listas Enlazadas ---")

# Implementación básica de una lista enlazada simple
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
    
    def __str__(self):
        return str(self.dato)

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.longitud = 0
    
    def esta_vacia(self):
        return self.cabeza is None
    
    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        
        self.longitud += 1
    
    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        
        self.longitud += 1
    
    def insertar(self, posicion, dato):
        if posicion < 0 or posicion > self.longitud:
            raise IndexError("Posición fuera de rango")
        
        if posicion == 0:
            self.agregar_al_inicio(dato)
            return
        
        if posicion == self.longitud:
            self.agregar_al_final(dato)
            return
        
        nuevo_nodo = Nodo(dato)
        actual = self.cabeza
        
        for _ in range(posicion - 1):
            actual = actual.siguiente
        
        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente = nuevo_nodo
        self.longitud += 1
    
    def eliminar_al_inicio(self):
        if self.esta_vacia():
            raise ValueError("La lista está vacía")
        
        dato = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        
        if self.cabeza is None:
            self.cola = None
        
        self.longitud -= 1
        return dato
    
    def eliminar_al_final(self):
        if self.esta_vacia():
            raise ValueError("La lista está vacía")
        
        if self.cabeza == self.cola:
            dato = self.cabeza.dato
            self.cabeza = None
            self.cola = None
            self.longitud -= 1
            return dato
        
        actual = self.cabeza
        while actual.siguiente != self.cola:
            actual = actual.siguiente
        
        dato = self.cola.dato
        self.cola = actual
        self.cola.siguiente = None
        self.longitud -= 1
        return dato
    
    def eliminar(self, posicion):
        if self.esta_vacia():
            raise ValueError("La lista está vacía")
        
        if posicion < 0 or posicion >= self.longitud:
            raise IndexError("Posición fuera de rango")
        
        if posicion == 0:
            return self.eliminar_al_inicio()
        
        if posicion == self.longitud - 1:
            return self.eliminar_al_final()
        
        actual = self.cabeza
        
        for _ in range(posicion - 1):
            actual = actual.siguiente
        
        dato = actual.siguiente.dato
        actual.siguiente = actual.siguiente.siguiente
        self.longitud -= 1
        return dato
    
    def obtener(self, posicion):
        if posicion < 0 or posicion >= self.longitud:
            raise IndexError("Posición fuera de rango")
        
        actual = self.cabeza
        
        for _ in range(posicion):
            actual = actual.siguiente
        
        return actual.dato
    
    def buscar(self, dato):
        actual = self.cabeza
        posicion = 0
        
        while actual:
            if actual.dato == dato:
                return posicion
            actual = actual.siguiente
            posicion += 1
        
        return -1
    
    def __len__(self):
        return self.longitud
    
    def __str__(self):
        if self.esta_vacia():
            return "[]"
        
        resultado = []
        actual = self.cabeza
        
        while actual:
            resultado.append(str(actual.dato))
            actual = actual.siguiente
        
        return "[" + " -> ".join(resultado) + "]"

# Ejemplo de uso de la lista enlazada
print("\nEjemplo de Lista Enlazada Simple:")
lista = ListaEnlazada()

# Agregar elementos
lista.agregar_al_final(10)
lista.agregar_al_final(20)
lista.agregar_al_inicio(5)
lista.insertar(2, 15)

print(f"Lista después de agregar elementos: {lista}")
print(f"Longitud de la lista: {len(lista)}")

# Acceder a elementos
print(f"Elemento en posición 2: {lista.obtener(2)}")
print(f"Posición del elemento 15: {lista.buscar(15)}")

# Eliminar elementos
eliminado = lista.eliminar(1)
print(f"Elemento eliminado en posición 1: {eliminado}")
print(f"Lista después de eliminar: {lista}")

################################################################################
## Lista Doblemente Enlazada
################################################################################

print("\n--- Lista Doblemente Enlazada ---")

class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None
    
    def __str__(self):
        return str(self.dato)

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.longitud = 0
    
    def esta_vacia(self):
        return self.cabeza is None
    
    def agregar_al_final(self, dato):
        nuevo_nodo = NodoDoble(dato)
        
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        
        self.longitud += 1
    
    def agregar_al_inicio(self, dato):
        nuevo_nodo = NodoDoble(dato)
        
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        
        self.longitud += 1
    
    def eliminar_al_inicio(self):
        if self.esta_vacia():
            raise ValueError("La lista está vacía")
        
        dato = self.cabeza.dato
        
        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None
        
        self.longitud -= 1
        return dato
    
    def eliminar_al_final(self):
        if self.esta_vacia():
            raise ValueError("La lista está vacía")
        
        dato = self.cola.dato
        
        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
        
        self.longitud -= 1
        return dato
    
    def __len__(self):
        return self.longitud
    
    def __str__(self):
        if self.esta_vacia():
            return "[]"
        
        resultado = []
        actual = self.cabeza
        
        while actual:
            resultado.append(str(actual.dato))
            actual = actual.siguiente
        
        return "[" + " <-> ".join(resultado) + "]"

# Ejemplo de uso de la lista doblemente enlazada
print("\nEjemplo de Lista Doblemente Enlazada:")
lista_doble = ListaDoblementeEnlazada()

# Agregar elementos
lista_doble.agregar_al_final(10)
lista_doble.agregar_al_final(20)
lista_doble.agregar_al_inicio(5)

print(f"Lista después de agregar elementos: {lista_doble}")

# Eliminar elementos
eliminado = lista_doble.eliminar_al_inicio()
print(f"Elemento eliminado al inicio: {eliminado}")
print(f"Lista después de eliminar al inicio: {lista_doble}")

eliminado = lista_doble.eliminar_al_final()
print(f"Elemento eliminado al final: {eliminado}")
print(f"Lista después de eliminar al final: {lista_doble}")

################################################################################
## Lista Circular
################################################################################

print("\n--- Lista Circular ---")

class ListaCircular:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.longitud = 0
    
    def esta_vacia(self):
        return self.cabeza is None
    
    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
            nuevo_nodo.siguiente = nuevo_nodo  # Apunta a sí mismo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        
        self.longitud += 1
    
    def eliminar(self, dato):
        if self.esta_vacia():
            raise ValueError("La lista está vacía")
        
        if self.cabeza == self.cola and self.cabeza.dato == dato:
            self.cabeza = None
            self.cola = None
            self.longitud = 0
            return True
        
        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            self.cola.siguiente = self.cabeza
            self.longitud -= 1
            return True
        
        actual = self.cabeza
        while actual.siguiente != self.cabeza:
            if actual.siguiente.dato == dato:
                if actual.siguiente == self.cola:
                    self.cola = actual
                actual.siguiente = actual.siguiente.siguiente
                self.longitud -= 1
                return True
            actual = actual.siguiente
        
        return False
    
    def __len__(self):
        return self.longitud
    
    def __str__(self):
        if self.esta_vacia():
            return "[]"
        
        resultado = []
        actual = self.cabeza
        
        # Recorrer hasta volver a la cabeza
        while True:
            resultado.append(str(actual.dato))
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        
        return "[" + " -> ".join(resultado) + " -> ...]"

# Ejemplo de uso de la lista circular
print("\nEjemplo de Lista Circular:")
lista_circular = ListaCircular()

# Agregar elementos
lista_circular.agregar(10)
lista_circular.agregar(20)
lista_circular.agregar(30)
lista_circular.agregar(40)

print(f"Lista circular: {lista_circular}")
print(f"Longitud: {len(lista_circular)}")

# Eliminar un elemento
eliminado = lista_circular.eliminar(20)
print(f"¿Se eliminó el elemento 20? {eliminado}")
print(f"Lista después de eliminar: {lista_circular}")

################################################################################
## Aplicaciones prácticas
################################################################################

print("\n--- Aplicaciones Prácticas ---")

# 1. Uso de matrices para procesamiento de imágenes (simulado)
print("\n1. Procesamiento de imágenes con matrices")

# Simular una imagen pequeña en escala de grises (0-255)
imagen = [
    [50, 100, 150],
    [100, 150, 200],
    [150, 200, 250]
]

imprimir_matriz(imagen, "Imagen original")

# Aplicar un filtro de brillo (aumentar en 50)
def aplicar_brillo(imagen, incremento):
    resultado = []
    for fila in imagen:
        nueva_fila = []
        for pixel in fila:
            # Asegurar que el valor esté entre 0 y 255
            nuevo_valor = max(0, min(255, pixel + incremento))
            nueva_fila.append(nuevo_valor)
        resultado.append(nueva_fila)
    return resultado

imagen_brillante = aplicar_brillo(imagen, 50)
imprimir_matriz(imagen_brillante, "Imagen con brillo aumentado")

# 2. Uso de listas enlazadas para historial de navegación
print("\n2. Historial de navegación con listas enlazadas")

class HistorialNavegacion:
    def __init__(self):
        self.historial = ListaEnlazada()
        self.posicion_actual = -1
    
    def visitar(self, url):
        # Si estamos en medio del historial, eliminar todo lo que está adelante
        while self.posicion_actual < len(self.historial) - 1:
            self.historial.eliminar_al_final()
        
        self.historial.agregar_al_final(url)
        self.posicion_actual = len(self.historial) - 1
        print(f"Visitando: {url}")
    
    def atras(self):
        if self.posicion_actual > 0:
            self.posicion_actual -= 1
            url = self.historial.obtener(self.posicion_actual)
            print(f"Retrocediendo a: {url}")
            return url
        else:
            print("No hay páginas anteriores")
            return None
    
    def adelante(self):
        if self.posicion_actual < len(self.historial) - 1:
            self.posicion_actual += 1
            url = self.historial.obtener(self.posicion_actual)
            print(f"Avanzando a: {url}")
            return url
        else:
            print("No hay páginas siguientes")
            return None
    
    def mostrar_historial(self):
        print("Historial de navegación:")
        for i in range(len(self.historial)):
            marca = " (actual)" if i == self.posicion_actual else ""
            print(f"  {i+1}. {self.historial.obtener(i)}{marca}")

# Ejemplo de uso del historial de navegación
navegador = HistorialNavegacion()
navegador.visitar("https://www.ejemplo.com")
navegador.visitar("https://www.ejemplo.com/pagina1")
navegador.visitar("https://www.ejemplo.com/pagina2")

navegador.mostrar_historial()

navegador.atras()
navegador.mostrar_historial()

navegador.visitar("https://www.ejemplo.com/pagina3")
navegador.mostrar_historial()

navegador.atras()
navegador.atras()
navegador.adelante()
navegador.mostrar_historial()

# 3. Uso de lista circular para un sistema de turnos
print("\n3. Sistema de turnos con lista circular")

class SistemaTurnos:
    def __init__(self):
        self.turnos = ListaCircular()
        self.turno_actual = None
    
    def agregar_participante(self, nombre):
        self.turnos.agregar(nombre)
        if self.turno_actual is None and not self.turnos.esta_vacia():
            self.turno_actual = self.turnos.cabeza
        print(f"Participante agregado: {nombre}")
    
    def siguiente_turno(self):
        if self.turnos.esta_vacia():
            print("No hay participantes")
            return None
        
        if self.turno_actual is None:
            self.turno_actual = self.turnos.cabeza
        else:
            self.turno_actual = self.turno_actual.siguiente
        
        print(f"Turno de: {self.turno_actual.dato}")
        return self.turno_actual.dato
    
    def eliminar_participante(self, nombre):
        if self.turnos.eliminar(nombre):
            print(f"Participante eliminado: {nombre}")
            if self.turnos.esta_vacia():
                self.turno_actual = None
            elif self.turno_actual.dato == nombre:
                self.turno_actual = self.turno_actual.siguiente
        else:
            print(f"Participante no encontrado: {nombre}")
    
    def mostrar_participantes(self):
        print("Participantes:")
        print(self.turnos)

# Ejemplo de uso del sistema de turnos
sistema = SistemaTurnos()
sistema.agregar_participante("Ana")
sistema.agregar_participante("Juan")
sistema.agregar_participante("María")
sistema.agregar_participante("Pedro")

sistema.mostrar_participantes()

for _ in range(6):  # Dar 6 turnos
    sistema.siguiente_turno()

sistema.eliminar_participante("Juan")
sistema.mostrar_participantes()

for _ in range(3):  # Dar 3 turnos más
    sistema.siguiente_turno()

################################################################################
## Comparación de rendimiento
################################################################################

print("\n--- Comparación de Rendimiento ---")

import time

# Comparar acceso a elementos en lista Python vs. lista enlazada
def comparar_acceso():
    tamaño = 10000
    
    # Crear lista Python
    lista_python = list(range(tamaño))
    
    # Crear lista enlazada
    lista_enlazada = ListaEnlazada()
    for i in range(tamaño):
        lista_enlazada.agregar_al_final(i)
    
    # Medir tiempo de acceso a elementos en lista Python
    inicio = time.time()
    for _ in range(100):
        elemento = lista_python[tamaño // 2]
    fin = time.time()
    tiempo_lista = fin - inicio
    
    # Medir tiempo de acceso a elementos en lista enlazada
    inicio = time.time()
    for _ in range(100):
        elemento = lista_enlazada.obtener(tamaño // 2)
    fin = time.time()
    tiempo_enlazada = fin - inicio
    
    print(f"Tiempo de acceso a elemento medio (100 veces):")
    print(f"  Lista Python: {tiempo_lista:.6f} segundos")
    print(f"  Lista Enlazada: {tiempo_enlazada:.6f} segundos")
    print(f"  La lista Python es {tiempo_enlazada/tiempo_lista:.1f} veces más rápida para acceso")

# Comparar inserción al inicio en lista Python vs. lista enlazada
def comparar_insercion_inicio():
    tamaño = 10000
    
    # Medir tiempo de inserción al inicio en lista Python
    lista_python = []
    inicio = time.time()
    for i in range(tamaño):
        lista_python.insert(0, i)
    fin = time.time()
    tiempo_lista = fin - inicio
    
    # Medir tiempo de inserción al inicio en lista enlazada
    lista_enlazada = ListaEnlazada()
    inicio = time.time()
    for i in range(tamaño):
        lista_enlazada.agregar_al_inicio(i)
    fin = time.time()
    tiempo_enlazada = fin - inicio
    
    print(f"\nTiempo de inserción al inicio ({tamaño} elementos):")
    print(f"  Lista Python: {tiempo_lista:.6f} segundos")
    print(f"  Lista Enlazada: {tiempo_enlazada:.6f} segundos")
    print(f"  La lista enlazada es {tiempo_lista/tiempo_enlazada:.1f} veces más rápida para inserción al inicio")

# Ejecutar comparaciones
comparar_acceso()
comparar_insercion_inicio()

################################################################################
## Conclusiones
################################################################################

print("\n--- Conclusiones ---")
print("""
1. Matrices:
   - Eficientes para acceso aleatorio a elementos
   - Útiles para algoritmos que requieren acceso por índice
   - NumPy proporciona operaciones matriciales optimizadas

2. Listas Enlazadas:
   - Eficientes para inserción/eliminación al inicio
   - No requieren reubicación de elementos
   - Útiles cuando el tamaño cambia frecuentemente
   - Tipos: simples, dobles, circulares

3. Comparación:
   - Listas Python (arrays): mejor para acceso aleatorio
   - Listas enlazadas: mejor para inserción/eliminación frecuente
   - La elección depende del caso de uso específico

4. Aplicaciones:
   - Matrices: procesamiento de imágenes, cálculos científicos
   - Listas enlazadas: historial de navegación, sistemas de turnos
""")