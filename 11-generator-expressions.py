################################################################################
# Expresiones Generadoras en Python
################################################################################

'''
Las expresiones generadoras son construcciones similares a las listas por
comprensión, pero en lugar de crear una lista completa en memoria, crean un
objeto generador que produce valores bajo demanda. Esto las hace más eficientes
en términos de memoria, especialmente para conjuntos de datos grandes.
'''

################################################################################
# Sintaxis Básica y Comparación con Listas por Comprensión
################################################################################

# Ejemplo 1: Comparación básica
print("Ejemplo 1: Comparación básica")

# Lista por comprensión - crea toda la lista en memoria
lista_cuadrados = [x**2 for x in range(10)]
print(f"Lista por comprensión: {lista_cuadrados}")
print(f"Tipo: {type(lista_cuadrados)}")
print(f"Tamaño en memoria: {lista_cuadrados.__sizeof__()} bytes")

# Expresión generadora - crea un generador que produce valores bajo demanda
gen_cuadrados = (x**2 for x in range(10))
print(f"Expresión generadora: {gen_cuadrados}")
print(f"Tipo: {type(gen_cuadrados)}")
print(f"Tamaño en memoria: {gen_cuadrados.__sizeof__()} bytes")

# Convertir generador a lista para ver sus valores
print(f"Valores del generador: {list(gen_cuadrados)}")

# Nota: después de consumir todos los valores, el generador está agotado
print(f"Intentar usar generador agotado: {list(gen_cuadrados)}")  # Lista vacía

################################################################################
# Evaluación Perezosa (Lazy Evaluation)
################################################################################

# Ejemplo 2: Demostración de evaluación perezosa
print("\nEjemplo 2: Evaluación perezosa")

def mostrar_calculo(x):
    print(f"Calculando para {x}")
    return x**2

# Con lista por comprensión - todos los cálculos se realizan inmediatamente
print("Usando lista por comprensión:")
lista = [mostrar_calculo(x) for x in range(5)]
print("Lista creada.")
print(f"Valores: {lista}")

# Con expresión generadora - los cálculos se realizan solo cuando se solicitan
print("\nUsando expresión generadora:")
generador = (mostrar_calculo(x) for x in range(5))
print("Generador creado.")
print("Obteniendo valores uno por uno:")
for valor in generador:
    print(f"Valor obtenido: {valor}")

################################################################################
# Uso de Expresiones Generadoras con Funciones
################################################################################

# Ejemplo 3: Uso con funciones que aceptan iterables
print("\nEjemplo 3: Uso con funciones")

# Suma de cuadrados
suma_cuadrados = sum(x**2 for x in range(1, 101))
print(f"Suma de cuadrados del 1 al 100: {suma_cuadrados}")

# Máximo valor
numeros = [10, 5, 8, 20, 3, 15]
maximo = max(x for x in numeros if x % 2 == 0)
print(f"Máximo valor par: {maximo}")

# Nota: No necesitas paréntesis adicionales cuando la expresión generadora
# es el único argumento de una función

################################################################################
# Encadenamiento de Generadores
################################################################################

# Ejemplo 4: Encadenamiento de operaciones
print("\nEjemplo 4: Encadenamiento de operaciones")

# Filtrar, transformar y limitar datos en una sola expresión
nombres = ['Ana', 'Juan', 'María', 'Pedro', 'Sofía', 'Carlos', 'Laura']

# Obtener las primeras 3 personas cuyo nombre empieza con vocal y convertir a mayúsculas
resultado = (
    nombre.upper() 
    for nombre in nombres 
    if nombre[0].lower() in 'aeiou'
)

# Limitar a los primeros 3 resultados
primeros_tres = list(resultado)[:3]
print(f"Primeros 3 nombres que empiezan con vocal (en mayúsculas): {primeros_tres}")

################################################################################
# Comparación de Rendimiento y Memoria
################################################################################

# Ejemplo 5: Comparación de rendimiento y memoria
print("\nEjemplo 5: Comparación de rendimiento y memoria")
import sys
import time

n = 10_000_000  # 10 millones

