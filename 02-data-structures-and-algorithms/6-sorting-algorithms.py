################################################################################## Algoritmos de Ordenamiento en Python
################################################################################


'''
Los algoritmos de ordenamiento son técnicas para reorganizar una lista de elementos
en un orden específico (generalmente ascendente o descendente).

Son fundamentales en ciencias de la computación y se utilizan constantemente
en aplicaciones del mundo real.
'''

import time
import random
import matplotlib.pyplot as plt

################################################################################
## Algoritmos de Ordenamiento Simples
################################################################################

def bubble_sort(arr):
    '''
    Ordenamiento burbuja: compara elementos adyacentes y los intercambia si están en orden incorrecto.
    Complejidad: O(n²) - Simple pero ineficiente para listas grandes
    '''
    n = len(arr)
    for i in range(n):
        # Bandera para optimizar si la lista ya está ordenada
        ordenado = True
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                ordenado = False
        # Si no hubo intercambios, la lista ya está ordenada
        if ordenado:
            break
    return arr

def selection_sort(arr):
    '''
    Ordenamiento por selección: busca el elemento mínimo y lo coloca al principio.
    Complejidad: O(n²) - Simple pero ineficiente para listas grandes
    '''
    n = len(arr)
    for i in range(n):
        # Encontrar el valor mínimo en el resto de la lista
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambiar el mínimo encontrado con el primer elemento
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    '''
    Ordenamiento por inserción: construye la lista ordenada uno a uno.
    Complejidad: O(n²) - Eficiente para listas pequeñas o casi ordenadas
    '''
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Mover elementos mayores que key a una posición adelante
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

################################################################################
## Algoritmos de Ordenamiento Eficientes
################################################################################

def merge_sort(arr):
    '''
    Ordenamiento por mezcla: divide la lista, ordena las partes y las combina.
    Complejidad: O(n log n) - Muy eficiente pero usa memoria adicional
    '''
    if len(arr) <= 1:
        return arr
    
    # Dividir la lista en mitades
    medio = len(arr) // 2
    izquierda = arr[:medio]
    derecha = arr[medio:]
    
    # Llamadas recursivas para ordenar ambas mitades
    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)
    
    # Combinar las mitades ordenadas
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    '''Función auxiliar para combinar dos listas ordenadas'''
    resultado = []
    i = j = 0
    
    # Comparar elementos de ambas listas y añadir el menor a resultado
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    
    # Añadir elementos restantes
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

def quick_sort(arr):
    '''
    Ordenamiento rápido: elige un pivote y particiona la lista.
    Complejidad: O(n log n) promedio, O(n²) peor caso - Muy eficiente en la práctica
    '''
    if len(arr) <= 1:
        return arr
    
    # Elegir pivote (aquí usamos el último elemento)
    pivote = arr[-1]
    
    # Particionar la lista
    menores = [x for x in arr[:-1] if x <= pivote]
    mayores = [x for x in arr[:-1] if x > pivote]
    
    # Llamadas recursivas y combinación
    return quick_sort(menores) + [pivote] + quick_sort(mayores)

def heap_sort(arr):
    '''
    Ordenamiento por montículo: usa una estructura de datos de montón.
    Complejidad: O(n log n) - Eficiente y usa ordenamiento in-place
    '''
    def heapify(arr, n, i):
        # Convertir un árbol binario en un montón (heap)
        mayor = i
        izq = 2 * i + 1
        der = 2 * i + 2
        
        if izq < n and arr[izq] > arr[mayor]:
            mayor = izq
        
        if der < n and arr[der] > arr[mayor]:
            mayor = der
        
        if mayor != i:
            arr[i], arr[mayor] = arr[mayor], arr[i]
            heapify(arr, n, mayor)
    
    n = len(arr)
    
    # Construir un max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extraer elementos uno por uno
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr

################################################################################
## Algoritmos de Ordenamiento de Python
################################################################################

def python_sort(arr):
    '''
    Método sort() nativo de Python: implementa Timsort, una combinación de merge sort e insertion sort.
    Complejidad: O(n log n) - Muy optimizado para diferentes patrones de datos
    '''
    arr_copia = arr.copy()
    arr_copia.sort()
    return arr_copia

