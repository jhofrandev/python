"""
  Los módulos en Python son archivos que contienen definiciones (como funciones y clases) y declaraciones (como asignaciones e importaciones) de Python.
  Permiten organizar el código en unidades lógicas y reutilizables.
  Python tiene una amplia biblioteca estándar con módulos para diversas funcionalidades.
"""

################################################################################
## Importación de módulos
################################################################################

# Importar un módulo completo
import math

# Usar funciones del módulo
radio = 5
area = math.pi * radio**2
print(f"Área del círculo: {area}")

# Calcular seno de 30 grados (convertir a radianes primero)
angulo_grados = 30
angulo_radianes = math.radians(angulo_grados)
seno = math.sin(angulo_radianes)
print(f"Seno de {angulo_grados} grados: {seno}")

# Importar módulos con alias
import math as m
print(f"Pi usando alias: {m.pi}")

# Importar funciones o variables específicas de un módulo
from math import pi, sqrt
print(f"Raíz cuadrada de 16: {sqrt(16)}")
print(f"Pi importado directamente: {pi}")

# Importar todo el contenido de un módulo (no recomendado generalmente)
from random import *
print(f"Número aleatorio: {random()}")

################################################################################
## Módulos comunes de la biblioteca estándar
################################################################################

# Módulo random - generación de números aleatorios
import random

# Número aleatorio entre 0 y 1
print(f"Aleatorio entre 0 y 1: {random.random()}")

# Entero aleatorio en un rango
print(f"Entero aleatorio entre 1 y 10: {random.randint(1, 10)}")

# Selección aleatoria de elementos
colores = ["rojo", "verde", "azul", "amarillo"]
print(f"Color aleatorio: {random.choice(colores)}")

# Mezclar una lista
numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print(f"Lista mezclada: {numeros}")

# Módulo datetime - manejo de fechas y horas
import datetime

# Fecha y hora actual
ahora = datetime.datetime.now()
print(f"Fecha y hora actual: {ahora}")

# Crear una fecha específica
fecha = datetime.date(2023, 12, 31)
print(f"Fecha específica: {fecha}")

# Diferencia entre fechas
otra_fecha = datetime.date(2023, 1, 1)
diferencia = fecha - otra_fecha
print(f"Días entre fechas: {diferencia.days}")

# Formateo de fechas
print(f"Fecha formateada: {ahora.strftime('%d/%m/%Y %H:%M:%S')}")

# Módulo os - interacción con el sistema operativo
import os

# Directorio actual
print(f"Directorio actual: {os.getcwd()}")

# Listar archivos en un directorio
print("Archivos en el directorio actual:")
for archivo in os.listdir('.'):
    print(f"  - {archivo}")

# Verificar si un archivo existe
archivo_ejemplo = "ejemplo.txt"
print(f"¿Existe {archivo_ejemplo}? {os.path.exists(archivo_ejemplo)}")

# Módulo sys - interacción con el intérprete de Python
import sys

# Versión de Python
print(f"Versión de Python: {sys.version}")

# Ruta de búsqueda de módulos
print("Rutas de búsqueda de módulos:")
for ruta in sys.path:
    print(f"  - {ruta}")

################################################################################
## Creación de módulos propios
################################################################################

# Vamos a crear un módulo simple para operaciones matemáticas
# Este código normalmente estaría en un archivo separado llamado 'operaciones.py'

"""
# Contenido de 'operaciones.py'
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

# Variable en el módulo
PI = 3.14159
"""

# Para usar este módulo, lo importaríamos así:
# import operaciones
# resultado = operaciones.sumar(5, 3)

################################################################################
## Paquetes
################################################################################

# Los paquetes son directorios que contienen módulos y un archivo __init__.py
# Estructura de ejemplo:
"""
mi_paquete/
    __init__.py
    modulo1.py
    modulo2.py
    subpaquete/
        __init__.py
        modulo3.py
"""

# Importar desde paquetes
# import mi_paquete.modulo1
# from mi_paquete import modulo2
# from mi_paquete.subpaquete import modulo3

################################################################################
## Módulo como script
################################################################################

# Un módulo puede ser ejecutado como script o importado como módulo
# Para diferenciar, se usa la variable __name__

def funcion_principal():
    print("Ejecutando como script principal")

# Este bloque se ejecuta solo si el archivo se ejecuta directamente
if __name__ == "__main__":
    funcion_principal()
    print("Este módulo se está ejecutando como script")
else:
    print("Este módulo ha sido importado")

################################################################################
## Explorar módulos
################################################################################

