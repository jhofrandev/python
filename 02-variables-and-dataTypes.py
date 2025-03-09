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

