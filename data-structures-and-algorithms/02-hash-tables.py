"""
  Tablas Hash en Python
  
  Este archivo explora la implementación y uso de tablas hash,
  una estructura de datos fundamental para almacenamiento y recuperación
  eficiente de información mediante claves.
"""

################################################################################
## Diccionarios: Implementación de Tablas Hash en Python
################################################################################

print("\n--- Diccionarios como Tablas Hash ---")

# Crear un diccionario (tabla hash)
persona = {
    "nombre": "Ana",
    "edad": 28,
    "profesion": "Ingeniera",
    "ciudad": "Madrid"
}

# Acceso a valores mediante claves (operación O(1) en promedio)
print(f"Nombre: {persona['nombre']}")
print(f"Edad: {persona['edad']}")

# Modificar valores
persona["edad"] = 29
print(f"Edad actualizada: {persona['edad']}")

# Agregar nuevos pares clave-valor
persona["email"] = "ana@ejemplo.com"
print(f"Diccionario actualizado: {persona}")

# Verificar si una clave existe
if "telefono" in persona:
    print(f"Teléfono: {persona['telefono']}")
else:
    print("No se encontró el teléfono")

# Eliminar un par clave-valor
del persona["profesion"]
print(f"Después de eliminar 'profesion': {persona}")

# Obtener todas las claves y valores
print(f"Claves: {list(persona.keys())}")
print(f"Valores: {list(persona.values())}")
print(f"Pares clave-valor: {list(persona.items())}")

################################################################################
## Funcionamiento interno de las Tablas Hash
################################################################################

print("\n--- Funcionamiento interno ---")

# 1. Función hash
print("Valores hash de diferentes objetos:")
print(f"hash('python'): {hash('python')}")
print(f"hash(42): {hash(42)}")
print(f"hash(3.14): {hash(3.14)}")
print(f"hash(True): {hash(True)}")

# Las listas y diccionarios no son hasheables (no pueden usarse como claves)
try:
    hash([1, 2, 3])
except TypeError as e:
    print(f"Error al intentar hash de una lista: {e}")

# 2. Colisiones
# Cuando dos claves diferentes producen el mismo valor hash
# Python maneja esto internamente usando técnicas como encadenamiento

# 3. Factor de carga
# Relación entre el número de elementos y el tamaño de la tabla
# Python redimensiona automáticamente los diccionarios para mantener eficiencia

################################################################################
## Implementación personalizada de una Tabla Hash
################################################################################

print("\n--- Implementación personalizada de Tabla Hash ---")

