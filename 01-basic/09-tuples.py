"""
  Las tuplas en Python son colecciones ordenadas e inmutables de elementos.
  A diferencia de las listas, una vez creadas, no se pueden modificar (añadir, eliminar o cambiar elementos).
  Esta inmutabilidad las hace útiles para datos que no deben cambiar.
"""

################################################################################
## Creación de tuplas
################################################################################

# Tupla vacía
tupla_vacia = ()
tupla_vacia_alternativa = tuple()

# Tupla con elementos
numeros = (1, 2, 3, 4, 5)
frutas = ("manzana", "banana", "naranja")
mixta = (1, "hola", 3.14, True, (1, 2))  # Las tuplas pueden contener diferentes tipos de datos

# Tupla con un solo elemento (requiere una coma)
singleton = (42,)  # Sin la coma sería un entero: (42) == 42
print(type((42,)))  # <class 'tuple'>
print(type((42)))   # <class 'int'>

# Crear tupla a partir de otros iterables
tupla_desde_lista = tuple([1, 2, 3])
tupla_desde_string = tuple("Python")  # ('P', 'y', 't', 'h', 'o', 'n')
tupla_desde_rango = tuple(range(5))   # (0, 1, 2, 3, 4)

# Tupla por empaquetado (sin paréntesis)
tupla_empaquetada = 1, 2, 3, 4, 5
print(tupla_empaquetada)  # (1, 2, 3, 4, 5)
print(type(tupla_empaquetada))  # <class 'tuple'>

################################################################################
## Acceso a elementos
################################################################################

# Acceso por índice (los índices comienzan en 0)
frutas = ("manzana", "banana", "naranja", "uva", "pera")
print(frutas[0])  # manzana
print(frutas[2])  # naranja

# Índices negativos (cuentan desde el final)
print(frutas[-1])  # pera (último elemento)
print(frutas[-2])  # uva (penúltimo elemento)

# Slicing (rebanado): obtener subtuplas
print(frutas[1:3])    # ('banana', 'naranja') (desde índice 1 hasta 3-1)
print(frutas[:3])     # ('manzana', 'banana', 'naranja') (desde el inicio hasta 3-1)
print(frutas[2:])     # ('naranja', 'uva', 'pera') (desde índice 2 hasta el final)
print(frutas[-3:])    # ('naranja', 'uva', 'pera') (últimos 3 elementos)
print(frutas[::2])    # ('manzana', 'naranja', 'pera') (cada 2 elementos)
print(frutas[::-1])   # ('pera', 'uva', 'naranja', 'banana', 'manzana') (invertir tupla)

################################################################################
## Inmutabilidad de las tuplas
################################################################################

# Las tuplas no pueden ser modificadas después de su creación
frutas = ("manzana", "banana", "naranja")

# Intentar modificar una tupla genera un error
try:
    frutas[1] = "kiwi"  # TypeError: 'tuple' object does not support item assignment
except TypeError as e:
    print(f"Error: {e}")

# Sin embargo, si una tupla contiene objetos mutables (como listas), estos sí pueden modificarse
tupla_con_lista = (1, 2, [3, 4])
tupla_con_lista[2].append(5)  # Esto es válido
print(tupla_con_lista)  # (1, 2, [3, 4, 5])

################################################################################
## Operaciones comunes
################################################################################

numeros = (3, 1, 4, 1, 5, 9, 2, 6, 5)

# Longitud de la tupla
print(len(numeros))  # 9

# Contar ocurrencias de un elemento
print(numeros.count(5))  # 2 (el número 5 aparece dos veces)

# Encontrar el índice de un elemento (primera ocurrencia)
print(numeros.index(4))  # 2 (el número 4 está en el índice 2)
# print(numeros.index(7))  # ValueError: 7 is not in tuple

# Concatenación de tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)  # (1, 2, 3, 4, 5, 6)

# Repetición de tuplas
tupla_repetida = tupla1 * 3
print(tupla_repetida)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Ordenar una tupla (creando una nueva)
numeros_ordenados = tuple(sorted(numeros))
print(numeros_ordenados)  # (1, 1, 2, 3, 4, 5, 5, 6, 9)

# Máximo y mínimo
print(max(numeros))  # 9
print(min(numeros))  # 1

################################################################################
## Verificaciones y pertenencia
################################################################################

frutas = ("manzana", "banana", "naranja", "uva")

# Verificar si un elemento está en la tupla
print("banana" in frutas)  # True
print("kiwi" in frutas)    # False

# Verificar si un elemento no está en la tupla
print("kiwi" not in frutas)  # True

################################################################################
## Iteración sobre tuplas
################################################################################

# Recorrer elementos
for fruta in frutas:
    print(fruta)

# Recorrer con índice usando enumerate
for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")

# Recorrer múltiples tuplas en paralelo con zip
precios = (1.2, 0.8, 1.5, 2.0)
for fruta, precio in zip(frutas, precios):
    print(f"{fruta}: ${precio}")

