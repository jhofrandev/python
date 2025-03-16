"""
  Las funciones en Python son bloques de código reutilizables diseñados para realizar
  una tarea específica. Permiten organizar el código, evitar repeticiones y hacer
  el programa más modular y mantenible.
"""

################################################################################
## Definición básica de funciones
################################################################################

# Sintaxis básica para definir una función
def saludar():
    """Esta es una función simple que imprime un saludo."""
    print("¡Hola, mundo!")

# Llamada a la función
saludar()

# Función con parámetros
def saludar_persona(nombre):
    """Saluda a una persona específica."""
    print(f"¡Hola, {nombre}!")

saludar_persona("Ana")
saludar_persona("Juan")

# Función con valor de retorno
def sumar(a, b):
    """Suma dos números y devuelve el resultado."""
    return a + b

resultado = sumar(5, 3)
print(f"La suma es: {resultado}")

################################################################################
## Parámetros y argumentos
################################################################################

# Parámetros posicionales
def describir_persona(nombre, edad, profesion):
    """Describe a una persona con sus atributos."""
    print(f"{nombre} tiene {edad} años y es {profesion}.")

describir_persona("Carlos", 30, "ingeniero")

# Parámetros con valores por defecto
def saludar_con_idioma(nombre, idioma="español"):
    """Saluda en el idioma especificado (español por defecto)."""
    if idioma == "español":
        print(f"¡Hola, {nombre}!")
    elif idioma == "inglés":
        print(f"Hello, {nombre}!")
    else:
        print(f"No conozco ese idioma, pero... ¡Hola, {nombre}!")

saludar_con_idioma("María")
saludar_con_idioma("John", "inglés")

# Argumentos nombrados (keyword arguments)
describir_persona(nombre="Elena", profesion="médica", edad=35)

# Mezcla de argumentos posicionales y nombrados
# Los posicionales deben ir primero
describir_persona("Pedro", profesion="abogado", edad=42)

################################################################################
## Número variable de argumentos
################################################################################

# *args: Número variable de argumentos posicionales
def sumar_varios(*numeros):
    """Suma un número variable de argumentos."""
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado

print(sumar_varios(1, 2, 3, 4, 5))  # 15

# **kwargs: Número variable de argumentos nombrados
def mostrar_datos(**datos):
    """Muestra los datos proporcionados como pares clave-valor."""
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_datos(nombre="Laura", edad=28, ciudad="Madrid", profesion="diseñadora")

# Combinando *args y **kwargs
def funcion_completa(param_obligatorio, *args, param_con_default="valor", **kwargs):
    """Ejemplo de función con diferentes tipos de parámetros."""
    print(f"Parámetro obligatorio: {param_obligatorio}")
    print(f"Args: {args}")
    print(f"Parámetro con valor por defecto: {param_con_default}")
    print(f"Kwargs: {kwargs}")

funcion_completa("Obligatorio", 1, 2, 3, param_con_default="Personalizado", x=10, y=20)

################################################################################
## Desempaquetado de argumentos
################################################################################

# Desempaquetado de listas o tuplas con *
numeros = [1, 2, 3, 4, 5]
print(sumar_varios(*numeros))  # Equivalente a sumar_varios(1, 2, 3, 4, 5)

# Desempaquetado de diccionarios con **
datos_persona = {"nombre": "Roberto", "edad": 45, "profesion": "arquitecto"}
describir_persona(**datos_persona)  # Equivalente a describir_persona(nombre="Roberto", edad=45, profesion="arquitecto")

################################################################################
## Ámbito de variables (scope)
################################################################################

# Variables locales: solo existen dentro de la función
def funcion_con_variable_local():
    x = 10  # Variable local
    print(f"Dentro de la función: x = {x}")

funcion_con_variable_local()
# print(x)  # Esto generaría un error porque x solo existe dentro de la función

# Variables globales: existen fuera de las funciones
y = 20  # Variable global

def funcion_con_variable_global():
    print(f"Dentro de la función: y = {y}")  # Puede acceder a la variable global

funcion_con_variable_global()

# Modificar variables globales dentro de una función
z = 30  # Variable global

def modificar_global():
    global z  # Declaramos que queremos usar la variable global z
    z = 40    # Modificamos la variable global

print(f"Antes de la función: z = {z}")
modificar_global()
print(f"Después de la función: z = {z}")

################################################################################
## Funciones anidadas
################################################################################

def funcion_externa(x):
    """Función que contiene otra función dentro."""
    
    def funcion_interna(y):
        """Función definida dentro de otra función."""
        return x + y
    
    # Usamos la función interna
    return funcion_interna(5)

print(funcion_externa(10))  # 15

# Closures: funciones que recuerdan el entorno donde fueron creadas
def crear_incrementador(incremento):
    """Crea una función que incrementa por un valor específico."""
    
    def incrementar(x):
        return x + incremento
    
    return incrementar

