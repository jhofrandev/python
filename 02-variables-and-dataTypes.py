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