################################################################################
## Desempaquetado de tuplas
################################################################################

# Desempaquetado básico
coordenadas = (10, 20, 30)
x, y, z = coordenadas  # Desempaquetado
print(f"x={x}, y={y}, z={z}")  # x=10, y=20, z=30

# Desempaquetado con * (resto)
primero, *resto, ultimo = (1, 2, 3, 4, 5)
print(primero)  # 1
print(resto)    # [2, 3, 4]
print(ultimo)   # 5

# Intercambio de variables con tuplas
a, b = 5, 10
a, b = b, a  # Intercambio de valores
print(f"a={a}, b={b}")  # a=10, b=5

# Retorno múltiple en funciones
def obtener_dimensiones():
    return (1920, 1080)  # Retorna una tupla

ancho, alto = obtener_dimensiones()  # Desempaqueta la tupla retornada
print(f"Ancho: {ancho}, Alto: {alto}")  # Ancho: 1920, Alto: 1080

################################################################################
## Tuplas con nombre (namedtuple)
################################################################################

from collections import namedtuple

# Definir un tipo de tupla con nombre
Persona = namedtuple('Persona', ['nombre', 'edad', 'ciudad'])

# Crear instancias
persona1 = Persona('Ana', 30, 'Madrid')
persona2 = Persona(nombre='Juan', edad=25, ciudad='Barcelona')

# Acceso por índice (como tupla normal)
print(persona1[0])  # Ana

# Acceso por nombre (como objeto)
print(persona1.nombre)  # Ana
print(persona2.ciudad)  # Barcelona

# Convertir a diccionario
print(persona1._asdict())  # {'nombre': 'Ana', 'edad': 30, 'ciudad': 'Madrid'}

# Crear una nueva instancia basada en otra (inmutabilidad)
persona3 = persona1._replace(edad=31)
print(persona3)  # Persona(nombre='Ana', edad=31, ciudad='Madrid')

################################################################################
## Ventajas de las tuplas sobre las listas
################################################################################

# 1. Inmutabilidad: garantiza que los datos no cambiarán
# 2. Rendimiento: las tuplas son ligeramente más rápidas que las listas
# 3. Pueden usarse como claves en diccionarios (las listas no)
# 4. Indican claramente la intención de que los datos no deben cambiar

# Ejemplo: tupla como clave de diccionario
coordenadas_valores = {
    (0, 0): "Origen",
    (1, 0): "Este",
    (0, 1): "Norte"
}
print(coordenadas_valores[(0, 0)])  # Origen

# Esto no funcionaría con listas:
# diccionario_error = {[0, 0]: "Origen"}  # TypeError: unhashable type: 'list'

################################################################################
## Casos de uso comunes
################################################################################

# 1. Retorno múltiple de funciones
def estadisticas(numeros):
    return min(numeros), max(numeros), sum(numeros) / len(numeros)

minimo, maximo, promedio = estadisticas([1, 2, 3, 4, 5])
print(f"Mín: {minimo}, Máx: {maximo}, Promedio: {promedio}")

# 2. Datos inmutables (constantes)
DIAS_SEMANA = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")

# 3. Estructura de datos heterogénea con posiciones fijas
registro = ("Juan", "Pérez", 30, "Ingeniero")
nombre, apellido, edad, profesion = registro

# 4. Diccionarios con claves compuestas
mapa_calor = {
    (x, y): temperatura
    for x in range(3)
    for y in range(3)
    for temperatura in [x + y * 10]
}
print(mapa_calor)

################################################################################
## Rendimiento y consideraciones
################################################################################

# Las tuplas son eficientes para:
# - Acceso por índice: O(1)
# - Iterar sobre todos los elementos: O(n)
# - Uso como claves en diccionarios (hashable)

# Comparación de rendimiento (ejemplo ilustrativo)
import timeit

# Crear una lista vs tupla (la tupla es ligeramente más rápida)
tiempo_lista = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000)
tiempo_tupla = timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000)
print(f"Tiempo para crear lista: {tiempo_lista}")
print(f"Tiempo para crear tupla: {tiempo_tupla}")

################################################################################
## Buenas prácticas
################################################################################

# 1. Usar tuplas para datos que no deben cambiar
CONFIGURACION = (1920, 1080, 60)  # resolución y fps

# 2. Preferir namedtuple para tuplas con muchos elementos para mejorar legibilidad
Configuracion = namedtuple('Configuracion', ['ancho', 'alto', 'fps'])
config = Configuracion(1920, 1080, 60)
print(config.ancho)  # Más legible que config[0]

# 3. Aprovechar el desempaquetado para código más limpio
for i, (clave, valor) in enumerate(coordenadas_valores.items()):
    print(f"Item {i}: {clave} -> {valor}")

# 4. Usar tuplas para retornos múltiples de funciones
# 5. Considerar listas para colecciones que necesitan ser modificadas
# 6. Recordar que la inmutabilidad es a nivel de la tupla, no de sus elementos