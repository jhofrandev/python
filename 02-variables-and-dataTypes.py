################################################################################## Que es una variable?
################################################################################

# Una variable es un nombre que referencia a un valor almacenado en la memoria. En Python, las variables no requieren declaración expliícita de tipo: el tipo se infiere del valor asignado.
nombre = 'Juan' # Variable de tipo str (cadena)
edad = 30        # Variable de tipo int (entero)
pi = 3.1416      # Variable de tipo float (flotante)
es_mayor = True  # Variable de tipo bool (booleano)

# Tipado Dinámico
# Python permite cambiar el tipo de una variable durante la ejecución.
x = 10      # x es un entero
x = 'Hola'  # ahora x es una cadena


################################################################################
## Convenciones de Nomenclatura
################################################################################
x = 20
y = 'Jhon'
print(type(x)) #int
print(type(y)) #str


################################################################################
## Convenciones de Nomenclatura
################################################################################

# Snake case: Usa guiones bajos para separar palabras en nombres de variables.
nombre_completo = "Juan Pérez"

# Constantes: Por convención, una MAYUSCULAS.
PI = 3.1416
GRAVEDAD = 9.8

# Variables privadas: Comienza con guión bajo.
_contador_interno = 0

# Variables "dunder": Doble guión bajo al inicio y final (para métodos especiales).
__nombre__ = "Variable especial"


################################################################################
## Reglas para nombrar variables
################################################################################

# 1. Caracteres permitidos: Letras (a-z, A-Z), números (0-9) y guiones bajos (_).
# 2. No puede empezar con número: 2variables ✖️, variable2 ✔️
# 3. Sensible a mayúsculas y minúsculas: edad != Edad != EDAD
# 4. No usar palabras reservadas: class, if, for, etc.
# 5. Convenciones:
#    - Ysa snake_case para nombres compuestos: mi_variable
#    - Para constantes, usa MAYÚSCULAS: PI = 3.1416


################################################################################
## Tipos de datos Fundamentales
################################################################################

## Inmutables:
# int: Números enteros (1, 100, -10)
# float: Números decimales (3.14, -0.001)
# str: Cadenas de texto ('Hola', 'Python')
# bool: Va,ores booleanos (True, False)
# tupla: Colecciones ordenadas inmutables((1, 2, 3))

## MUtables:
# list: Colecciones ordenadas mutables ([1, 2, 3])
# dict: Diccionarios (pares clave-valor) ({'nombre': 'Juan'})
# set: Conjuntos de elementos únicos ({1, 2, 3})

################################################################################
## Asignación Múltiple
################################################################################

# Python permite asignar valores a múltiples variables en una sola línea:
x, y, z = 1, 2, 3

# También puedes intercambiar valores fácilmente:
a, b, = 10, 20
a, b = b, a

################################################################################
## Ámbito de Variables (Scope)
################################################################################

## Variables Locales
# Definidad dentro de una función, solo accesibles dentro de ella:
def mi_funcion():
  x = 10    # Variable local
  print(x)

## Variables Globales
# Definidas fuera de  cualquier función, accesibles en todo el módulo:
y = 20

def otra_funcion():
  print(y) # Accede a la variable global
  # Para modificarla dentro de la función:
  global y
  y = 30

## Variable No locales
# Para acceder a variables de un ámbito externo (pero no global):
def funcion_externa():
  z = 10
  def funcion_interna():
    nonlocal z
    z = 20
  funcion_interna()
  print(z)  # Imprime 20


################################################################################
## Buenas Prácticas
################################################################################

# Nombres descriptivos: Usa nombres que expliquen el propósito de la variable
a = 3600 # mal
segundos_por_hora = 3600 # bien

# Evita variables globales: Limita su uso para reducir efectos secundarios

#Consistencia: Mentén un estilo coherente en todo tu código

# Evita nombres reservador: No uses palabras claves de Python como nombre de variables

# Inicializa tus variables: Asigna un valor inicial antes de usarlas

# Usa type hints (anotaciones de tipo) para mejorar la leginilidad y facilitar el mantenimiento:
nombre: str = 'Juan'
edad: int = 30


################################################################################
## Referencias y Objetos
################################################################################

# En Python, las variables son referencias a onjetos en memoria. Esto es importante para entender el comportamiento de asignación:
lista1 = [1, 2, 3]
lista2 = lista1 # lista2 referencia al mismo objeto que lista1
lista2.append(4)
print(lista1)  # Muestra [1, 2, 3, 4]

# Para crear una copia independiente:
lista2 = lista1.copy()  # o list(lista1) o lista1[:]


################################################################################
## Garbage Collection
################################################################################

# Python maneja automáticamente la memoria. Cuando una variable ya no tiene referencias, el recolector de basura libera la memoria:
x = 10
x = 'hola' # El valor 10 queda sin referencia y puede ser liberado


################################################################################
## Variables Especiales
################################################################################

# _: En el intérprete interactivo, almacena el último resultado evaluado.a
# __name__: Contiene el nombre del módulo actual

# add this