# Medir tiempo y memoria para lista por comprensión
inicio = time.time()
lista_grande = [i for i in range(n)]
tiempo_lista = time.time() - inicio
memoria_lista = sys.getsizeof(lista_grande)
print(f"Lista por comprensión:")
print(f"  Tiempo: {tiempo_lista:.4f} segundos")
print(f"  Memoria: {memoria_lista:,} bytes ({memoria_lista / 1024 / 1024:.2f} MB)")

# Medir tiempo y memoria para expresión generadora
inicio = time.time()
gen_grande = (i for i in range(n))
tiempo_gen = time.time() - inicio
memoria_gen = sys.getsizeof(gen_grande)
print(f"Expresión generadora:")
print(f"  Tiempo: {tiempo_gen:.4f} segundos")
print(f"  Memoria: {memoria_gen:,} bytes ({memoria_gen / 1024 / 1024:.2f} MB)")

# Comparación de eficiencia al procesar datos
print("\nProcesando datos:")

# Con lista
inicio = time.time()
suma_lista = sum(lista_grande)
tiempo_suma_lista = time.time() - inicio
print(f"  Suma con lista: {tiempo_suma_lista:.4f} segundos")

# Con generador
inicio = time.time()
suma_gen = sum(i for i in range(n))  # Nuevo generador ya que el anterior está agotado
tiempo_suma_gen = time.time() - inicio
print(f"  Suma con generador: {tiempo_suma_gen:.4f} segundos")

################################################################################
# Casos de Uso Prácticos
################################################################################

# Ejemplo 6: Procesamiento de archivos grandes
print("\nEjemplo 6: Procesamiento de archivos grandes (simulado)")

# Simulamos un archivo grande con líneas
def simular_archivo_grande(n_lineas):
    for i in range(n_lineas):
        yield f"Línea {i}: Contenido de ejemplo con número {i**2}"

# Procesamiento eficiente línea por línea
def procesar_lineas(lineas):
    # Extraer números de cada línea
    numeros = (
        int(linea.split("número ")[1]) 
        for linea in lineas 
        if "número" in linea
    )
    
    # Calcular promedio de números
    total = 0
    count = 0
    for num in numeros:
        total += num
        count += 1
    
    return total / count if count > 0 else 0

# Simular procesamiento de archivo grande
archivo = simular_archivo_grande(1000)
promedio = procesar_lineas(archivo)
print(f"Promedio de números en el archivo: {promedio}")

# Ejemplo 7: Transformación de datos en pipeline
print("\nEjemplo 7: Transformación de datos en pipeline")

datos = [
    "10,manzana,rojo",
    "5,banana,amarillo",
    "8,uva,morado",
    "error_de_formato",
    "3,naranja,naranja",
    "7,fresa,rojo"
]

# Pipeline de procesamiento
def pipeline_procesamiento(lineas):
    # Paso 1: Dividir por comas y filtrar líneas válidas
    campos = (linea.split(',') for linea in lineas)
    validos = (c for c in campos if len(c) == 3)
    
    # Paso 2: Convertir a diccionarios y filtrar por cantidad
    frutas = (
        {"cantidad": int(c[0]), "nombre": c[1], "color": c[2]} 
        for c in validos
    )
    seleccionadas = (f for f in frutas if f["cantidad"] > 5)
    
    # Paso 3: Formatear resultado final
    return (f"{f['nombre'].title()}: {f['cantidad']} unidades" for f in seleccionadas)

# Ejecutar pipeline y mostrar resultados
resultados = pipeline_procesamiento(datos)
print("Frutas seleccionadas:")
for resultado in resultados:
    print(f"  {resultado}")

################################################################################
# Expresiones Generadoras Anidadas
################################################################################

# Ejemplo 8: Generadores anidados
print("\nEjemplo 8: Generadores anidados")

# Generar pares de coordenadas (x,y) donde x e y son pares
coordenadas = (
    (x, y) 
    for x in range(5) 
    for y in range(5) 
    if x % 2 == 0 and y % 2 == 0
)

print("Coordenadas con valores pares:")
for coord in coordenadas:
    print(f"  {coord}")

################################################################################
# Generadores vs. Iteradores
################################################################################

# Ejemplo 9: Comparación con iteradores
print("\nEjemplo 9: Comparación con iteradores")

