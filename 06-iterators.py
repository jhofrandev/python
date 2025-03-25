################################################################################
# Iteradores en Python
################################################################################

'''
Los iteradores son objetos que permiten recorrer colecciones de datos, como listas,
tuplas, diccionarios, etc. Son la base de muchas características de Python como
bucles for, comprensiones de listas y generadores.

Un iterador en Python debe implementar dos métodos especiales:
- __iter__(): Devuelve el objeto iterador en sí mismo
- __next__(): Devuelve el siguiente elemento de la colección o lanza StopIteration si no hay más elementos
'''

################################################################################
# Iteradores Básicos
################################################################################

# Ejemplo 1: Usando iteradores integrados
print("Ejemplo 1: Iteradores integrados")
mi_lista = [1, 2, 3, 4, 5]

# Obtener un iterador de la lista
iterador = iter(mi_lista)

# Usar next() para obtener elementos
print(next(iterador))  # 1
print(next(iterador))  # 2
print(next(iterador))  # 3
print(next(iterador))  # 4
print(next(iterador))  # 5

try:
    print(next(iterador))  # Esto lanzará StopIteration
except StopIteration:
    print("No hay más elementos en el iterador")

# Ejemplo 2: Bucle for usa iteradores internamente
print("\nEjemplo 2: Bucle for con iteradores")
for elemento in mi_lista:
    print(elemento, end=" ")
print()

# Lo que hace el bucle for es equivalente a:
iterador = iter(mi_lista)
while True:
    try:
        elemento = next(iterador)
        print(elemento, end=" ")
    except StopIteration:
        break
print()

################################################################################
# Creando Iteradores Personalizados
################################################################################

# Ejemplo 3: Implementando un iterador personalizado
print("\nEjemplo 3: Iterador personalizado")

class ContadorIterador:
    def __init__(self, max):
        self.max = max
        self.numero = 0
    
    def __iter__(self):
        # El iterador es el propio objeto
        return self
    
    def __next__(self):
        if self.numero < self.max:
            self.numero += 1
            return self.numero
        else:
            # No hay más elementos
            raise StopIteration

# Usar nuestro iterador personalizado
contador = ContadorIterador(5)
for num in contador:
    print(num, end=" ")
print()

# Ejemplo 4: Iterador de Fibonacci
print("\nEjemplo 4: Iterador de Fibonacci")

class FibonacciIterador:
    def __init__(self, max_num):
        self.max_num = max_num
        self.a, self.b = 0, 1
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count < self.max_num:
            if self.count == 0:
                self.count += 1
                return self.a
            elif self.count == 1:
                self.count += 1
                return self.b
            else:
                self.a, self.b = self.b, self.a + self.b
                self.count += 1
                return self.b
        else:
            raise StopIteration

# Usar el iterador de Fibonacci
fib = FibonacciIterador(10)
print("Secuencia de Fibonacci:")
for num in fib:
    print(num, end=" ")
print()

################################################################################
# Iterables vs Iteradores
################################################################################

'''
Es importante distinguir entre iterables e iteradores:

- Iterable: Un objeto que implementa __iter__() y puede proporcionar un iterador
  (ejemplos: listas, tuplas, diccionarios, cadenas)
  
- Iterador: Un objeto que implementa __iter__() y __next__() y mantiene el estado
  durante la iteración
'''

# Ejemplo 5: Creando un iterable personalizado
print("\nEjemplo 5: Iterable personalizado")

class RangoPersonalizado:
    """Un iterable similar a range() pero que devuelve un nuevo iterador cada vez"""
    
    def __init__(self, inicio, fin, paso=1):
        self.inicio = inicio
        self.fin = fin
        self.paso = paso
    
    def __iter__(self):
        # Devuelve un nuevo iterador cada vez
        return RangoIterador(self.inicio, self.fin, self.paso)

class RangoIterador:
    """El iterador para RangoPersonalizado"""
    
    def __init__(self, inicio, fin, paso):
        self.actual = inicio
        self.fin = fin
        self.paso = paso
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.paso > 0 and self.actual < self.fin) or (self.paso < 0 and self.actual > self.fin):
            valor = self.actual
            self.actual += self.paso
            return valor
        else:
            raise StopIteration

# Usar nuestro iterable personalizado
rango = RangoPersonalizado(1, 10, 2)

print("Primera iteración:")
for num in rango:
    print(num, end=" ")
print()

print("Segunda iteración (mismo objeto):")
for num in rango:
    print(num, end=" ")
print()

################################################################################
# Generadores: Una Forma Simplificada de Crear Iteradores
################################################################################

