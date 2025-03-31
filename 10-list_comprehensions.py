################################################################################
# Listas por Comprensión en Python
################################################################################

'''
Las listas por comprensión (list comprehensions) son una forma concisa y elegante
de crear listas basadas en listas existentes u otros iterables. Proporcionan una
sintaxis más compacta cuando se desea crear una nueva lista basada en los valores
de una lista existente o cuando se quiere generar una secuencia de elementos.
'''

################################################################################
# Sintaxis Básica
################################################################################

# Sintaxis general:
# [expresión for elemento in iterable]

# Ejemplo 1: Lista de cuadrados
print("Ejemplo 1: Lista de cuadrados")
# Método tradicional con bucle for
cuadrados_tradicional = []
for x in range(10):
    cuadrados_tradicional.append(x**2)
print(f"Tradicional: {cuadrados_tradicional}")

# Usando lista por comprensión
cuadrados_comprension = [x**2 for x in range(10)]
print(f"Comprensión: {cuadrados_comprension}")

# Ejemplo 2: Convertir cadenas a mayúsculas
print("\nEjemplo 2: Convertir cadenas a mayúsculas")
frutas = ['manzana', 'banana', 'cereza', 'kiwi', 'mango']
frutas_mayusculas = [fruta.upper() for fruta in frutas]
print(frutas_mayusculas)

################################################################################
# Listas por Comprensión con Condiciones
################################################################################

# Sintaxis con condición:
# [expresión for elemento in iterable if condición]

# Ejemplo 3: Filtrar números pares
print("\nEjemplo 3: Filtrar números pares")
numeros = list(range(1, 21))
pares = [num for num in numeros if num % 2 == 0]
print(f"Números pares del 1 al 20: {pares}")

# Ejemplo 4: Filtrar frutas que contienen 'a'
print("\nEjemplo 4: Filtrar frutas que contienen 'a'")
frutas_con_a = [fruta for fruta in frutas if 'a' in fruta]
print(f"Frutas que contienen 'a': {frutas_con_a}")

################################################################################
# Listas por Comprensión con Múltiples Condiciones
################################################################################

# Ejemplo 5: Números pares y divisibles por 3
print("\nEjemplo 5: Números pares y divisibles por 3")
numeros_filtrados = [num for num in range(1, 31) if num % 2 == 0 if num % 3 == 0]
print(f"Números pares y divisibles por 3 del 1 al 30: {numeros_filtrados}")

# Ejemplo 6: Usando condición if-else en la expresión
print("\nEjemplo 6: Usando condición if-else en la expresión")
# Sintaxis: [expresión_if_verdadero if condición else expresión_if_falso for elemento in iterable]
resultado = ["par" if num % 2 == 0 else "impar" for num in range(1, 11)]
print(f"Clasificación de números del 1 al 10: {resultado}")

################################################################################
# Listas por Comprensión Anidadas
################################################################################

# Ejemplo 7: Matriz de multiplicación
print("\nEjemplo 7: Matriz de multiplicación")
matriz_multiplicacion = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("Matriz de multiplicación 5x5:")
for fila in matriz_multiplicacion:
    print(fila)

# Ejemplo 8: Aplanar una matriz
print("\nEjemplo 8: Aplanar una matriz")
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
aplanada = [elemento for fila in matriz for elemento in fila]
print(f"Matriz original: {matriz}")
print(f"Matriz aplanada: {aplanada}")

################################################################################
# Casos de Uso Prácticos
################################################################################

# Ejemplo 9: Extraer datos específicos de una lista de diccionarios
print("\nEjemplo 9: Extraer datos de diccionarios")
estudiantes = [
    {'nombre': 'Ana', 'edad': 22, 'calificacion': 95},
    {'nombre': 'Juan', 'edad': 20, 'calificacion': 88},
    {'nombre': 'María', 'edad': 25, 'calificacion': 92},
    {'nombre': 'Pedro', 'edad': 19, 'calificacion': 75},
    {'nombre': 'Sofía', 'edad': 23, 'calificacion': 99}
]

# Extraer nombres
nombres = [estudiante['nombre'] for estudiante in estudiantes]
print(f"Nombres de estudiantes: {nombres}")

# Extraer nombres de estudiantes con calificación > 90
buenos_estudiantes = [estudiante['nombre'] for estudiante in estudiantes if estudiante['calificacion'] > 90]
print(f"Estudiantes con calificación > 90: {buenos_estudiantes}")

# Ejemplo 10: Transformación de datos
print("\nEjemplo 10: Transformación de datos")
# Crear diccionarios nombre:calificación
calificaciones = {estudiante['nombre']: estudiante['calificacion'] for estudiante in estudiantes}
print(f"Diccionario de calificaciones: {calificaciones}")

################################################################################
# Rendimiento y Consideraciones
################################################################################

