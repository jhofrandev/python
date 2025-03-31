'''
# Paradigmas de Programación en Python
Python es un lenguaje multiparadigma, lo que significa que soporta varios estilos o enfoques de programación. Esto le da gran flexibilidad y permite a los desarrolladores elegir el paradigma más adecuado para cada problema.

## Principales Paradigmas en Python
### 1. Programación Imperativa
Python permite escribir código que especifica paso a paso cómo debe ejecutarse un programa.
'''

# Ejemplo de programación imperativa
def calcular_suma(numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

numeros = [1, 2, 3, 4, 5]
resultado = calcular_suma(numeros)
print(f"La suma es: {resultado}")

'''
### 2. Programación Orientada a Objetos (POO)
Python implementa completamente el paradigma orientado a objetos con clases, herencia, polimorfismo y encapsulamiento.
'''

# Ejemplo de programación orientada a objetos
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

animales = [Perro("Fido"), Gato("Whiskers")]
for animal in animales:
    print(f"{animal.nombre} hace {animal.hacer_sonido()}")

'''
### 3. Programación Funcional
Python soporta muchos conceptos de programación funcional como funciones de primera clase, funciones lambda, y operaciones de orden superior.
'''

# Ejemplo de programación funcional
from functools import reduce

# Función de orden superior (map)
cuadrados = list(map(lambda x: x**2, range(1, 6)))

# Función de orden superior (filter)
pares = list(filter(lambda x: x % 2 == 0, range(1, 11)))

# Función de orden superior (reduce)
suma = reduce(lambda x, y: x + y, range(1, 6))

print(f"Cuadrados: {cuadrados}")
print(f"Números pares: {pares}")
print(f"Suma: {suma}")


'''
### 4. Programación Procedural
Enfocada en procedimientos o rutinas que operan sobre datos.
'''

# Ejemplo de programación procedural
def calcular_area_rectangulo(ancho, alto):
    return ancho * alto

def calcular_perimetro_rectangulo(ancho, alto):
    return 2 * (ancho + alto)

ancho = 5
alto = 3
area = calcular_area_rectangulo(ancho, alto)
perimetro = calcular_perimetro_rectangulo(ancho, alto)

print(f"Área: {area}, Perímetro: {perimetro}")

'''
### 5. Programación Declarativa
Python permite ciertos estilos declarativos, especialmente con comprensiones y expresiones generadoras.
'''

# Ejemplo de programación declarativa con comprensiones
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Declaramos qué queremos (números pares al cuadrado) en lugar de cómo obtenerlos
resultado = [x**2 for x in numeros if x % 2 == 0]
print(f"Cuadrados de números pares: {resultado}")

'''
### 6. Metaprogramación
Python permite modificar el comportamiento del programa durante su ejecución.
'''

# Ejemplo de metaprogramación con decoradores
def mi_decorador(funcion):
    def wrapper():
        print("Algo antes de llamar a la función")
        funcion()
        print("Algo después de llamar a la función")
    return wrapper

@mi_decorador
def saludar():
    print("¡Hola!")

saludar()