incrementar_por_2 = crear_incrementador(2)
incrementar_por_5 = crear_incrementador(5)

print(incrementar_por_2(10))  # 12
print(incrementar_por_5(10))  # 15

################################################################################
## Funciones lambda (anónimas)
################################################################################

# Funciones lambda: funciones anónimas de una sola expresión
sumar_lambda = lambda a, b: a + b
print(sumar_lambda(3, 4))  # 7

# Uso común: como función de orden superior
numeros = [1, 5, 2, 8, 3]
numeros_ordenados = sorted(numeros)  # Ordenamiento normal
print(numeros_ordenados)  # [1, 2, 3, 5, 8]

# Ordenar una lista de tuplas por el segundo elemento
pares = [(1, 'b'), (3, 'a'), (2, 'c')]
pares_ordenados = sorted(pares, key=lambda par: par[1])
print(pares_ordenados)  # [(3, 'a'), (1, 'b'), (2, 'c')]

################################################################################
## Funciones de orden superior
################################################################################

# Funciones que reciben o devuelven otras funciones

# map: aplica una función a cada elemento de un iterable
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)  # [1, 4, 9, 16, 25]

# filter: filtra elementos según una función
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4]

# reduce: reduce un iterable a un solo valor
from functools import reduce
suma_total = reduce(lambda x, y: x + y, numeros)
print(suma_total)  # 15 (1+2+3+4+5)

################################################################################
## Decoradores
################################################################################

# Decoradores: funciones que modifican el comportamiento de otras funciones
def mi_decorador(funcion):
    """Decorador simple que imprime mensajes antes y después de llamar a la función."""
    
    def wrapper():
        print("Antes de llamar a la función")
        funcion()
        print("Después de llamar a la función")
    
    return wrapper

@mi_decorador
def saludar_decorada():
    print("¡Hola desde la función decorada!")

saludar_decorada()

# Decoradores con argumentos
def decorador_con_args(funcion):
    def wrapper(*args, **kwargs):
        print(f"Argumentos recibidos: {args}, {kwargs}")
        return funcion(*args, **kwargs)
    return wrapper

@decorador_con_args
def suma_decorada(a, b):
    return a + b

print(suma_decorada(5, 3))

################################################################################
## Recursividad
################################################################################

# Funciones recursivas: funciones que se llaman a sí mismas
def factorial(n):
    """Calcula el factorial de n de forma recursiva."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 120 (5*4*3*2*1)

# Fibonacci recursivo
def fibonacci(n):
    """Calcula el n-ésimo número de Fibonacci de forma recursiva."""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print([fibonacci(i) for i in range(10)])  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

################################################################################
## Documentación de funciones
################################################################################

def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.
    
    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.
        
    Returns:
        float: El área del rectángulo.
        
    Raises:
        ValueError: Si la base o la altura son negativas.
    """
    if base < 0 or altura < 0:
        raise ValueError("La base y la altura deben ser positivas")
    return base * altura

# Acceder a la documentación
print(area_rectangulo.__doc__)
help(area_rectangulo)

################################################################################
## Type hints (anotaciones de tipo)
################################################################################

# Python 3.5+ permite anotaciones de tipo para mejorar la legibilidad
def saludar_con_tipo(nombre: str) -> str:
    """Saluda a una persona y devuelve el mensaje."""
    return f"¡Hola, {nombre}!"

mensaje = saludar_con_tipo("Laura")
print(mensaje)

# Anotaciones más complejas
from typing import List, Dict, Tuple, Optional

def procesar_datos(numeros: List[int], 
                  config: Dict[str, str], 
                  rango: Tuple[int, int], 
                  factor: Optional[float] = None) -> List[float]:
    """Ejemplo de función con anotaciones de tipo complejas."""
    resultado = []
    for num in numeros:
        if num >= rango[0] and num <= rango[1]:
            valor = num * (factor if factor is not None else 1.0)
            resultado.append(valor)
    return resultado

################################################################################
## Buenas prácticas
################################################################################

# 1. Nombres descriptivos para funciones y parámetros
def calcular_promedio(numeros):
    """Mejor que 'calc_prom' o 'función1'."""
    return sum(numeros) / len(numeros)

# 2. Una función debe hacer una sola cosa bien (principio de responsabilidad única)

# 3. Documentar funciones con docstrings

# 4. Usar valores por defecto inmutables
# Mal:
def añadir_item(item, lista=[]):  # ¡Peligroso! La lista se comparte entre llamadas
    lista.append(item)
    return lista

# Bien:
def añadir_item_correcto(item, lista=None):
    if lista is None:
        lista = []
    lista.append(item)
    return lista

# 5. Evitar efectos secundarios (modificar variables globales o parámetros mutables)

# 6. Mantener las funciones cortas y enfocadas

# 7. Usar excepciones para manejar errores, no valores de retorno especiales