# Ejemplo 11: Comparación de rendimiento
print("\nEjemplo 11: Comparación de rendimiento")
import time

# Generar una lista grande
n = 1000000

# Método tradicional
inicio = time.time()
cuadrados_tradicional = []
for i in range(n):
    cuadrados_tradicional.append(i**2)
fin = time.time()
tiempo_tradicional = fin - inicio
print(f"Tiempo con método tradicional: {tiempo_tradicional:.6f} segundos")

# Método de comprensión
inicio = time.time()
cuadrados_comprension = [i**2 for i in range(n)]
fin = time.time()
tiempo_comprension = fin - inicio
print(f"Tiempo con lista por comprensión: {tiempo_comprension:.6f} segundos")

# Método map (otra alternativa)
inicio = time.time()
cuadrados_map = list(map(lambda x: x**2, range(n)))
fin = time.time()
tiempo_map = fin - inicio
print(f"Tiempo con map: {tiempo_map:.6f} segundos")

################################################################################
# Alternativas a las Listas por Comprensión
################################################################################

# Ejemplo 12: Expresiones generadoras
print("\nEjemplo 12: Expresiones generadoras")
# Las expresiones generadoras son similares pero usan paréntesis y generan valores bajo demanda
generador = (x**2 for x in range(10))
print(f"Tipo de generador: {type(generador)}")
print(f"Valores del generador: {list(generador)}")

# Ejemplo 13: Dict comprehensions
print("\nEjemplo 13: Dict comprehensions")
# Crear un diccionario de número:cuadrado
cuadrados_dict = {x: x**2 for x in range(1, 11)}
print(f"Diccionario de cuadrados: {cuadrados_dict}")

# Ejemplo 14: Set comprehensions
print("\nEjemplo 14: Set comprehensions")
# Crear un conjunto de letras únicas
texto = "python es un lenguaje de programación versátil"
letras_unicas = {letra for letra in texto if letra.isalpha()}
print(f"Letras únicas en el texto: {letras_unicas}")

################################################################################
# Buenas Prácticas
################################################################################

'''
1. Legibilidad: Usa listas por comprensión para casos simples y claros.
   Para lógica compleja, considera usar bucles tradicionales.

2. Longitud: Evita listas por comprensión demasiado largas. Si no cabe en una
   línea de 79-100 caracteres, considera usar un bucle tradicional.

3. Anidamiento: Limita el anidamiento a un máximo de dos niveles para mantener
   la legibilidad.

4. Efectos secundarios: Las listas por comprensión deben usarse para crear listas,
   no para efectos secundarios. Evita cosas como [print(x) for x in range(10)].

5. Rendimiento: Para conjuntos de datos muy grandes, considera usar expresiones
   generadoras en lugar de listas por comprensión para ahorrar memoria.
'''

################################################################################
# Ejercicios Prácticos
################################################################################

# Ejercicio 1: Crear una lista de los primeros 20 números de Fibonacci
print("\nEjercicio 1: Números de Fibonacci")
fibonacci = [0, 1]
[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for _ in range(18)]
print(f"Primeros 20 números de Fibonacci: {fibonacci}")

# Ejercicio 2: Filtrar palabras por longitud
print("\nEjercicio 2: Filtrar palabras por longitud")
palabras = ["Python", "es", "un", "lenguaje", "de", "programación", "poderoso"]
palabras_largas = [palabra for palabra in palabras if len(palabra) > 5]
print(f"Palabras con más de 5 letras: {palabras_largas}")

# Ejercicio 3: Extraer información de una URL
print("\nEjercicio 3: Extraer información de URL")
urls = [
    "https://www.ejemplo.com/pagina1.html",
    "http://blog.ejemplo.com/post/12345",
    "https://api.ejemplo.org/v2/datos",
    "ftp://archivos.ejemplo.net/descargas"
]

# Extraer protocolo y dominio
info_urls = [(url.split("://")[0], url.split("://")[1].split("/")[0]) for url in urls]
print("Información de URLs (protocolo, dominio):")
for info in info_urls:
    print(f"  {info[0]:<5} - {info[1]}")

################################################################################
# Conclusiones
################################################################################

'''
Las listas por comprensión son una característica poderosa de Python que permite:

1. Código más conciso y expresivo
2. Mejor rendimiento en muchos casos
3. Sintaxis clara para transformaciones y filtrados

Son especialmente útiles para:
- Transformar elementos de una lista
- Filtrar elementos basados en condiciones
- Aplanar listas anidadas
- Extraer datos específicos de estructuras complejas

Cuando se usan correctamente, las listas por comprensión hacen que el código sea
más legible y mantenible, siguiendo la filosofía de Python de que "lo explícito
es mejor que lo implícito" y "lo simple es mejor que lo complejo".
'''