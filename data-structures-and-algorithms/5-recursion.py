################################################################################## ¿Qué es la Recursión?
################################################################################

'''
La recursión es una técnica de programación donde una función se llama a sí misma para resolver un problema. Es como un espejo frente a otro espejo, creando un efecto infinito, pero con una condición de salida.
'''

################################################################################## Componentes clave de la recursión
################################################################################

'''
- Caso base : La condición que detiene la recursión (¡muy importante para evitar bucles infinitos!)
- Caso recursivo : Donde la función se llama a sí misma con un problema más pequeño
'''

################################################################################## Ejemplo simple de recursión
################################################################################

def factorial(n):
    # Caso base
    if n == 0 or n == 1:
        return 1
    # Caso recursivo
    else:
        return n * factorial(n-1)

# Ejemplo de uso
print(factorial(5))  # 5! = 5 * 4 * 3 * 2 * 1 = 120

################################################################################## Recursión en tu código de BST
################################################################################

'''
En tu implementación de árbol binario de búsqueda, ya estás usando recursión en varias partes:
1. En el método _insertar_recursivo : La función se llama a sí misma para navegar por el árbol hasta encontrar la posición correcta.
2. En el método _buscar_recursivo : Se llama a sí misma para buscar en el subárbol izquierdo o derecho.
3. En el método _inorden_recursivo : Se llama a sí misma para recorrer todo el árbol en orden.
4. En el método _eliminar_recursivo : Se llama a sí misma para encontrar y eliminar un nodo.

## Ventajas de la recursión:
- Hace que el código sea más elegante y fácil de entender para problemas que son naturalmente recursivos
- Ideal para estructuras de datos jerárquicas como árboles y grafos
- Simplifica la solución de problemas complejos dividiéndolos en casos más simples

## Desventajas de la recursión:
- Puede consumir mucha memoria (cada llamada recursiva añade un marco a la pila de llamadas)
- Puede ser menos eficiente que soluciones iterativas
- Riesgo de desbordamiento de pila (stack overflow) si hay demasiadas llamadas recursivas
'''

################################################################################## Ejemplo práctico: Algoritmo de compresión usando recursión
################################################################################

'''
Mencionaste los algoritmos de compresión como una aplicación de los BST. Aquí hay un ejemplo simplificado de cómo la recursión podría usarse en un algoritmo de compresión básico (codificación Huffman):
'''

class NodoHuffman:
    def __init__(self, caracter=None, frecuencia=0):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierdo = None
        self.derecho = None
    
    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

def generar_codigos(nodo, codigo_actual="", codigos={}):
    # Caso base: es un nodo hoja (tiene un carácter)
    if nodo.caracter is not None:
        codigos[nodo.caracter] = codigo_actual
        return
    
    # Caso recursivo: seguir explorando el árbol
    # Añadir '0' para la rama izquierda
    if nodo.izquierdo:
        generar_codigos(nodo.izquierdo, codigo_actual + "0", codigos)
    
    # Añadir '1' para la rama derecha
    if nodo.derecho:
        generar_codigos(nodo.derecho, codigo_actual + "1", codigos)
    
    return codigos

'''
Este es un ejemplo simplificado de cómo la recursión se utiliza en el algoritmo de compresión Huffman para generar códigos de longitud variable para cada carácter.
'''

################################################################################## Consejos para usar recursión en Python:
################################################################################

'''
- Considera el límite de recursión de Python (normalmente 1000 llamadas)
- Usa memoización (guardar resultados ya calculados) para funciones recursivas que calculan lo mismo varias veces
- Considera convertir a iterativo si la profundidad de recursión puede ser grande
'''

# ade this