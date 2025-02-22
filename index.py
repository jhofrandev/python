# 1. Variables y tipos de datos
## No se declaran tipos, Pytho los infiere:
nombre = "Ana" # String (texto)
edad = 25 # Int (enteros)
altura = 1.75 # Float (decimales)
es_programador = True # Bool (booleanos)

# 2. Estruturas de Datos Básicas
## Listas: Colecciones ordenadas y modificables.
frutas = ["manzana", "naranja", "banana"]
print(frutas[0]) # Output: "manzana"

## Tuplas: Colecciones ordenadas inmutables.
coordenadas = (10, 20)

## Diccionarios: Colecciones clave-valor.
usuario = {
  "nombre": "Carlos",
  "edad": 30,
  "ciudad": "Madrid"
}
print(usuario["nombre"]) # Output: "Carlos"

# 3. Estructuras de Control
## Condicionales (if, elif, else)
if edad >= 18:
  print("Eres mayor de edad")
elif edad >= 13:
  print("Eres adolescente")
else:
  print("Eres niño")

## Buncle
### for (itera sobre una secuencia)
for fruta in frutas:
  print(fruta)

### while (ejecuta mientras se cumpla condición)
contador = 0
while contador < 5:
  print(contador)
  contador += 1

# 4. Funciones 
## Se definen con def
def saludar(nombre):
  return f"Hola, {nombre}!"

print(saludar("Jhofran")) # Output: "Hola, Jhofran!"

# 5. Entrada/Salida Basica
## input:
nombre_usuario = input("¿Cuál es tu nombre?")

## print:
print("Hola,", nombre_usuario)

# 6. Comentarios
## Una linea:
# esto es un comentario de una linea

## Multiples lineas (usando también como docstrings)
"""
Este es un comentario de
multiples lineas
"""

# 7. Manejo de Errores (try/except)
try:
  resultado = 10 / 0
except ZeroDivisionError:
  print("No se puede dividir por cero")

# Reglas Clave de Si
'''
  Python utiliza sangría para indicar un bloque de código.

  La sangría se refiere a los espacios al comienzo de una línea de código.

  Case Sensitive: variable ≠ Variable.

  Snake Case: Para nombres de variables/funciones: mi_variable, calcular_promedio.
'''

# add this