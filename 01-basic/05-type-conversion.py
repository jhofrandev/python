"""
  La conversión de tipos (type casting) en Python permite cambiar un tipo de dato a otro.
  Es fundamental para manejar diferentes tipos de datos y realizar operaciones entre ellos.
"""

################################################################################
## Conversión de tipos básicos
################################################################################

# Python permite convertir entre tipos de datos básicos usando funciones constructoras

# Conversión a entero (int)
print("Conversión a entero:")
print(int(5.7))       # 5 (trunca el decimal)
print(int("10"))      # 10
print(int(True))      # 1
print(int(False))     # 0
# print(int("Hola"))  # Error: no se puede convertir texto no numérico a entero

# Conversión a flotante (float)
print("\nConversión a flotante:")
print(float(5))       # 5.0
print(float("10.5"))  # 10.5
print(float("-3.14")) # -3.14
print(float(True))    # 1.0
print(float(False))   # 0.0

# Conversión a cadena (str)
print("\nConversión a cadena:")
print(str(5))         # "5"
print(str(3.14))      # "3.14"
print(str(True))      # "True"
print(str([1, 2, 3])) # "[1, 2, 3]"

# Conversión a booleano (bool)
print("\nConversión a booleano:")
print(bool(1))        # True
print(bool(0))        # False
print(bool(0.0))      # False
print(bool(""))       # False (cadena vacía)
print(bool("Hola"))   # True (cadena no vacía)
print(bool([]))       # False (lista vacía)
print(bool([1, 2]))   # True (lista no vacía)

################################################################################
## Conversión entre colecciones
################################################################################

# Conversión a lista
print("\nConversión a lista:")
print(list("Python"))         # ['P', 'y', 't', 'h', 'o', 'n']
print(list((1, 2, 3)))        # [1, 2, 3] (de tupla a lista)
print(list({1, 2, 3}))        # [1, 2, 3] (de conjunto a lista)
print(list({"a": 1, "b": 2})) # ['a', 'b'] (de diccionario a lista de claves)

# Conversión a tupla
print("\nConversión a tupla:")
print(tuple([1, 2, 3]))       # (1, 2, 3) (de lista a tupla)
print(tuple("Python"))        # ('P', 'y', 't', 'h', 'o', 'n')
print(tuple({1, 2, 3}))       # (1, 2, 3) (de conjunto a tupla)

# Conversión a conjunto (elimina duplicados)
print("\nConversión a conjunto:")
print(set([1, 2, 2, 3, 3]))   # {1, 2, 3} (elimina duplicados)
print(set("Mississippi"))     # {'M', 'i', 's', 'p'} (caracteres únicos)
print(set((1, 2, 2, 3)))      # {1, 2, 3} (de tupla a conjunto)

# Conversión a diccionario
print("\nConversión a diccionario:")
# A partir de una lista de tuplas (clave, valor)
print(dict([("a", 1), ("b", 2)]))  # {'a': 1, 'b': 2}
# A partir de dos listas usando zip
claves = ["nombre", "edad", "ciudad"]
valores = ["Ana", 25, "Madrid"]
print(dict(zip(claves, valores)))  # {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Madrid'}

################################################################################
## Conversión implícita
################################################################################

# Python realiza algunas conversiones automáticamente

print("\nConversión implícita:")
# Entero a flotante en operaciones mixtas
print(5 + 3.14)  # 8.14 (el entero 5 se convierte implícitamente a 5.0)

# Concatenación de cadenas
print("Edad: " + str(25))  # Necesita conversión explícita

################################################################################
## Funciones útiles para conversión y verificación
################################################################################

# isinstance(): Verifica si un objeto es de un tipo específico
print("\nVerificación de tipos con isinstance():")
print(isinstance(5, int))       # True
print(isinstance("Hola", str))  # True
print(isinstance(3.14, float))  # True
print(isinstance(5, (int, float)))  # True (es alguno de los tipos listados)

# type(): Devuelve el tipo de un objeto
print("\nObteniendo el tipo con type():")
print(type(5))        # <class 'int'>
print(type("Hola"))   # <class 'str'>
print(type([1, 2]))   # <class 'list'>

################################################################################
## Conversiones numéricas especiales
################################################################################

# Conversión entre sistemas numéricos
print("\nConversión entre sistemas numéricos:")
# Decimal a binario, octal, hexadecimal
print(bin(10))        # '0b1010' (binario)
print(oct(10))        # '0o12' (octal)
print(hex(10))        # '0xa' (hexadecimal)

# Binario, octal, hexadecimal a decimal
print(int('1010', 2))  # 10 (binario a decimal)
print(int('12', 8))    # 10 (octal a decimal)
print(int('a', 16))    # 10 (hexadecimal a decimal)

################################################################################
## Manejo de errores en conversiones
################################################################################

print("\nManejo de errores en conversiones:")
# Usando try-except para manejar errores de conversión
try:
    num = int("abc")
except ValueError as e:
    print(f"Error de conversión: {e}")

# Validación previa
texto = "123"
if texto.isdigit():
    num = int(texto)
    print(f"Conversión exitosa: {num}")

################################################################################
## Buenas prácticas
################################################################################

# 1. Siempre verifica que la conversión sea posible antes de intentarla
# 2. Usa try-except para manejar posibles errores de conversión
# 3. Considera el comportamiento de truncamiento al convertir float a int
# 4. Recuerda que bool() considera muchos valores como False (0, "", [], {}, etc.)
# 5. Para conversiones complejas, considera usar bibliotecas especializadas
# 6. Evita confiar en conversiones implícitas para código crítico