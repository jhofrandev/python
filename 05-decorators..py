################################################################################
# Decoradores en Python
################################################################################

'''
Los decoradores son una característica avanzada de Python que permite modificar
el comportamiento de funciones o clases sin cambiar su código interno.

Un decorador es una función que toma otra función como entrada, añade alguna
funcionalidad y devuelve una nueva función.

Sintaxis básica:
    @nombre_decorador
    def funcion_a_decorar():
        pass

Esto es equivalente a:
    def funcion_a_decorar():
        pass
    funcion_a_decorar = nombre_decorador(funcion_a_decorar)
'''

################################################################################
# Decoradores Básicos
################################################################################

# Ejemplo 1: Un decorador simple
def mi_decorador(funcion):
    def wrapper():
        print("Algo se ejecuta antes de la función")
        funcion()
        print("Algo se ejecuta después de la función")
    return wrapper

# Usando el decorador con la sintaxis @
@mi_decorador
def saludar():
    print("¡Hola, mundo!")

# Llamando a la función decorada
print("\nEjemplo 1: Decorador simple")
saludar()

# Ejemplo 2: Decorador con argumentos para la función
def decorador_con_args(funcion):
    def wrapper(*args, **kwargs):
        print(f"Argumentos recibidos: {args}, {kwargs}")
        resultado = funcion(*args, **kwargs)
        print(f"La función retornó: {resultado}")
        return resultado
    return wrapper

@decorador_con_args
def suma(a, b):
    return a + b

print("\nEjemplo 2: Decorador con argumentos")
resultado = suma(5, 3)
print(f"Resultado final: {resultado}")

################################################################################
# Decoradores con Parámetros
################################################################################

# Decorador que acepta parámetros propios
def repetir(n):
    def decorador_repetir(funcion):
        def wrapper(*args, **kwargs):
            resultado = None
            for _ in range(n):
                resultado = funcion(*args, **kwargs)
            return resultado
        return wrapper
    return decorador_repetir

@repetir(3)
def mensaje(texto):
    print(texto)
    return len(texto)

print("\nEjemplo 3: Decorador con parámetros")
longitud = mensaje("Este mensaje se repetirá")
print(f"Longitud del mensaje: {longitud}")

################################################################################
# Decoradores Múltiples
################################################################################

# Se pueden aplicar varios decoradores a una misma función
def negrita(funcion):
    def wrapper(*args, **kwargs):
        return f"<b>{funcion(*args, **kwargs)}</b>"
    return wrapper

def italica(funcion):
    def wrapper(*args, **kwargs):
        return f"<i>{funcion(*args, **kwargs)}</i>"
    return wrapper

@negrita
@italica
def formatear_texto(texto):
    return texto

print("\nEjemplo 4: Decoradores múltiples")
texto_formateado = formatear_texto("Texto con formato")
print(f"Resultado: {texto_formateado}")
# El orden de aplicación es de abajo hacia arriba: primero italica, luego negrita

################################################################################
# Preservando Metadatos
################################################################################

# Los decoradores pueden ocultar información importante de la función original
import functools

def decorador_sin_wraps(funcion):
    def wrapper(*args, **kwargs):
        """Documentación del wrapper"""
        return funcion(*args, **kwargs)
    return wrapper

def decorador_con_wraps(funcion):
    @functools.wraps(funcion)  # Preserva metadatos de la función original
    def wrapper(*args, **kwargs):
        """Documentación del wrapper"""
        return funcion(*args, **kwargs)
    return wrapper

@decorador_sin_wraps
def funcion1():
    """Documentación de funcion1"""
    pass

@decorador_con_wraps
def funcion2():
    """Documentación de funcion2"""
    pass

print("\nEjemplo 5: Preservando metadatos")
print(f"Nombre de funcion1: {funcion1.__name__}")
print(f"Documentación de funcion1: {funcion1.__doc__}")
print(f"Nombre de funcion2: {funcion2.__name__}")
print(f"Documentación de funcion2: {funcion2.__doc__}")

################################################################################
# Aplicaciones Prácticas
################################################################################

# 1. Medición de tiempo de ejecución
import time

def medir_tiempo(funcion):
    @functools.wraps(funcion)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f"La función {funcion.__name__} tardó {fin - inicio:.6f} segundos en ejecutarse")
        return resultado
    return wrapper

@medir_tiempo
def operacion_lenta():
    """Simula una operación que toma tiempo"""
    time.sleep(1)
    return "Operación completada"

print("\nEjemplo 6: Medición de tiempo")
operacion_lenta()

# 2. Validación de argumentos
def validar_tipos(*tipos):
    def decorador(funcion):
        @functools.wraps(funcion)
        def wrapper(*args, **kwargs):
            # Verificar que el número de argumentos coincide con el número de tipos
            if len(args) != len(tipos):
                raise ValueError(f"Se esperaban {len(tipos)} argumentos, pero se recibieron {len(args)}")
            
            # Verificar que cada argumento es del tipo correcto
            for i, (arg, tipo) in enumerate(zip(args, tipos)):
                if not isinstance(arg, tipo):
                    raise TypeError(f"El argumento {i+1} debe ser de tipo {tipo.__name__}")
            
            return funcion(*args, **kwargs)
        return wrapper
    return decorador

