"""
  Los diccionarios en Python son colecciones de pares clave-valor, donde cada clave debe ser única.
  Son estructuras de datos mutables y no ordenadas (aunque desde Python 3.7 mantienen el orden de inserción).
  Permiten acceso rápido a valores mediante sus claves y son extremadamente versátiles.
"""

################################################################################
## Creación de diccionarios
################################################################################

# Diccionario vacío
diccionario_vacio = {}
diccionario_vacio_alternativo = dict()

# Diccionario con elementos
persona = {
    "nombre": "Ana",
    "edad": 30,
    "profesion": "ingeniera",
    "ciudad": "Madrid"
}

# Usando el constructor dict()
persona2 = dict(nombre="Juan", edad=25, profesion="médico", ciudad="Barcelona")

# A partir de una lista de tuplas (clave, valor)
items = [("a", 1), ("b", 2), ("c", 3)]
diccionario_desde_items = dict(items)
print(diccionario_desde_items)  # {'a': 1, 'b': 2, 'c': 3}

# Usando dict.fromkeys() para crear un diccionario con valores predeterminados
claves = ["a", "b", "c"]
diccionario_desde_claves = dict.fromkeys(claves, 0)  # Todas las claves tendrán valor 0
print(diccionario_desde_claves)  # {'a': 0, 'b': 0, 'c': 0}

# Comprensión de diccionarios
cuadrados = {x: x**2 for x in range(5)}
print(cuadrados)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

################################################################################
## Acceso y modificación
################################################################################

# Acceder a valores mediante claves
print(persona["nombre"])  # Ana

# Acceder con get() (no genera error si la clave no existe)
print(persona.get("telefono"))  # None
print(persona.get("telefono", "No disponible"))  # "No disponible" (valor por defecto)

# Modificar valores
persona["edad"] = 31
print(persona["edad"])  # 31

# Añadir nuevos pares clave-valor
persona["telefono"] = "555-123456"
print(persona)

# Eliminar pares clave-valor
del persona["telefono"]
print(persona)

# Eliminar y devolver un valor
profesion = persona.pop("profesion")
print(f"Profesión eliminada: {profesion}")
print(persona)

# Eliminar y devolver el último par insertado (Python 3.7+)
ultimo_par = persona.popitem()
print(f"Último par eliminado: {ultimo_par}")
print(persona)

# Vaciar el diccionario
persona.clear()
print(persona)  # {}

################################################################################
## Métodos comunes
################################################################################

estudiantes = {
    "Ana": 9.5,
    "Juan": 8.0,
    "María": 9.8,
    "Pedro": 7.5,
    "Laura": 8.9
}

# Obtener todas las claves
claves = estudiantes.keys()
print(f"Claves: {claves}")  # dict_keys(['Ana', 'Juan', 'María', 'Pedro', 'Laura'])

# Obtener todos los valores
valores = estudiantes.values()
print(f"Valores: {valores}")  # dict_values([9.5, 8.0, 9.8, 7.5, 8.9])

# Obtener todos los pares clave-valor como tuplas
items = estudiantes.items()
print(f"Items: {items}")  # dict_items([('Ana', 9.5), ('Juan', 8.0), ...])

# Actualizar un diccionario con otro
nuevos_estudiantes = {"Carlos": 8.5, "Elena": 9.2}
estudiantes.update(nuevos_estudiantes)
print(estudiantes)

# También se puede actualizar con pares clave-valor
estudiantes.update(Roberto=7.8, Sofía=9.0)
print(estudiantes)

# Obtener una copia del diccionario
copia = estudiantes.copy()

################################################################################
## Verificación de claves
################################################################################

# Verificar si una clave existe
print("Ana" in estudiantes)  # True
print("Diego" in estudiantes)  # False

# Verificar si una clave no existe
print("Diego" not in estudiantes)  # True

################################################################################
## Iteración sobre diccionarios
################################################################################

# Iterar sobre las claves (comportamiento por defecto)
print("\nIterando sobre claves:")
for estudiante in estudiantes:
    print(estudiante)

# Iterar explícitamente sobre las claves
print("\nIterando explícitamente sobre claves:")
for estudiante in estudiantes.keys():
    print(estudiante)

