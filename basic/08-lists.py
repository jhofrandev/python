"""
  Las listas en Python son colecciones ordenadas y mutables de elementos.
  Son una de las estructuras de datos más versátiles y utilizadas en Python,
  permitiendo almacenar elementos de diferentes tipos en una misma lista.
"""

################################################################################
## Creación de listas
################################################################################

# Lista vacía
lista_vacia = []
lista_vacia_alternativa = list()

# Lista con elementos
numeros = [1, 2, 3, 4, 5]
frutas = ["manzana", "banana", "naranja"]
mixta = [1, "hola", 3.14, True, [1, 2]]  # Las listas pueden contener diferentes tipos de datos

# Crear lista a partir de otros iterables
lista_desde_tupla = list((1, 2, 3))
lista_desde_string = list("Python")  # ['P', 'y', 't', 'h', 'o', 'n']
lista_desde_rango = list(range(5))   # [0, 1, 2, 3, 4]

# Listas por comprensión (list comprehension)
cuadrados = [x**2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]
pares = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

################################################################################
## Acceso a elementos
################################################################################

# Acceso por índice (los índices comienzan en 0)
frutas = ["manzana", "banana", "naranja", "uva", "pera"]
print(frutas[0])  # manzana
print(frutas[2])  # naranja

# Índices negativos (cuentan desde el final)
print(frutas[-1])  # pera (último elemento)
print(frutas[-2])  # uva (penúltimo elemento)

# Slicing (rebanado): obtener sublistas
print(frutas[1:3])    # ['banana', 'naranja'] (desde índice 1 hasta 3-1)
print(frutas[:3])     # ['manzana', 'banana', 'naranja'] (desde el inicio hasta 3-1)
print(frutas[2:])     # ['naranja', 'uva', 'pera'] (desde índice 2 hasta el final)
print(frutas[-3:])    # ['naranja', 'uva', 'pera'] (últimos 3 elementos)
print(frutas[::2])    # ['manzana', 'naranja', 'pera'] (cada 2 elementos)
print(frutas[::-1])   # ['pera', 'uva', 'naranja', 'banana', 'manzana'] (invertir lista)

################################################################################
## Modificación de listas
################################################################################

# Cambiar un elemento
frutas = ["manzana", "banana", "naranja"]
frutas[1] = "kiwi"
print(frutas)  # ['manzana', 'kiwi', 'naranja']

# Añadir elementos
frutas.append("uva")  # Añade al final
print(frutas)  # ['manzana', 'kiwi', 'naranja', 'uva']

frutas.insert(1, "pera")  # Inserta en posición específica
print(frutas)  # ['manzana', 'pera', 'kiwi', 'naranja', 'uva']

frutas.extend(["melon", "sandia"])  # Añade múltiples elementos
print(frutas)  # ['manzana', 'pera', 'kiwi', 'naranja', 'uva', 'melon', 'sandia']

# También se puede usar el operador + para concatenar listas
mas_frutas = frutas + ["fresa", "cereza"]
print(mas_frutas)

# Eliminar elementos
frutas.remove("kiwi")  # Elimina por valor (primera ocurrencia)
print(frutas)  # ['manzana', 'pera', 'naranja', 'uva', 'melon', 'sandia']

eliminado = frutas.pop()  # Elimina y devuelve el último elemento
print(eliminado)  # 'sandia'
print(frutas)  # ['manzana', 'pera', 'naranja', 'uva', 'melon']

eliminado = frutas.pop(1)  # Elimina y devuelve el elemento en el índice 1
print(eliminado)  # 'pera'
print(frutas)  # ['manzana', 'naranja', 'uva', 'melon']

del frutas[0]  # Elimina el elemento en el índice 0
print(frutas)  # ['naranja', 'uva', 'melon']

# Limpiar la lista
frutas.clear()
print(frutas)  # []

################################################################################
## Operaciones comunes
################################################################################

numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# Longitud de la lista
print(len(numeros))  # 9

# Contar ocurrencias de un elemento
print(numeros.count(5))  # 2 (el número 5 aparece dos veces)

# Encontrar el índice de un elemento (primera ocurrencia)
print(numeros.index(4))  # 2 (el número 4 está en el índice 2)
# print(numeros.index(7))  # ValueError: 7 is not in list