def python_sorted(arr):
    '''
    Función sorted() de Python: igual que sort() pero devuelve una nueva lista.
    Complejidad: O(n log n) - Muy optimizado para diferentes patrones de datos
    '''
    return sorted(arr)

################################################################################
## Comparación de Rendimiento
################################################################################

def comparar_algoritmos(tamaños=[100, 500, 1000, 2000], repeticiones=3):
    '''Compara el rendimiento de diferentes algoritmos de ordenamiento'''
    algoritmos = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
        "Heap Sort": heap_sort,
        "Python Sort": python_sort
    }
    
    resultados = {nombre: [] for nombre in algoritmos}
    
    for tamaño in tamaños:
        print(f"\nProbando con listas de tamaño {tamaño}:")
        
        for _ in range(repeticiones):
            # Crear la misma lista aleatoria para todos los algoritmos
            lista = [random.randint(1, 10000) for _ in range(tamaño)]
            
            for nombre, algoritmo in algoritmos.items():
                lista_copia = lista.copy()
                
                # Medir tiempo de ejecución
                inicio = time.time()
                algoritmo(lista_copia)
                fin = time.time()
                
                tiempo = fin - inicio
                print(f"{nombre}: {tiempo:.6f} segundos")
                
                resultados[nombre].append((tamaño, tiempo))
    
    # Graficar resultados
    plt.figure(figsize=(12, 8))
    
    for nombre, datos in resultados.items():
        tamaños_alg = [dato[0] for dato in datos]
        tiempos = [dato[1] for dato in datos]
        
        # Calcular promedios para cada tamaño
        tamaños_unicos = sorted(set(tamaños_alg))
        tiempos_promedio = []
        
        for t in tamaños_unicos:
            tiempos_t = [tiempos[i] for i in range(len(tiempos)) if tamaños_alg[i] == t]
            tiempos_promedio.append(sum(tiempos_t) / len(tiempos_t))
        
        plt.plot(tamaños_unicos, tiempos_promedio, marker='o', label=nombre)
    
    plt.title("Comparación de Algoritmos de Ordenamiento")
    plt.xlabel("Tamaño de la lista")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.grid(True)
    plt.savefig("comparacion_algoritmos.png")
    plt.show()

################################################################################
## Ejemplos de Uso
################################################################################

# Ejemplo básico
lista_ejemplo = [64, 34, 25, 12, 22, 11, 90]
print(f"Lista original: {lista_ejemplo}")
print(f"Bubble Sort: {bubble_sort(lista_ejemplo.copy())}")
print(f"Selection Sort: {selection_sort(lista_ejemplo.copy())}")
print(f"Insertion Sort: {insertion_sort(lista_ejemplo.copy())}")
print(f"Merge Sort: {merge_sort(lista_ejemplo.copy())}")
print(f"Quick Sort: {quick_sort(lista_ejemplo.copy())}")
print(f"Heap Sort: {heap_sort(lista_ejemplo.copy())}")
print(f"Python Sort: {python_sort(lista_ejemplo.copy())}")

# Comparar rendimiento (descomenta para ejecutar)
# comparar_algoritmos()

################################################################################
# Aplicaciones Prácticas
################################################################################

'''
Los algoritmos de ordenamiento se utilizan en:

1. Bases de datos: para indexar y buscar información eficientemente
2. Análisis de datos: para preparar datos para análisis estadístico
3. Interfaces de usuario: para mostrar listas ordenadas al usuario
4. Algoritmos de compresión: como parte del proceso de compresión
5. Algoritmos de búsqueda: para mejorar la eficiencia de búsqueda binaria

Cada algoritmo tiene sus ventajas:
- Bubble, Selection e Insertion: simples de implementar, buenos para listas pequeñas
- Merge y Quick: eficientes para listas grandes
- Heap: bueno cuando se necesita encontrar los k elementos más grandes/pequeños
- Timsort (Python): optimizado para datos del mundo real con patrones variados
'''

################################################################################
## Conclusiones
################################################################################

'''
1. No existe un "mejor" algoritmo de ordenamiento para todos los casos
2. La elección depende del tamaño de los datos, su distribución y requisitos específicos
3. Para uso general en Python, confía en los métodos nativos sort() y sorted()
4. Conocer diferentes algoritmos te permite elegir el más adecuado para casos especiales
5. Los algoritmos de ordenamiento son fundamentales para entender conceptos de eficiencia algorítmica
'''