# Iterador manual
class CuadradosIterador:
    def __init__(self, n):
        self.n = n
        self.i = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        resultado = self.i ** 2
        self.i += 1
        return resultado

# Usando el iterador manual
print("Usando iterador manual:")
iterador = CuadradosIterador(5)
for valor in iterador:
    print(f"  {valor}")

# Usando expresión generadora
print("\nUsando expresión generadora:")
generador = (x**2 for x in range(5))
for valor in generador:
    print(f"  {valor}")

################################################################################
# Buenas Prácticas
################################################################################

'''
1. Usa expresiones generadoras en lugar de listas por comprensión cuando:
   - Trabajas con conjuntos de datos grandes
   - Solo necesitas iterar sobre los resultados una vez
   - Quieres procesar datos de forma incremental

2. Considera el uso de generadores para:
   - Procesamiento de archivos grandes línea por línea
   - Transformaciones de datos en pipeline
   - Cálculos que requieren mucha memoria

3. Recuerda que los generadores se agotan después de una iteración:
   - No puedes reutilizar un generador después de consumirlo
   - Si necesitas los datos múltiples veces, considera convertirlo a lista
     o crear un nuevo generador cada vez

4. Para operaciones complejas, considera dividir la lógica en múltiples
   pasos en lugar de crear una expresión generadora muy compleja
'''

################################################################################
# Ejercicios Prácticos
################################################################################

# Ejercicio 1: Filtrado eficiente de datos
print("\nEjercicio 1: Filtrado eficiente de datos")

# Simulamos una fuente de datos grande
def generar_datos(n):
    import random
    for i in range(n):
        yield {
            "id": i,
            "valor": random.randint(1, 100),
            "categoria": random.choice(["A", "B", "C", "D"])
        }

# Filtrar y transformar datos eficientemente
datos_filtrados = (
    f"ID: {dato['id']}, Valor: {dato['valor']}" 
    for dato in generar_datos(1000) 
    if dato["valor"] > 80 and dato["categoria"] in ["A", "C"]
)

# Mostrar primeros 5 resultados
print("Primeros 5 datos filtrados:")
for _ in range(5):
    try:
        print(f"  {next(datos_filtrados)}")
    except StopIteration:
        print("  No hay más datos")
        break

# Ejercicio 2: Procesamiento de texto eficiente
print("\nEjercicio 2: Procesamiento de texto eficiente")

texto_largo = """
Python es un lenguaje de programación interpretado cuya filosofía hace 
hincapié en la legibilidad de su código. Se trata de un lenguaje de programación 
multiparadigma, ya que soporta orientación a objetos, programación imperativa y, 
en menor medida, programación funcional. Es un lenguaje interpretado, dinámico 
y multiplataforma.
"""

# Contar frecuencia de palabras eficientemente
palabras = (
    palabra.lower().strip(".,;:()\"'") 
    for linea in texto_largo.split("\n") 
    for palabra in linea.split() 
    if palabra.strip()
)

# Usar un diccionario para contar frecuencias
from collections import Counter
frecuencias = Counter(palabras)

# Mostrar palabras más comunes
print("Palabras más comunes:")
for palabra, frecuencia in frecuencias.most_common(5):
    print(f"  '{palabra}': {frecuencia} veces")

################################################################################
# Conclusiones
################################################################################

'''
Las expresiones generadoras son una característica poderosa de Python que ofrece:

1. Eficiencia de memoria: No almacenan todos los elementos en memoria a la vez
2. Evaluación perezosa: Calculan valores solo cuando se necesitan
3. Sintaxis concisa: Similar a las listas por comprensión pero con paréntesis
4. Rendimiento: Ideal para procesar grandes conjuntos de datos

Son especialmente útiles para:
- Procesamiento de archivos grandes
- Transformaciones de datos en pipeline
- Trabajar con conjuntos de datos potencialmente infinitos
- Optimizar el uso de memoria en aplicaciones

Cuando se combinan con otras características de Python como funciones de orden
superior (map, filter, reduce) y bibliotecas como itertools, las expresiones
generadoras se convierten en una herramienta extremadamente poderosa para el
procesamiento de datos eficiente.
'''