'''
Los generadores son una forma simplificada de crear iteradores. 
Se definen como funciones pero usan 'yield' en lugar de 'return'.
Cada vez que se llama a next(), la función se ejecuta hasta el próximo 'yield'.
'''

# Ejemplo 6: Función generadora simple
print("\nEjemplo 6: Función generadora")

def contador_generador(max):
    numero = 0
    while numero < max:
        numero += 1
        yield numero

# Usar el generador
gen = contador_generador(5)
for num in gen:
    print(num, end=" ")
print()

# Ejemplo 7: Generador de Fibonacci
print("\nEjemplo 7: Generador de Fibonacci")

def fibonacci_generador(max_num):
    a, b = 0, 1
    count = 0
    while count < max_num:
        if count == 0:
            yield a
        elif count == 1:
            yield b
        else:
            a, b = b, a + b
            yield b
        count += 1

# Usar el generador de Fibonacci
print("Secuencia de Fibonacci con generador:")
for num in fibonacci_generador(10):
    print(num, end=" ")
print()

# Ejemplo 8: Expresiones generadoras
print("\nEjemplo 8: Expresiones generadoras")

# Similar a las comprensiones de listas pero con paréntesis
cuadrados_gen = (x**2 for x in range(1, 6))
print("Cuadrados con expresión generadora:")
for cuadrado in cuadrados_gen:
    print(cuadrado, end=" ")
print()

################################################################################
# Iteradores en la Biblioteca Estándar
################################################################################

# Ejemplo 9: Iteradores en itertools
print("\nEjemplo 9: Iteradores en itertools")
import itertools

# count: cuenta infinitamente desde un número
contador = itertools.count(1)
print("itertools.count:")
for _ in range(5):
    print(next(contador), end=" ")
print()

# cycle: cicla infinitamente a través de un iterable
ciclo = itertools.cycle(['A', 'B', 'C'])
print("itertools.cycle:")
for _ in range(7):
    print(next(ciclo), end=" ")
print()

# chain: encadena iterables
cadena = itertools.chain([1, 2], [3, 4], [5, 6])
print("itertools.chain:")
for num in cadena:
    print(num, end=" ")
print()

# islice: corta un iterador
infinito = itertools.count()
cortado = itertools.islice(infinito, 5, 10)
print("itertools.islice:")
for num in cortado:
    print(num, end=" ")
print()

################################################################################
# Aplicaciones Prácticas
################################################################################

# Ejemplo 10: Procesamiento de archivos grandes
print("\nEjemplo 10: Procesamiento de archivos")

def leer_lineas(nombre_archivo):
    """Lee un archivo línea por línea usando un generador"""
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            yield linea.strip()

# Este código leería un archivo línea por línea sin cargarlo todo en memoria
# Comentado porque no tenemos un archivo de ejemplo
'''
for linea in leer_lineas('archivo_grande.txt'):
    print(linea)
'''

# Ejemplo 11: Generador para procesar datos en lotes
print("\nEjemplo 11: Procesamiento por lotes")

def procesar_por_lotes(datos, tamano_lote):
    """Divide una lista grande en lotes más pequeños"""
    for i in range(0, len(datos), tamano_lote):
        yield datos[i:i + tamano_lote]

# Datos de ejemplo
datos_grandes = list(range(1, 21))  # 20 elementos
tamano_lote = 5

print(f"Procesando {len(datos_grandes)} elementos en lotes de {tamano_lote}:")
for i, lote in enumerate(procesar_por_lotes(datos_grandes, tamano_lote), 1):
    print(f"Lote {i}: {lote}")

################################################################################
# Ventajas de los Iteradores
################################################################################

'''
1. Eficiencia de memoria: No necesitan cargar todos los datos en memoria
2. Evaluación perezosa: Los elementos se calculan solo cuando se necesitan
3. Composición: Pueden combinarse para crear flujos de datos complejos
4. Infinitud: Pueden representar secuencias infinitas
5. Simplicidad: Simplifican el código para recorrer colecciones
'''

################################################################################
# Conclusiones
################################################################################

'''
Los iteradores son una parte fundamental de Python que permiten:

1. Recorrer colecciones de datos de manera eficiente
2. Procesar grandes volúmenes de datos sin cargarlos completamente en memoria
3. Crear secuencias personalizadas, incluso infinitas
4. Simplificar el código mediante generadores
5. Componer operaciones de procesamiento de datos

Los generadores son una forma simplificada de crear iteradores y son
especialmente útiles para trabajar con grandes conjuntos de datos o
secuencias infinitas.

El módulo itertools proporciona muchas herramientas útiles para trabajar
con iteradores y crear flujos de datos complejos.
'''