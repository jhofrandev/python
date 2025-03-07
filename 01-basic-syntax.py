"""
La sintaxis es la parte de la gramática que estudia cómo se combina y ordena las palabra, osea que vela por las reglas y la estrutura correcta que deberia de tener una oración.

La sintaxis de Python es un conjunto de reglas que se utilizan para crear un programa Python.
"""


################################################################################
## Identación y bloques de código
################################################################################

# Python utiliza espacios o tabulaciones para definir bloques (como funciones bucles o condiciones)
# Error común: No mantener la identación consistente (generalmente 4 espacios por nivel)
# Ejemplo:
if 5 > 2:
  print("5 es mayor que 2")


################################################################################
## Identificadores de Python
################################################################################

# Un identificador de Python es un nombre que se utiliza para identificar una variable, función, clase, módulo u otro objeto. Un identificador comienza con una letra de la A a la Z o de la a a la z o un guión bajo (_) seguido de cero o más letras, guiones bajos y dígitos (0 a 9).

# Python no permite caracteres de puntuación como @, $ y % dentro de los identificadores.

# Python es sensible a mayúsculas y minúsculas. Esto significa que "Nombre" y "nombre" son dos identificadores diferentes en Python.

# Los nombres de clase de Python comienza con una mayúscula, Todos los demás identificadores comienzan con una letra minúscula.
# Comenzar un identificador con un guión bajo inicial indica qie el identificador es privado.
# Comenzar un identificador con dos guiones bajo iniciales indica un identificador fuertemente privado.
# Si el identificador tambien termina con dos guiones bajos finales, el identificador es in nombre especial definifo por el lenguaje.

################################################################################
## Palabras reservadas de Python.
################################################################################


################################################################################
## Sentencias multilineales en Python
################################################################################

# Las sentencias en Python suelen terminar con una nueva línea. Sin embargom Python permite el uso del carácter de continuación de línea (\) para indicar que la línea debe continuar.
total = 1 + \
        2 + \
        3

# Las declaraciones cotenidas entre corchetes []. {} o () no necesitan utilizar el carácter de continuación de línea.
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']


################################################################################
## Variables y Tipos de Datos
################################################################################


# Variables: No se declaran con un tipo especidico, Python es de tipo dinámico.
nombre = "Ana" # String (str)
edad = 25 # Entero (int)
altura = 1.75 # Flotante (float)
es_estudiante = True # Booleano (bool)

# Tipos básicos:
# int, float, str, bool, None
# Colecciones: list, tuple, dict, set
# Mutabilidad:
# Inmutables: int, str, tuble, bool
# Mutables: list, dict, set

################################################################################
## Citas en Python
################################################################################

# Python acepta comillas simples ('), dobles (") y triples (''' o """) para indicar literales de cadena, siempre que el mismo tipo de comillas comience y finalice la cadena.

# Las comillas triples se utilizan para extender la cadena a lo largo de varias líneas.
word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is made up of multiple lines and sentences."""

################################################################################
## Varias declaraciones en una línea
################################################################################
import sys; x = 'foo'; sys.stdout.write(x + '\n')

################################################################################
## Operadores
################################################################################

# Aritméticos: +, -, *. /. // (división entera), % (módulo), ** (potencia)
# Comparación: ==, !=, <, >, <=, >=
# Lógicos: and, or, not
# Identidad: is, is not (comprueban si dos variables son el mismo objeto)
# Pertenencia: in, not in (para verificar elementos en colecciones)

################################################################################
## Estuturas de Control
################################################################################

# Condicionales: if, elif, else
if edad >= 18:
  print("Mayor de edad")
elif edad > 12:
  print("Adolescente")
else:
  print("Niño")

# Bucles:
# for: Itera sobre secuencias (listas, strings, rangos, etc.)
for i in range(5):
  print(i)

# while: Ejecuta mientras una condición sea cerdadera.
contador = 0
while contador < 3:
  print(contador)
  contador += 1

################################################################################
## Funciones
################################################################################

# Se definen con def, parámetros entre paréntesis y return para devolver valores.
def suma(a, b):
  return a + b

# Parámetros opcionales
def saludar(nombre, mensaje="hola"):
  print(f"{mensaje}, {nombre}")

# Lambda: Funciones anónimas.
multiplicar = lambda x, y: x * y

################################################################################
## Menejo de Errores
################################################################################

# Usa try-except para capturar excepciones:
try:
  resultado = 10 / 0
except ZeroDivisionError:
  print("No puedes dividir por cero")

################################################################################
## Estruturas de Datos
################################################################################

# Listas: Mutables, se definen con []
numeros = [1, 2, 3]
numeros.append(4)

# Tuplas: Inmutables, se definen con ()
coordenadas = (4, 5)

# Diccionarios: Pares clave-valor, se definen con {}
persona = {"nombre": "Ana", "edad": 25}

# Sets: Colecciones no ordenadas y sin duplicados.
conjunto = {1, 2, 3}

################################################################################
# Módulos y Paquetes
################################################################################

# Importar módulos:
import math
print(math.sqrt(16)) # 4.0

# Paquetes: Directorios con archivos __init__.py


################################################################################
# Clases y POO
################################################################################

# Definición de clases:
class Perro:
  def __init__(self, nombre):
    self.nombre = nombre

    def ladrar(self):
      print("¡Guau!")

# Herencia:
class PerroLabrador(Perro):
  def __init__(self, nombre, color):
    super().__init__(nombre)
    self.color = color

################################################################################
## Convenciones y Buenas Prácticas
################################################################################

# PEP 8: Guía de estilo oficial (ej. 4 espacios para identación, nombre de variables en snake_case)

# Docstrings: Comentarios para documentar funciones y clases.
def suma(a, b):
  """"Devuelve la suma de a y b."""
  return a + b

################################################################################
# Ejecutar sintaxis de Python
################################################################################

# Escribiendo directamente en la línea de comandos:
# >>> print("Hola")
# Hola

# Ejecutando un script:
# python script.py

################################################################################
# Comentarios
################################################################################
# this is a comment
"""
this is a multi-line comment
"""

# https://learnxinyminutes.com/python/