class TablaHash:
    def __init__(self, tamaño=10):
        # Inicializar con una lista de "cubetas" vacías
        self.cubetas = [[] for _ in range(tamaño)]
        self.tamaño = tamaño
        self.elementos = 0
    
    def _hash(self, clave):
        # Función hash simple: convertir la clave a un índice
        return hash(clave) % self.tamaño
    
    def insertar(self, clave, valor):
        # Calcular el índice usando la función hash
        indice = self._hash(clave)
        
        # Buscar si la clave ya existe en la cubeta
        for i, (k, v) in enumerate(self.cubetas[indice]):
            if k == clave:
                # Actualizar el valor si la clave existe
                self.cubetas[indice][i] = (clave, valor)
                return
        
        # Si la clave no existe, agregarla a la cubeta
        self.cubetas[indice].append((clave, valor))
        self.elementos += 1
        
        # Verificar si es necesario redimensionar
        if self.elementos > self.tamaño * 0.7:  # Factor de carga > 0.7
            self._redimensionar()
    
    def obtener(self, clave):
        # Calcular el índice usando la función hash
        indice = self._hash(clave)
        
        # Buscar la clave en la cubeta
        for k, v in self.cubetas[indice]:
            if k == clave:
                return v
        
        # Si la clave no se encuentra, lanzar excepción
        raise KeyError(f"Clave no encontrada: {clave}")
    
    def eliminar(self, clave):
        # Calcular el índice usando la función hash
        indice = self._hash(clave)
        
        # Buscar la clave en la cubeta
        for i, (k, v) in enumerate(self.cubetas[indice]):
            if k == clave:
                # Eliminar el par clave-valor
                del self.cubetas[indice][i]
                self.elementos -= 1
                return
        
        # Si la clave no se encuentra, lanzar excepción
        raise KeyError(f"Clave no encontrada: {clave}")
    
    def contiene(self, clave):
        # Calcular el índice usando la función hash
        indice = self._hash(clave)
        
        # Buscar la clave en la cubeta
        for k, v in self.cubetas[indice]:
            if k == clave:
                return True
        
        return False
    
    def _redimensionar(self):
        # Duplicar el tamaño de la tabla
        nuevo_tamaño = self.tamaño * 2
        nuevas_cubetas = [[] for _ in range(nuevo_tamaño)]
        
        # Rehash de todos los elementos
        for cubeta in self.cubetas:
            for clave, valor in cubeta:
                indice = hash(clave) % nuevo_tamaño
                nuevas_cubetas[indice].append((clave, valor))
        
        # Actualizar la tabla
        self.cubetas = nuevas_cubetas
        self.tamaño = nuevo_tamaño
    
    def __str__(self):
        # Representación en cadena de la tabla hash
        resultado = "{\n"
        for i, cubeta in enumerate(self.cubetas):
            if cubeta:
                resultado += f"  Cubeta {i}: {cubeta}\n"
        resultado += "}"
        return resultado

# Ejemplo de uso de nuestra implementación
tabla = TablaHash()

# Insertar elementos
tabla.insertar("nombre", "Carlos")
tabla.insertar("edad", 35)
tabla.insertar("ciudad", "Barcelona")
tabla.insertar("profesion", "Programador")

print("Tabla hash después de insertar elementos:")
print(tabla)

# Obtener valores
print(f"Nombre: {tabla.obtener('nombre')}")
print(f"Edad: {tabla.obtener('edad')}")

# Verificar si una clave existe
print(f"¿Contiene 'ciudad'? {tabla.contiene('ciudad')}")
print(f"¿Contiene 'telefono'? {tabla.contiene('telefono')}")

# Actualizar un valor
tabla.insertar("edad", 36)
print(f"Edad actualizada: {tabla.obtener('edad')}")

# Eliminar un elemento
tabla.eliminar("profesion")
print("Tabla hash después de eliminar 'profesion':")
print(tabla)

################################################################################
## Aplicaciones de las Tablas Hash
################################################################################

print("\n--- Aplicaciones de las Tablas Hash ---")

# 1. Conteo de frecuencias
texto = "este es un ejemplo de texto para contar frecuencias de palabras en este texto de ejemplo"
palabras = texto.split()

frecuencias = {}
for palabra in palabras:
    if palabra in frecuencias:
        frecuencias[palabra] += 1
    else:
        frecuencias[palabra] = 1

print("Frecuencia de palabras:")
for palabra, frecuencia in frecuencias.items():
    print(f"  '{palabra}': {frecuencia}")

# 2. Caché de resultados (memoización)
def fibonacci_con_cache(n, cache={}):
    # Verificar si el resultado ya está en la caché
    if n in cache:
        return cache[n]
    
    # Calcular el resultado si no está en la caché
    if n <= 1:
        resultado = n
    else:
        resultado = fibonacci_con_cache(n-1) + fibonacci_con_cache(n-2)
    
    # Almacenar el resultado en la caché
    cache[n] = resultado
    return resultado

print("\nSecuencia de Fibonacci con memoización:")
for i in range(10):
    print(f"fibonacci({i}) = {fibonacci_con_cache(i)}")

