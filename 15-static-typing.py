'''
En Python, el static typing (tipado estático) se refiere a la capacidad de definir explícitamente los tipos de datos de variables, parámetros de funciones y valores de retorno, aunque Python sea un lenguaje de tipado dinámico por defecto. Esto se logra mediante anotaciones de tipo (type hints), introducidas en PEP 484 (Python 3.5+). Estas anotaciones no afectan el funcionamiento del código en tiempo de ejecución, pero permiten a herramientas externas realizar verificación estática de tipos para detectar errores antes de ejecutar el código.
'''

################################################################################## Características Clave
################################################################################

# 1. Anotaciones de Tipo:
## Se usan para indicar el tipo esperado de una variable, parámetro o retorno.
def suma(a: int, b: int) -> int:
    return a + b

# 2. Herramientas de Verificación:
## Mypy: Es la herramienta más popular para verificar tipos estáticamente.
## Pyright (Microsoft), Pyre (Facebook): Alternativas.

# 3. Tipos Complejos:
## Se utiliza el módulo typing para estructuras como listas, diccionarios, uniones, etc.
from typing import List, Dict, Union

def procesar_datos(data: List[Dict[str, Union[int, str]]]) -> None:
    # Código aquí
    pass


################################################################################## Ejemplo Práctico
################################################################################

# Definición con anotaciones de tipo
def saludar(nombre: str) -> str:
    return f"Hola, {nombre}"

# Variable con anotación de tipo
edad: int = 25

# Uso incorrecto (detectado por Mypy)
saludar(42)  # Error: se espera un 'str', no un 'int'


################################################################################## Static Typing vs Dynamic Typing
################################################################################

# Static Typing:
## Los tipos se verifican antes de la ejecución (con herramientas como Mypy).
## Mejora la legibilidad y el mantenimiento del código.

# Dynamic Typing:
## Los tipos se verifican en tiempo de ejecución (comportamiento natural de Python).
## Flexible pero propenso a errores sutiles.


################################################################################## Ventajas
################################################################################

# Detección temprana de errores: Atrapa inconsistencias de tipos antes de ejecutar.

# Documentación automática: Las anotaciones sirven como documentación explícita.

# Compatibilidad con IDEs: Mejora el autocompletado y las sugerencias en editores como VS Code o PyCharm.