# Ordenar la lista
numeros.sort()  # Modifica la lista original
print(numeros)  # [1, 1, 2, 3, 4, 5, 5, 6, 9]

numeros.sort(reverse=True)  # Orden descendente
print(numeros)  # [9, 6, 5, 5, 4, 3, 2, 1, 1]

# Ordenar sin modificar la original
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5]
ordenados = sorted(numeros)
print(ordenados)  # [1, 1, 2, 3, 4, 5, 5, 6, 9]
print(numeros)    # [3, 1, 4, 1, 5, 9, 2, 6, 5] (no se modifica)

# Invertir la lista
numeros.reverse()
print(numeros)  # [5, 6, 2, 9, 5, 1, 4, 1, 3]

# Copiar una lista
copia1 = numeros.copy()
copia2 = list(numeros)
copia3 = numeros[:]  # Usando slicing
print(copia1)  # [5, 6, 2, 9, 5, 1, 4, 1, 3]

################################################################################
## Listas anidadas (matrices)
################################################################################

# Crear una matriz (lista de listas)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acceder a elementos
print(matriz[1][2])  # 6 (fila 1, columna 2)

# Recorrer una matriz
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()  # Nueva línea después de cada fila

# Crear una matriz con comprensión de listas
matriz_3x3 = [[i*3+j+1 for j in range(3)] for i in range(3)]
print(matriz_3x3)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

################################################################################
## Verificaciones y pertenencia
################################################################################

frutas = ["manzana", "banana", "naranja", "uva"]

# Verificar si un elemento está en la lista
print("banana" in frutas)  # True
print("kiwi" in frutas)    # False

# Verificar si un elemento no está en la lista
print("kiwi" not in frutas)  # True

################################################################################
## Iteración sobre listas
################################################################################

# Recorrer elementos
for fruta in frutas:
    print(fruta)

# Recorrer con índice usando enumerate
for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")

# Recorrer múltiples listas en paralelo con zip
precios = [1.2, 0.8, 1.5, 2.0]
for fruta, precio in zip(frutas, precios):
    print(f"{fruta}: ${precio}")

################################################################################
## Funciones avanzadas con listas
################################################################################

numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# map: aplicar una función a cada elemento
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)  # [9, 1, 16, 1, 25, 81, 4, 36, 25]

# filter: filtrar elementos según una condición
mayores_que_3 = list(filter(lambda x: x > 3, numeros))
print(mayores_que_3)  # [4, 5, 9, 6, 5]

# reduce: reducir la lista a un solo valor
from functools import reduce
suma = reduce(lambda x, y: x + y, numeros)
print(suma)  # 36

################################################################################
## Desempaquetado de listas
################################################################################

coordenadas = [10, 20, 30]
x, y, z = coordenadas  # Desempaquetado
print(f"x={x}, y={y}, z={z}")  # x=10, y=20, z=30

# Desempaquetado con * (resto)
primero, *resto, ultimo = [1, 2, 3, 4, 5]
print(primero)  # 1
print(resto)    # [2, 3, 4]
print(ultimo)   # 5

################################################################################
## Rendimiento y consideraciones
################################################################################

# Las listas son eficientes para:
# - Acceso por índice: O(1)
# - Añadir/eliminar al final (append/pop): O(1)
# - Iterar sobre todos los elementos: O(n)

# Las listas son menos eficientes para:
# - Insertar/eliminar al principio o en medio: O(n)
# - Buscar elementos (in): O(n)
# - Ordenar: O(n log n)

################################################################################
## Buenas prácticas
################################################################################

# 1. Usar comprensiones de listas para código más conciso y legible
cuadrados = [x**2 for x in range(10)]  # Mejor que un bucle for tradicional

# 2. Evitar modificar una lista mientras se itera sobre ella
# Mal:
# for elemento in lista:
#     if condicion(elemento):
#         lista.remove(elemento)  # ¡Puede causar comportamientos inesperados!

# Mejor:
# lista = [elemento for elemento in lista if not condicion(elemento)]

# 3. Usar copy() cuando se necesite una copia independiente

# 4. Considerar tuplas para datos inmutables o namedtuple para datos estructurados

# 5. Para operaciones frecuentes de búsqueda, considerar usar un conjunto (set) o diccionario

# 6. Usar métodos incorporados (sort, reverse, etc.) en lugar de implementaciones manuales