# 3. Índice invertido (como en motores de búsqueda)
documentos = {
    "doc1": "Python es un lenguaje de programación versátil",
    "doc2": "Las tablas hash son estructuras de datos eficientes",
    "doc3": "Python utiliza tablas hash en sus diccionarios"
}

# Crear un índice invertido
indice = {}
for doc_id, contenido in documentos.items():
    palabras = contenido.lower().split()
    for palabra in palabras:
        if palabra not in indice:
            indice[palabra] = set()
        indice[palabra].add(doc_id)

print("\nÍndice invertido:")
for palabra, docs in sorted(indice.items()):
    print(f"  '{palabra}': {docs}")

# Realizar una búsqueda
consulta = "python tablas"
palabras_consulta = consulta.lower().split()

# Encontrar documentos que contienen todas las palabras de la consulta
resultados = None
for palabra in palabras_consulta:
    if palabra in indice:
        if resultados is None:
            resultados = indice[palabra].copy()
        else:
            resultados &= indice[palabra]  # Intersección de conjuntos
    else:
        resultados = set()
        break

print(f"\nDocumentos que contienen '{consulta}':")
if resultados:
    for doc_id in resultados:
        print(f"  {doc_id}: {documentos[doc_id]}")
else:
    print("  No se encontraron documentos")

################################################################################
## Ventajas y desventajas de las Tablas Hash
################################################################################

print("\n--- Ventajas y desventajas ---")

print("""
Ventajas:
1. Acceso rápido: O(1) en promedio para operaciones de búsqueda, inserción y eliminación
2. Flexibilidad: pueden almacenar cualquier tipo de datos como valores
3. Eficiencia en espacio: solo almacenan los datos necesarios

Desventajas:
1. Sin orden: no mantienen el orden de inserción (excepto en OrderedDict)
2. Colisiones: pueden degradar el rendimiento si la función hash no es adecuada
3. Consumo de memoria: pueden usar más memoria que otras estructuras
4. No adecuadas para búsquedas por rango o parciales
""")

################################################################################
## Variantes de diccionarios en Python
################################################################################

print("\n--- Variantes de diccionarios ---")

# 1. OrderedDict - mantiene el orden de inserción
from collections import OrderedDict

orden_dict = OrderedDict()
orden_dict["c"] = 3
orden_dict["a"] = 1
orden_dict["b"] = 2

print("OrderedDict mantiene el orden de inserción:")
for clave, valor in orden_dict.items():
    print(f"  {clave}: {valor}")

# 2. defaultdict - proporciona un valor predeterminado para claves inexistentes
from collections import defaultdict

# defaultdict con valor predeterminado 0
conteo = defaultdict(int)
for letra in "mississippi":
    conteo[letra] += 1

print("\nConteo de letras con defaultdict:")
for letra, cantidad in conteo.items():
    print(f"  '{letra}': {cantidad}")

# defaultdict con listas como valores predeterminados
agrupacion = defaultdict(list)
datos = [("fruta", "manzana"), ("verdura", "zanahoria"), 
         ("fruta", "plátano"), ("verdura", "lechuga")]

for categoria, item in datos:
    agrupacion[categoria].append(item)

print("\nAgrupación con defaultdict:")
for categoria, items in agrupacion.items():
    print(f"  {categoria}: {items}")

# 3. Counter - especializado en conteo
from collections import Counter

contador = Counter("mississippi")
print("\nConteo con Counter:")
print(f"  {contador}")
print(f"  Letras más comunes: {contador.most_common(2)}")

################################################################################
## Conclusión
################################################################################

print("\n--- Conclusión ---")
print("""
Las tablas hash son estructuras de datos fundamentales que:
1. Permiten acceso rápido a datos mediante claves
2. Son la base de los diccionarios en Python
3. Tienen numerosas aplicaciones prácticas
4. Ofrecen un equilibrio entre velocidad y uso de memoria

Python proporciona varias implementaciones especializadas como
OrderedDict, defaultdict y Counter para casos de uso específicos.
""")