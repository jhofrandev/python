"""
  Los conjuntos (sets) en Python son colecciones no ordenadas de elementos únicos.
  Son útiles para eliminar duplicados, realizar operaciones matemáticas de conjuntos
  como uniones, intersecciones y diferencias, y para verificar pertenencia de manera eficiente.
"""

################################################################################
## Creación de conjuntos
################################################################################

# Conjunto vacío
conjunto_vacio = set()  # No se puede usar {} porque crearía un diccionario vacío

# Conjunto con elementos
numeros = {1, 2, 3, 4, 5}
frutas = {"manzana", "banana", "naranja"}

# Los conjuntos eliminan automáticamente los duplicados
numeros_con_duplicados = {1, 2, 2, 3, 3, 3, 4, 5, 5}
print(numeros_con_duplicados)  # {1, 2, 3, 4, 5}

# Crear conjunto a partir de otros iterables
conjunto_desde_lista = set([1, 2, 2, 3, 4])
conjunto_desde_string = set("Mississippi")  # {'M', 'i', 'p', 's'}
conjunto_desde_tupla = set((1, 2, 2, 3, 3, 3))

# Comprensión de conjuntos
cuadrados = {x**2 for x in range(10) if x % 2 == 0}
print(cuadrados)  # {0, 4, 16, 36, 64}

################################################################################
## Características de los conjuntos
################################################################################

# 1. No ordenados: los elementos no tienen un orden específico
print({3, 1, 2})  # El orden de impresión puede variar

# 2. Elementos únicos: no puede haber duplicados
print({1, 1, 1})  # {1}

# 3. Inmutables: los elementos deben ser inmutables (números, strings, tuplas)
# conjunto_invalido = {[1, 2], 3}  # TypeError: unhashable type: 'list'
conjunto_valido = {(1, 2), 3, "hola"}  # Tuplas (inmutables) sí son válidas

# 4. Mutabilidad del conjunto: aunque los elementos deben ser inmutables,
#    el conjunto en sí es mutable (se puede modificar)

################################################################################
## Operaciones básicas
################################################################################

frutas = {"manzana", "banana", "naranja", "uva"}

# Añadir un elemento
frutas.add("pera")
print(frutas)

# Añadir múltiples elementos
frutas.update(["sandía", "melón"])
print(frutas)

# También se puede usar update con cualquier iterable
frutas.update(("fresa", "cereza"))
print(frutas)

# Eliminar un elemento (genera error si no existe)
frutas.remove("banana")
print(frutas)

# Eliminar un elemento (no genera error si no existe)
frutas.discard("plátano")  # No existe, pero no genera error
print(frutas)

# Eliminar y devolver un elemento arbitrario
elemento = frutas.pop()
print(f"Elemento eliminado: {elemento}")
print(frutas)

# Vaciar el conjunto
frutas.clear()
print(frutas)  # set()

################################################################################
## Operaciones matemáticas de conjuntos
################################################################################

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Unión: elementos que están en A o en B (o en ambos)
union1 = A | B
union2 = A.union(B)
print(f"Unión: {union1}")  # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersección: elementos que están tanto en A como en B
interseccion1 = A & B
interseccion2 = A.intersection(B)
print(f"Intersección: {interseccion1}")  # {4, 5}

# Diferencia: elementos que están en A pero no en B
diferencia1 = A - B
diferencia2 = A.difference(B)
print(f"Diferencia A - B: {diferencia1}")  # {1, 2, 3}

# Diferencia simétrica: elementos que están en A o en B, pero no en ambos
dif_simetrica1 = A ^ B
dif_simetrica2 = A.symmetric_difference(B)
print(f"Diferencia simétrica: {dif_simetrica1}")  # {1, 2, 3, 6, 7, 8}

################################################################################
## Operaciones de conjuntos in-place (modifican el conjunto original)
################################################################################

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Unión in-place
A_copia = A.copy()
A_copia |= B  # Equivalente a A_copia.update(B)
print(f"A después de unión in-place: {A_copia}")

# Intersección in-place
A_copia = A.copy()
A_copia &= B  # Equivalente a A_copia.intersection_update(B)
print(f"A después de intersección in-place: {A_copia}")

# Diferencia in-place
A_copia = A.copy()
A_copia -= B  # Equivalente a A_copia.difference_update(B)
print(f"A después de diferencia in-place: {A_copia}")

# Diferencia simétrica in-place
A_copia = A.copy()
A_copia ^= B  # Equivalente a A_copia.symmetric_difference_update(B)
print(f"A después de diferencia simétrica in-place: {A_copia}")

################################################################################
## Relaciones entre conjuntos
################################################################################

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {6, 7, 8}

# Verificar si un conjunto es subconjunto de otro
print(f"¿A es subconjunto de B? {A.issubset(B)}")  # True
print(f"¿A <= B? {A <= B}")  # True (operador de subconjunto)

# Verificar si un conjunto es superconjunto de otro
print(f"¿B es superconjunto de A? {B.issuperset(A)}")  # True
print(f"¿B >= A? {B >= A}")  # True (operador de superconjunto)

# Verificar si dos conjuntos son disjuntos (no tienen elementos en común)
print(f"¿A y C son disjuntos? {A.isdisjoint(C)}")  # True
print(f"¿A y B son disjuntos? {A.isdisjoint(B)}")  # False

################################################################################
## Verificación de pertenencia
################################################################################

frutas = {"manzana", "banana", "naranja", "uva"}

# Verificar si un elemento está en el conjunto
print("banana" in frutas)  # True
print("kiwi" in frutas)    # False

