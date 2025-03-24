################################################################################
# Lambdas en Python
################################################################################

'''
Las expresiones lambda son funciones anónimas (sin nombre) que pueden definirse
en una sola línea. Son útiles para crear funciones simples que se utilizan
brevemente o se pasan como argumentos a otras funciones.

Sintaxis básica:
    lambda argumentos: expresión

Características:
- Pueden tener cualquier número de argumentos pero solo una expresión
- La expresión se evalúa y se devuelve automáticamente
- No pueden contener declaraciones ni anotaciones
- Son ideales para operaciones simples y de un solo uso
'''

################################################################################
# Ejemplos Básicos
################################################################################

# Función tradicional vs. Lambda
def cuadrado(x):
    return x * x

# Equivalente con lambda
cuadrado_lambda = lambda x: x * x

# Uso
print("Función tradicional:", cuadrado(5))
print("Función lambda:", cuadrado_lambda(5))

# Lambda con múltiples argumentos
suma = lambda x, y: x + y
print("Suma con lambda:", suma(3, 4))

# Lambda con argumentos por defecto
saludo = lambda nombre="Usuario": f"Hola, {nombre}!"
print(saludo())
print(saludo("María"))

################################################################################
# Uso con funciones de orden superior
################################################################################

# map() - Aplica una función a cada elemento de un iterable
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x * x, numeros))
print("Map con lambda (cuadrados):", cuadrados)

# filter() - Filtra elementos según una condición
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Filter con lambda (pares):", pares)

# sorted() - Ordena con una función personalizada
estudiantes = [
    {"nombre": "Ana", "nota": 85},
    {"nombre": "Carlos", "nota": 92},
    {"nombre": "Berta", "nota": 78}
]

# Ordenar por nota (de mayor a menor)
ordenados_por_nota = sorted(estudiantes, key=lambda e: e["nota"], reverse=True)
print("\nEstudiantes ordenados por nota:")
for e in ordenados_por_nota:
    print(f"{e['nombre']}: {e['nota']}")

# Ordenar por nombre
ordenados_por_nombre = sorted(estudiantes, key=lambda e: e["nombre"])
print("\nEstudiantes ordenados por nombre:")
for e in ordenados_por_nombre:
    print(f"{e['nombre']}: {e['nota']}")

################################################################################
# Lambdas en algoritmos de ordenamiento
################################################################################

# Recordando nuestros algoritmos de ordenamiento, podemos usar lambdas
# para personalizar el criterio de ordenamiento

def quick_sort_con_key(arr, key=lambda x: x):
    '''Quick sort que acepta una función key para determinar el orden'''
    if len(arr) <= 1:
        return arr
    
    pivote = arr[-1]
    pivote_valor = key(pivote)
    
    menores = [x for x in arr[:-1] if key(x) <= pivote_valor]
    mayores = [x for x in arr[:-1] if key(x) > pivote_valor]
    
    return quick_sort_con_key(menores, key) + [pivote] + quick_sort_con_key(mayores, key)

# Ejemplo: ordenar una lista de tuplas por el segundo elemento
datos = [(1, 5), (3, 2), (2, 8), (4, 3)]
ordenados = quick_sort_con_key(datos, key=lambda x: x[1])
print("\nOrdenamiento con lambda como key:")
print(f"Original: {datos}")
print(f"Ordenado por segundo elemento: {ordenados}")

################################################################################
# Lambdas en comprensiones de listas
################################################################################

# Podemos combinar lambdas con comprensiones de listas
calculos = [(lambda x: x**2)(i) for i in range(1, 6)]
print("\nLambdas en comprensiones de listas:", calculos)

# Crear una lista de funciones
multiplicadores = [(lambda x, y=i: x * y) for i in range(1, 6)]
print("\nResultados de multiplicadores:")
for m in multiplicadores:
    print(f"Multiplicar por {multiplicadores.index(m)+1}: {m(10)}")

################################################################################
# Lambdas para funciones parciales
################################################################################

from functools import partial