# Iterar sobre los valores
print("\nIterando sobre valores:")
for calificacion in estudiantes.values():
    print(calificacion)

# Iterar sobre pares clave-valor
print("\nIterando sobre pares clave-valor:")
for estudiante, calificacion in estudiantes.items():
    print(f"{estudiante}: {calificacion}")

################################################################################
## Diccionarios anidados
################################################################################

# Los diccionarios pueden contener otros diccionarios como valores
universidad = {
    "Informática": {
        "Ana": {"calificación": 9.5, "asistencia": "90%"},
        "Juan": {"calificación": 8.0, "asistencia": "85%"}
    },
    "Matemáticas": {
        "María": {"calificación": 9.8, "asistencia": "95%"},
        "Pedro": {"calificación": 7.5, "asistencia": "80%"}
    }
}

# Acceder a valores en diccionarios anidados
print(universidad["Informática"]["Ana"]["calificación"])  # 9.5

# Modificar valores en diccionarios anidados
universidad["Informática"]["Ana"]["asistencia"] = "92%"
print(universidad["Informática"]["Ana"])

# Añadir un nuevo estudiante a un departamento existente
universidad["Matemáticas"]["Laura"] = {"calificación": 8.9, "asistencia": "88%"}

# Añadir un nuevo departamento
universidad["Física"] = {
    "Carlos": {"calificación": 8.5, "asistencia": "87%"}
}

################################################################################
## Técnicas avanzadas
################################################################################

# Combinar diccionarios (Python 3.9+)
# dict1 | dict2  # Unión de diccionarios
# En versiones anteriores:
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict_combinado = {**dict1, **dict2}  # {'a': 1, 'b': 3, 'c': 4}
print(dict_combinado)

# Ordenar un diccionario por valores
estudiantes_ordenados = dict(sorted(estudiantes.items(), key=lambda item: item[1], reverse=True))
print("Estudiantes ordenados por calificación (mayor a menor):")
for estudiante, calificacion in estudiantes_ordenados.items():
    print(f"{estudiante}: {calificacion}")

# Filtrar un diccionario
aprobados = {k: v for k, v in estudiantes.items() if v >= 8.0}
print(f"Estudiantes aprobados: {aprobados}")

# Transformar valores de un diccionario
calificaciones_redondeadas = {k: round(v) for k, v in estudiantes.items()}
print(f"Calificaciones redondeadas: {calificaciones_redondeadas}")

################################################################################
## Diccionarios y funciones
################################################################################

# Pasar diccionarios a funciones
def mostrar_estudiante(estudiante, **datos):
    print(f"Información de {estudiante}:")
    for clave, valor in datos.items():
        print(f"  {clave}: {valor}")

mostrar_estudiante("Ana", calificación=9.5, asistencia="90%", grupo="A")

# Desempaquetar diccionarios en llamadas a funciones
datos_estudiante = {"calificación": 8.0, "asistencia": "85%", "grupo": "B"}
mostrar_estudiante("Juan", **datos_estudiante)

################################################################################
## defaultdict: diccionario con valores por defecto
################################################################################

from collections import defaultdict

# defaultdict con valor por defecto 0
contador = defaultdict(int)
palabras = ["manzana", "banana", "manzana", "naranja", "banana", "manzana"]

for palabra in palabras:
    contador[palabra] += 1  # No hay error si la clave no existe

print(contador)  # defaultdict(<class 'int'>, {'manzana': 3, 'banana': 2, 'naranja': 1})

# defaultdict con listas como valores por defecto
grupos = defaultdict(list)
estudiantes_datos = [
    ("Informática", "Ana"),
    ("Matemáticas", "María"),
    ("Informática", "Juan"),
    ("Física", "Pedro"),
    ("Matemáticas", "Laura")
]

for departamento, estudiante in estudiantes_datos:
    grupos[departamento].append(estudiante)

print(grupos)
# defaultdict(<class 'list'>, {'Informática': ['Ana', 'Juan'], 'Matemáticas': ['María', 'Laura'], 'Física': ['Pedro']})

################################################################################
## Counter: diccionario especializado para contar
################################################################################

from collections import Counter

# Contar elementos en una lista
contador = Counter(palabras)
print(contador)  # Counter({'manzana': 3, 'banana': 2, 'naranja': 1})