# Verificar si un elemento no está en el conjunto
print("kiwi" not in frutas)  # True

################################################################################
## Iteración sobre conjuntos
################################################################################

# Recorrer elementos
for fruta in frutas:
    print(fruta)  # El orden no está garantizado

# Uso con enumerate (aunque el orden no está garantizado)
for i, fruta in enumerate(frutas):
    print(f"Elemento {i}: {fruta}")

################################################################################
## Conjuntos inmutables (frozenset)
################################################################################

# Los frozenset son conjuntos inmutables
fs = frozenset([1, 2, 3, 4])
print(fs)  # frozenset({1, 2, 3, 4})

# No se pueden modificar
try:
    fs.add(5)  # AttributeError: 'frozenset' object has no attribute 'add'
except AttributeError as e:
    print(f"Error: {e}")

# Pueden usarse como elementos de otros conjuntos o como claves de diccionarios
conjunto_de_frozensets = {frozenset([1, 2]), frozenset([3, 4])}
print(conjunto_de_frozensets)

diccionario = {frozenset([1, 2]): "conjunto 1-2", frozenset([3, 4]): "conjunto 3-4"}
print(diccionario[frozenset([1, 2])])  # "conjunto 1-2"

################################################################################
## Casos de uso comunes
################################################################################

# 1. Eliminar duplicados de una lista
lista_con_duplicados = [1, 2, 2, 3, 3, 3, 4, 5, 5]
lista_sin_duplicados = list(set(lista_con_duplicados))
print(f"Lista sin duplicados: {lista_sin_duplicados}")

# 2. Encontrar elementos únicos entre múltiples colecciones
lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
elementos_unicos = set(lista1) ^ set(lista2)  # Diferencia simétrica
print(f"Elementos únicos: {elementos_unicos}")  # {1, 2, 5, 6}

# 3. Verificar si dos listas tienen elementos en común
tienen_comun = not set(lista1).isdisjoint(set(lista2))
print(f"¿Tienen elementos en común? {tienen_comun}")  # True

# 4. Encontrar elementos comunes entre múltiples listas
lista3 = [4, 5, 6, 7]
comunes = set(lista1) & set(lista2) & set(lista3)
print(f"Elementos comunes: {comunes}")  # {4}

# 5. Implementar un filtro de elementos únicos en tiempo real
def procesar_elemento(elemento, elementos_vistos):
    if elemento in elementos_vistos:
        print(f"Elemento duplicado: {elemento}")
        return False
    elementos_vistos.add(elemento)
    return True

elementos_vistos = set()
datos = [1, 2, 3, 2, 4, 1, 5]
elementos_unicos = [elem for elem in datos if procesar_elemento(elem, elementos_vistos)]
print(f"Elementos procesados: {elementos_unicos}")  # [1, 2, 3, 4, 5]

################################################################################
## Rendimiento y consideraciones
################################################################################

# Los conjuntos son muy eficientes para:
# - Verificar pertenencia (in): O(1) en promedio
# - Añadir elementos (add): O(1) en promedio
# - Eliminar elementos (remove, discard): O(1) en promedio
# - Operaciones de conjuntos (union, intersection): O(len(s) + len(t))

# Comparación de rendimiento para verificar pertenencia
import timeit
import random

# Generar datos de prueba
tamaño = 10000
datos = list(range(tamaño))
random.shuffle(datos)
buscar = datos[tamaño // 2]

# Tiempo para verificar pertenencia en una lista
tiempo_lista = timeit.timeit(
    stmt=f"{buscar} in datos",
    globals={"buscar": buscar, "datos": datos},
    number=1000
)

# Tiempo para verificar pertenencia en un conjunto
conjunto_datos = set(datos)
tiempo_conjunto = timeit.timeit(
    stmt=f"{buscar} in conjunto_datos",
    globals={"buscar": buscar, "conjunto_datos": conjunto_datos},
    number=1000
)

print(f"Tiempo para verificar pertenencia en lista: {tiempo_lista:.6f} segundos")
print(f"Tiempo para verificar pertenencia en conjunto: {tiempo_conjunto:.6f} segundos")
print(f"El conjunto es aproximadamente {tiempo_lista/tiempo_conjunto:.1f} veces más rápido")

################################################################################
## Buenas prácticas
################################################################################

# 1. Usar conjuntos para eliminar duplicados
# En lugar de:
def elementos_unicos_manual(lista):
    resultado = []
    for item in lista:
        if item not in resultado:
            resultado.append(item)
    return resultado

# Mejor usar:
def elementos_unicos_set(lista):
    return list(set(lista))

# 2. Usar conjuntos para verificaciones de pertenencia en colecciones grandes
# En lugar de:
def contiene_algun_elemento(lista, elementos):
    for elemento in elementos:
        if elemento in lista:  # Operación O(n) para listas
            return True
    return False

# Mejor usar:
def contiene_algun_elemento_set(lista, elementos):
    conjunto = set(lista)
    for elemento in elementos:
        if elemento in conjunto:  # Operación O(1) para conjuntos
            return True
    return False

# 3. Preferir operadores de conjunto sobre métodos cuando sea posible por legibilidad
# A | B es más legible que A.union(B)

# 4. Usar frozenset para conjuntos que no deben cambiar o que necesitan ser usados como claves

# 5. Recordar que los conjuntos no mantienen el orden, usar listas si el orden es importante

# 6. Para conjuntos muy grandes, considerar el uso de operaciones in-place para ahorrar memoria