@validar_tipos(int, int)
def dividir(a, b):
    """Divide dos números enteros"""
    return a / b

print("\nEjemplo 7: Validación de argumentos")
try:
    print(f"10 / 2 = {dividir(10, 2)}")
    print(f"10 / '2' = {dividir(10, '2')}")  # Esto debería fallar
except TypeError as e:
    print(f"Error: {e}")

# 3. Caché de resultados (memoización)
def memoizar(funcion):
    """Almacena en caché los resultados de una función para evitar cálculos repetidos"""
    cache = {}
    
    @functools.wraps(funcion)
    def wrapper(*args):
        if args in cache:
            print(f"Usando valor en caché para {args}")
            return cache[args]
        
        resultado = funcion(*args)
        cache[args] = resultado
        return resultado
    
    return wrapper

@memoizar
def fibonacci(n):
    """Calcula el n-ésimo número de Fibonacci (implementación ineficiente a propósito)"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("\nEjemplo 8: Memoización")
print(f"fibonacci(10) = {fibonacci(10)}")
print(f"fibonacci(10) de nuevo = {fibonacci(10)}")  # Debería usar el valor en caché

################################################################################
# Decoradores de Clases
################################################################################

# Los decoradores también pueden aplicarse a clases
def agregar_metodo(clase):
    def metodo_nuevo(self):
        return "Este es un método añadido por el decorador"
    
    clase.metodo_nuevo = metodo_nuevo
    return clase

@agregar_metodo
class MiClase:
    def __init__(self, valor):
        self.valor = valor
    
    def metodo_original(self):
        return f"Valor original: {self.valor}"

print("\nEjemplo 9: Decoradores de clases")
obj = MiClase(42)
print(obj.metodo_original())
print(obj.metodo_nuevo())

################################################################################
# Decoradores Integrados en Python
################################################################################

# Python incluye varios decoradores útiles

# @property - Convierte un método en un atributo de solo lectura
class Temperatura:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("La temperatura no puede ser menor que el cero absoluto")
        self._celsius = valor
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, valor):
        self.celsius = (valor - 32) * 5/9

print("\nEjemplo 10: Decorador @property")
temp = Temperatura(25)
print(f"Temperatura en Celsius: {temp.celsius}°C")
print(f"Temperatura en Fahrenheit: {temp.fahrenheit}°F")

temp.celsius = 30
print(f"Nueva temperatura en Celsius: {temp.celsius}°C")
print(f"Nueva temperatura en Fahrenheit: {temp.fahrenheit}°F")

temp.fahrenheit = 68
print(f"Temperatura en Celsius después de cambiar Fahrenheit: {temp.celsius}°C")

try:
    temp.celsius = -300  # Debería fallar
except ValueError as e:
    print(f"Error: {e}")

# @classmethod y @staticmethod
class Calculadora:
    valor_default = 10
    
    def __init__(self, valor):
        self.valor = valor
    
    def sumar(self, x):
        return self.valor + x
    
    @classmethod
    def desde_string(cls, valor_str):
        """Crea una instancia a partir de una cadena"""
        return cls(int(valor_str))
    
    @staticmethod
    def es_par(numero):
        """Verifica si un número es par"""
        return numero % 2 == 0

print("\nEjemplo 11: @classmethod y @staticmethod")
calc = Calculadora(5)
print(f"5 + 3 = {calc.sumar(3)}")

# Usando classmethod para crear una instancia de forma alternativa
calc2 = Calculadora.desde_string("15")
print(f"15 + 3 = {calc2.sumar(3)}")

# Usando staticmethod (no necesita una instancia)
print(f"¿10 es par? {Calculadora.es_par(10)}")
print(f"¿15 es par? {Calculadora.es_par(15)}")

################################################################################
# Conclusiones
################################################################################

'''
Los decoradores son una característica poderosa de Python que permite:

1. Modificar el comportamiento de funciones y clases sin cambiar su código interno
2. Aplicar aspectos transversales como logging, medición de tiempo, validación, etc.
3. Implementar patrones de diseño como Singleton, Factory, etc.
4. Crear APIs más limpias y expresivas

Buenas prácticas:
- Usar @functools.wraps para preservar metadatos
- Mantener los decoradores simples y enfocados en una sola responsabilidad
- Documentar claramente lo que hace el decorador
- Considerar el impacto en el rendimiento, especialmente para funciones que se llaman frecuentemente

Los decoradores son una herramienta fundamental para la programación avanzada en Python
y son ampliamente utilizados en frameworks como Flask, Django, FastAPI, etc.
'''