# Ver todos los nombres definidos en un módulo
print("\nNombres definidos en el módulo math:")
print(dir(math)[:10])  # Mostrar solo los primeros 10 para brevedad

# Obtener ayuda sobre un módulo o función
# help(math)  # Comentado para no mostrar demasiada información
# help(math.sin)

# Ver la ruta del archivo de un módulo
print(f"\nRuta del módulo math: {math.__file__}")

################################################################################
## Recargar módulos
################################################################################

# Si un módulo cambia durante la ejecución, se puede recargar
import importlib

# Ejemplo (comentado porque no tenemos un módulo real para recargar)
# importlib.reload(mi_modulo)

################################################################################
## Módulos y espacios de nombres
################################################################################

# Cada módulo tiene su propio espacio de nombres
import math
import random

# Aunque ambos módulos podrían tener funciones con el mismo nombre,
# no hay conflicto porque están en espacios de nombres diferentes
print(f"math.ceil(3.7): {math.ceil(3.7)}")
# Si random tuviera una función ceil, se accedería como random.ceil()

################################################################################
## Buenas prácticas
################################################################################

# 1. Importar módulos al principio del archivo

# 2. Preferir importaciones explícitas sobre 'from module import *'
#    Bien:  from math import pi, sqrt
#    Evitar: from math import *

# 3. Usar alias para módulos con nombres largos o para evitar conflictos
#    import numpy as np
#    import pandas as pd

# 4. Organizar las importaciones en grupos:
#    - Módulos de la biblioteca estándar
#    - Módulos de terceros
#    - Módulos propios de la aplicación

# 5. Documentar los módulos con docstrings

# 6. Usar if __name__ == "__main__": para código que debe ejecutarse solo cuando
#    el módulo se ejecuta como script

################################################################################
## Ejemplo práctico: Crear y usar un módulo
################################################################################

# Vamos a simular la creación y uso de un módulo

# Primero, creamos un archivo 'utilidades.py' con este contenido:
"""
# utilidades.py

def formatear_nombre(nombre, apellido):
    '''Formatea un nombre completo en formato "Apellido, Nombre"'''
    return f"{apellido.title()}, {nombre.title()}"

def calcular_edad(año_nacimiento, año_actual=None):
    '''Calcula la edad basada en el año de nacimiento'''
    if año_actual is None:
        import datetime
        año_actual = datetime.datetime.now().year
    return año_actual - año_nacimiento

# Constante
VERSION = "1.0.0"

# Clase de ejemplo
class Persona:
    def __init__(self, nombre, apellido, año_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.año_nacimiento = año_nacimiento
    
    def nombre_completo(self):
        return formatear_nombre(self.nombre, self.apellido)
    
    def edad(self):
        return calcular_edad(self.año_nacimiento)
    
    def __str__(self):
        return f"{self.nombre_completo()} ({self.edad()} años)"
"""

# Luego, usaríamos el módulo así:
"""
# programa_principal.py

# Importar el módulo
import utilidades

# Usar funciones del módulo
nombre_formateado = utilidades.formatear_nombre("juan", "pérez")
print(nombre_formateado)  # "Pérez, Juan"

# Usar la clase del módulo
persona = utilidades.Persona("ana", "garcía", 1990)
print(persona)  # "García, Ana (33 años)"

# Acceder a constantes
print(f"Versión: {utilidades.VERSION}")
"""

################################################################################
## Módulos como espacios de nombres
################################################################################

# Los módulos también pueden usarse como simples contenedores de variables

# Ejemplo (normalmente en un archivo separado):
"""
# configuracion.py

# Configuración de la base de datos
DB_HOST = "localhost"
DB_PORT = 5432
DB_USER = "usuario"
DB_PASSWORD = "contraseña"
DB_NAME = "mi_base_de_datos"

# Configuración de la aplicación
APP_NAME = "Mi Aplicación"
APP_VERSION = "1.0.0"
DEBUG_MODE = True
"""

# Uso:
"""
import configuracion

print(f"Conectando a {configuracion.DB_HOST}:{configuracion.DB_PORT}")
print(f"Aplicación: {configuracion.APP_NAME} v{configuracion.APP_VERSION}")
"""

################################################################################
## Conclusión
################################################################################

# Los módulos son fundamentales en Python para:
# - Organizar código en unidades lógicas
# - Reutilizar código en diferentes programas
# - Evitar conflictos de nombres
# - Distribuir funcionalidades

# La biblioteca estándar de Python ofrece una amplia gama de módulos
# que cubren desde matemáticas hasta redes y procesamiento de texto

# Crear módulos propios es sencillo y permite estructurar mejor los proyectos