# Función tradicional
def potencia(base, exponente):
    return base ** exponente

# Usando lambda para crear una función parcial
cuadrado_lambda = lambda x: potencia(x, 2)
cubo_lambda = lambda x: potencia(x, 3)

# Usando partial (alternativa a lambda para funciones parciales)
cuadrado_partial = partial(potencia, exponente=2)
cubo_partial = partial(potencia, exponente=3)

print("\nFunciones parciales:")
print(f"Cuadrado con lambda: {cuadrado_lambda(4)}")
print(f"Cubo con lambda: {cubo_lambda(4)}")
print(f"Cuadrado con partial: {cuadrado_partial(4)}")
print(f"Cubo con partial: {cubo_partial(4)}")

################################################################################
# Ventajas y desventajas de lambdas
################################################################################

'''
Ventajas:
- Código más conciso para funciones simples
- Útiles como argumentos para funciones de orden superior (map, filter, sorted)
- Mejoran la legibilidad cuando se usan apropiadamente
- No contaminan el espacio de nombres con funciones de un solo uso

Desventajas:
- Pueden reducir la legibilidad si son demasiado complejas
- Limitadas a una sola expresión
- No pueden contener documentación (docstrings)
- Pueden ser difíciles de depurar en caso de errores
'''

################################################################################
# Buenas prácticas
################################################################################

'''
1. Usa lambdas para operaciones simples y de un solo uso
2. Prefiere funciones normales para lógica compleja
3. Evita anidar múltiples lambdas
4. Usa nombres descriptivos cuando asignes lambdas a variables
5. Considera alternativas como functools.partial para funciones parciales
'''

################################################################################
# Aplicación práctica: Ordenamiento personalizado
################################################################################

# Ordenar una lista de productos por diferentes criterios
productos = [
    {"id": 1, "nombre": "Laptop", "precio": 1200, "stock": 5},
    {"id": 2, "nombre": "Monitor", "precio": 300, "stock": 15},
    {"id": 3, "nombre": "Teclado", "precio": 80, "stock": 25},
    {"id": 4, "nombre": "Mouse", "precio": 50, "stock": 30},
    {"id": 5, "nombre": "Disco SSD", "precio": 150, "stock": 10}
]

# Función para mostrar productos
def mostrar_productos(titulo, productos):
    print(f"\n{titulo}:")
    for p in productos:
        print(f"ID: {p['id']}, {p['nombre']}, ${p['precio']}, Stock: {p['stock']}")

# Ordenamientos con lambdas
por_precio_asc = sorted(productos, key=lambda p: p["precio"])
por_precio_desc = sorted(productos, key=lambda p: p["precio"], reverse=True)
por_stock = sorted(productos, key=lambda p: p["stock"], reverse=True)
por_nombre = sorted(productos, key=lambda p: p["nombre"])

# Ordenamiento por múltiples criterios (primero por stock, luego por precio)
por_stock_y_precio = sorted(productos, key=lambda p: (p["stock"], p["precio"]), reverse=True)

# Mostrar resultados
mostrar_productos("Productos originales", productos)
mostrar_productos("Ordenados por precio (ascendente)", por_precio_asc)
mostrar_productos("Ordenados por precio (descendente)", por_precio_desc)
mostrar_productos("Ordenados por stock (mayor a menor)", por_stock)
mostrar_productos("Ordenados por nombre", por_nombre)
mostrar_productos("Ordenados por stock y precio", por_stock_y_precio)

################################################################################
# Conclusión
################################################################################

'''
Las expresiones lambda son una herramienta poderosa en Python que permite
escribir código más conciso y funcional. Son especialmente útiles cuando
trabajamos con funciones de orden superior como map, filter y sorted.

Sin embargo, es importante usarlas con moderación y solo para casos simples.
Para lógica más compleja, las funciones tradicionales siguen siendo la mejor opción
por su legibilidad, documentación y facilidad de mantenimiento.

Dominar las lambdas te permite escribir código más elegante y expresivo,
especialmente cuando trabajas con programación funcional en Python.
'''