# Métodos útiles de Counter
print(contador.most_common(2))  # [('manzana', 3), ('banana', 2)]
print(contador.total())  # 6 (total de elementos)

################################################################################
## OrderedDict: diccionario que recuerda el orden de inserción
################################################################################

from collections import OrderedDict

# En Python 3.7+ los diccionarios normales ya mantienen el orden,
# pero OrderedDict tiene métodos adicionales

ordenado = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(ordenado)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Mover un elemento al final
ordenado.move_to_end('a')
print(ordenado)  # OrderedDict([('b', 2), ('c', 3), ('a', 1)])

# Mover un elemento al principio
ordenado.move_to_end('a', last=False)
print(ordenado)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

################################################################################
## Rendimiento y consideraciones
################################################################################

# Los diccionarios son muy eficientes para:
# - Acceso por clave: O(1) en promedio
# - Inserción/eliminación: O(1) en promedio
# - Verificación de existencia (in): O(1) en promedio

# Comparación de rendimiento para acceso
import timeit
import random

# Generar datos de prueba
tamaño = 10000
claves = [f"clave_{i}" for i in range(tamaño)]
valores = list(range(tamaño))
buscar = f"clave_{tamaño//2}"

# Crear diccionario y lista de tuplas
diccionario = dict(zip(claves, valores))
lista_tuplas = list(zip(claves, valores))

# Tiempo para buscar en diccionario
tiempo_dict = timeit.timeit(
    stmt=f"diccionario['{buscar}']",
    globals={"diccionario": diccionario, "buscar": buscar},
    number=10000
)

# Tiempo para buscar en lista de tuplas
def buscar_en_lista(lista, clave):
    for k, v in lista:
        if k == clave:
            return v
    return None

tiempo_lista = timeit.timeit(
    stmt=f"buscar_en_lista(lista_tuplas, '{buscar}')",
    globals={"buscar_en_lista": buscar_en_lista, "lista_tuplas": lista_tuplas, "buscar": buscar},
    number=10
)

print(f"Tiempo para buscar en diccionario: {tiempo_dict:.6f} segundos (10000 búsquedas)")
print(f"Tiempo para buscar en lista: {tiempo_lista:.6f} segundos (10 búsquedas)")
print(f"El diccionario es aproximadamente {(tiempo_lista/10)/(tiempo_dict/10000):.1f} veces más rápido")

################################################################################
## Buenas prácticas
################################################################################

# 1. Usar get() para acceder a valores cuando la clave podría no existir
valor = estudiantes.get("Diego", "No registrado")  # No genera KeyError

# 2. Usar setdefault() para establecer un valor solo si la clave no existe
estudiantes.setdefault("Diego", 7.0)  # Añade solo si "Diego" no existe
print(estudiantes["Diego"])  # 7.0

# 3. Usar comprensiones de diccionarios para transformaciones
# En lugar de:
resultado = {}
for k, v in estudiantes.items():
    if v >= 8.0:
        resultado[k] = v
# Mejor:
resultado = {k: v for k, v in estudiantes.items() if v >= 8.0}

# 4. Considerar defaultdict o Counter para casos específicos

# 5. Usar items() para iterar sobre claves y valores simultáneamente

# 6. Recordar que desde Python 3.7, los diccionarios mantienen el orden de inserción

# 7. Para claves que son tuplas de atributos, considerar usar namedtuple como clave
from collections import namedtuple
Punto = namedtuple('Punto', ['x', 'y'])
distancias = {
    Punto(0, 0): 0.0,
    Punto(1, 0): 1.0,
    Punto(0, 1): 1.0,
    Punto(1, 1): 1.414
}
print(distancias[Punto(1, 1)])  # 1.414

# 8. Usar frozenset como clave cuando se necesite un conjunto inmutable como clave
usuarios_por_roles = {
    frozenset(["admin", "editor"]): ["Ana", "Carlos"],
    frozenset(["editor"]): ["Juan", "María"],
    frozenset(["lector"]): ["Pedro", "Laura"]
}

# Buscar usuarios con ciertos roles
roles_buscados = frozenset(["admin", "editor"])
print(f"Usuarios con roles {roles_buscados}: {usuarios_por_roles[roles_buscados]}")

# add this