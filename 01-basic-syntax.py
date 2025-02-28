# 1. Identación y bloques de código
## Python utiliza espacios o tabulaciones para definir bloques (como funcionesm buncles o condiciones)
## Error común: No mantener la identación consistente (generalmente 4 espacios por nivel)
## Ejemplo:
if 5 > 2:
  print("5 es mayor que 2")


# 2. Variables y Tipos de Datos
## Variables: No se declaran con un tipo especidico, Python es de tipo dinámico.
nombre = "Ana" # String (str)
edad = 25 # Entero (int)
altura = 1.75 # Flotante (float)
es_estudiante = True # Booleano (bool)
## Tipos básicos:
### int, float, str, bool, None
### Colecciones: list, tuple, dict, set
## Mutabilidad:
### Inmutables: int, str, tuble, bool
### Mutables: list, dict, set


# 3. Operadores
## Aritméticos: +, -, *. /. // (división entera), % (módulo), ** (potencia)
## Comparación: ==, !=, <, >, <=, >=
## Lógicos: and, or, not
## Identidad: is, is not (comprueban si dos variables son el mismo objeto)
## Pertenencia: in, not in (para verificar elementos en colecciones)

# 4. Estuturas de Control
## Condicionales: if, elif, else
if edad >= 18:
  print("Mayor de edad")
elif edad > 12:
  print("Adolescente")
else:
  print("Niño")
## Bucles:
### for: Itera sobre secuencias (listas, strings, rangos, etc.)
for i in range(5):
  print(i)
### while: Ejecuta mientras una condición sea cerdadera.
contador = 0
while contador < 3:
  print(contador)
  contador += 1

# 5. Funciones
## Se definen con def, parámetros entre paréntesis y return para devolver valores.
def suma(a, b):
  return a + b
## Parámetros opcionales
def saludar(nombre, mensaje="hola"):
  print(f"{mensaje}, {nombre}")
## Lambda: Funciones anónimas.
multiplicar = lambda x, y: x * y

# 6. Menejo de Errores
## Usa try-except para capturar excepciones:
try:
  resultado = 10 / 0
except ZeroDivisionError:
  print("No puedes dividir por cero")

# 7. Estruturas de Datos
## Listas: Mutables, se definen con []
numeros = [1, 2, 3]
numeros.append(4)
## Tuplas: Inmutables, se definen con ()
coordenadas = (4, 5)
## Diccionarios: Pares clave-valor, se definen con {}
persona = {"nombre": "Ana", "edad": 25}
## Sets: Colecciones no ordenadas y sin duplicados.
conjunto = {1, 2, 3}

# 8. Módulos y Paquetes
## Importar módulos:
import math
print(math.sqrt(16)) # 4.0
## Paquetes: Directorios con archivos __init__.py

# 9. Clases y POO
## Definición de clases:
class Perro:
  def __init__(self, nombre):
    self.nombre = nombre

    def ladrar(self):
      print("¡Guau!")
## Herencia:
class PerroLabrador(Perro):
  def __init__(self, nombre, color):
    super().__init__(nombre)
    self.color = color

# Convenciones y Buenas Prácticas
## PEP 8: Guía de estilo oficial (ej. 4 espacios para identación, nombre de variables en snake_case)
## Docstrings: Comentarios para documentar funciones y clases.
def suma(a, b):
  """"Devuelve la suma de a y b."""
  return a + b