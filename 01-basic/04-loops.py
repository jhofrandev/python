"""
  Los bucles (loops) en Python permiten ejecutar un bloque de código múltiples veces.
  Son fundamentales para automatizar tareas repetitivas y procesar colecciones de datos.
"""

################################################################################
## Bucle for
################################################################################

# El bucle for en Python itera sobre elementos de cualquier secuencia (lista, tupla, cadena, etc.)
# o cualquier objeto iterable.

# Iterando sobre una lista
print("Iterando sobre una lista:")
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(fruta)

# Iterando sobre una cadena
print("\nIterando sobre una cadena:")
for letra in "Python":
    print(letra)

# Iterando sobre un rango de números
print("\nIterando sobre un rango:")
for numero in range(5):  # 0, 1, 2, 3, 4
    print(numero)

# La función range() puede tomar hasta tres argumentos:
# range(inicio, fin, paso)
print("\nRange con inicio y fin:")
for i in range(2, 6):  # 2, 3, 4, 5
    print(i)

print("\nRange con inicio, fin y paso:")
for i in range(1, 10, 2):  # 1, 3, 5, 7, 9
    print(i)

################################################################################
## Bucle while
################################################################################

# El bucle while ejecuta un bloque de código mientras una condición sea verdadera

print("\nBucle while básico:")
contador = 0
while contador < 5:
    print(contador)
    contador += 1  # Es importante actualizar la condición para evitar bucles infinitos

# Bucle while con break
print("\nBucle while con break:")
contador = 0
while True:  # Bucle infinito
    print(contador)
    contador += 1
    if contador >= 5:
        break  # Sale del bucle

################################################################################
## Instrucciones de control de bucles
################################################################################

# break: Sale completamente del bucle
print("\nUsando break en un bucle for:")
for i in range(10):
    if i == 5:
        break
    print(i)  # Imprime 0, 1, 2, 3, 4

# continue: Salta a la siguiente iteración
print("\nUsando continue en un bucle for:")
for i in range(10):
    if i % 2 == 0:  # Si i es par
        continue
    print(i)  # Imprime solo números impares: 1, 3, 5, 7, 9

# else en bucles: Se ejecuta cuando el bucle termina normalmente (sin break)
print("\nUsando else en un bucle for:")
for i in range(5):
    print(i)
else:
    print("Bucle completado sin interrupciones")

print("\nUsando else con break:")
for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("Este mensaje no se imprimirá porque el bucle se interrumpió")

################################################################################
## Técnicas avanzadas con bucles
################################################################################

# Enumerate: Obtiene índice y valor en cada iteración
print("\nUsando enumerate:")
frutas = ["manzana", "banana", "naranja"]
for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")

# Zip: Itera sobre múltiples secuencias en paralelo
print("\nUsando zip:")
nombres = ["Ana", "Juan", "María"]
edades = [25, 30, 22]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

# Comprensión de listas: Forma concisa de crear listas
print("\nComprensión de listas:")
cuadrados = [x**2 for x in range(1, 6)]
print(cuadrados)  # [1, 4, 9, 16, 25]

# Comprensión de listas con condición
print("\nComprensión de listas con condición:")
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]

################################################################################
## Bucles anidados
################################################################################

print("\nBucles anidados:")
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# Ejemplo práctico: Imprimir una matriz
print("\nImprimiendo una matriz:")
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()  # Nueva línea después de cada fila

################################################################################
## Buenas prácticas
################################################################################

# 1. Evita bucles anidados profundos (más de 2-3 niveles) por legibilidad y rendimiento

# 2. Usa nombres descriptivos para las variables de iteración
for estudiante in estudiantes:
    # Mejor que: for e in estudiantes:
    pass

# 3. Considera usar funciones como any() o all() en lugar de bucles para verificaciones simples
numeros = [1, 2, 3, 4, 5]
todos_positivos = all(n > 0 for n in numeros)
alguno_par = any(n % 2 == 0 for n in numeros)

# 4. Para iteraciones complejas, considera usar itertools
import itertools

# Ejemplo: Combinaciones
for combo in itertools.combinations([1, 2, 3, 4], 2):
    print(combo)

# 5. Usa enumerate() cuando necesites tanto el índice como el valor

# 6. Prefiere comprensiones de listas sobre bucles for cuando sea apropiado