################################################################################
# Administradores de Contexto en Python
################################################################################


'''
Los administradores de contexto son una característica de Python que permite
gestionar recursos de manera eficiente, asegurando que se inicialicen y liberen
correctamente, incluso si ocurren excepciones durante su uso.

Se implementan mediante la sentencia 'with' y son especialmente útiles para:
- Manejo de archivos
- Conexiones a bases de datos
- Bloqueos y semáforos
- Medición de tiempo
- Redirección de salida
- Y muchos otros escenarios donde se requiere configuración y limpieza
'''

################################################################################
# Uso Básico: Manejo de Archivos
################################################################################

# Ejemplo 1: Manejo de archivos con 'with'
print("Ejemplo 1: Manejo de archivos con 'with'")

# Método tradicional (propenso a errores si olvidamos cerrar el archivo)
print("Método tradicional:")
try:
    archivo = open('ejemplo.txt', 'w')
    archivo.write('Hola, mundo!')
finally:
    archivo.close()
    print("Archivo cerrado manualmente")

# Usando administrador de contexto
print("\nUsando administrador de contexto:")
with open('ejemplo.txt', 'w') as archivo:
    archivo.write('Hola, mundo con with!')
print("Archivo cerrado automáticamente")

# Lectura del archivo
with open('ejemplo.txt', 'r') as archivo:
    contenido = archivo.read()
    print(f"Contenido: {contenido}")

################################################################################
# Creando Administradores de Contexto Personalizados
################################################################################

# Ejemplo 2: Clase con métodos __enter__ y __exit__
print("\nEjemplo 2: Clase con métodos __enter__ y __exit__")

class MiContexto:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def __enter__(self):
        print(f"Entrando al contexto {self.nombre}")
        return self  # El objeto devuelto se asigna a la variable después de 'as'
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Saliendo del contexto {self.nombre}")
        # Si devuelve True, suprime cualquier excepción que ocurra
        # Si devuelve False o None, la excepción se propaga
        if exc_type is not None:
            print(f"Ocurrió una excepción: {exc_type}, {exc_val}")
            return False  # Propagar la excepción
        return True

# Uso normal
with MiContexto("ejemplo") as ctx:
    print(f"Dentro del contexto: {ctx.nombre}")

# Con excepción
try:
    with MiContexto("con error") as ctx:
        print("Vamos a generar un error...")
        raise ValueError("¡Error de prueba!")
except ValueError as e:
    print(f"Excepción capturada fuera del contexto: {e}")

################################################################################
# Administradores de Contexto con Decoradores
################################################################################

# Ejemplo 3: Usando el decorador contextmanager
print("\nEjemplo 3: Usando el decorador contextmanager")
from contextlib import contextmanager

@contextmanager
def mi_contexto_simple(nombre):
    print(f"Entrando al contexto {nombre}")
    try:
        # El yield separa el código de inicialización del de limpieza
        yield nombre  # Este valor se asigna a la variable después de 'as'
    except Exception as e:
        print(f"Excepción dentro del contexto: {e}")
        raise  # Re-lanzar la excepción
    finally:
        print(f"Saliendo del contexto {nombre}")

# Uso normal
with mi_contexto_simple("simple") as nombre:
    print(f"Dentro del contexto: {nombre}")

# Con excepción
try:
    with mi_contexto_simple("simple con error"):
        print("Vamos a generar otro error...")
        raise RuntimeError("¡Error en contexto simple!")
except RuntimeError as e:
    print(f"Excepción capturada: {e}")

################################################################################
# Casos de Uso Prácticos
################################################################################

# Ejemplo 4: Medición de tiempo
print("\nEjemplo 4: Medición de tiempo")
import time

@contextmanager
def medir_tiempo(nombre_operacion):
    inicio = time.time()
    try:
        yield
    finally:
        fin = time.time()
        print(f"Tiempo de '{nombre_operacion}': {fin - inicio:.6f} segundos")

# Medir tiempo de una operación
with medir_tiempo("cálculo"):
    # Simulamos una operación que toma tiempo
    time.sleep(0.5)
    resultado = sum(i**2 for i in range(10000))
    print(f"Resultado: {resultado}")

# Ejemplo 5: Redirección de salida
print("\nEjemplo 5: Redirección de salida")
import sys
from io import StringIO

@contextmanager
def capturar_salida():
    salida_original = sys.stdout
    salida_capturada = StringIO()
    sys.stdout = salida_capturada
    try:
        yield salida_capturada
    finally:
        sys.stdout = salida_original

# Capturar la salida de print
with capturar_salida() as salida:
    print("Esta salida será capturada")
    print("Y no se mostrará en la consola")

print(f"Salida capturada: {salida.getvalue()}")

# Ejemplo 6: Gestión de conexiones a bases de datos (simulado)
print("\nEjemplo 6: Gestión de conexiones a bases de datos (simulado)")

class ConexionBD:
    def __init__(self, nombre_bd):
        self.nombre_bd = nombre_bd
        self.conectado = False
        
    def conectar(self):
        print(f"Conectando a la base de datos '{self.nombre_bd}'...")
        self.conectado = True
        
    def desconectar(self):
        print(f"Desconectando de la base de datos '{self.nombre_bd}'...")
        self.conectado = False
        
    def ejecutar_consulta(self, consulta):
        if not self.conectado:
            raise RuntimeError("No hay conexión a la base de datos")
        print(f"Ejecutando: {consulta}")
        return ["resultado1", "resultado2"]  # Simulación de resultados

@contextmanager
def conexion_bd(nombre_bd):
    conexion = ConexionBD(nombre_bd)
    try:
        conexion.conectar()
        yield conexion
    finally:
        conexion.desconectar()

# Uso de la conexión
with conexion_bd("mi_aplicacion") as bd:
    resultados = bd.ejecutar_consulta("SELECT * FROM usuarios")
    print(f"Resultados: {resultados}")

################################################################################
# Administradores de Contexto Anidados
################################################################################

# Ejemplo 7: Contextos anidados
print("\nEjemplo 7: Contextos anidados")

@contextmanager
def nivel(numero):
    print(f"Entrando al nivel {numero}")
    try:
        yield numero
    finally:
        print(f"Saliendo del nivel {numero}")

# Anidamiento explícito
with nivel(1) as n1:
    print(f"En nivel {n1}")
    with nivel(2) as n2:
        print(f"En nivel {n2}")
        with nivel(3) as n3:
            print(f"En nivel {n3}")

# Anidamiento en una línea
print("\nAnidamiento en una línea:")
with nivel(1) as n1, nivel(2) as n2, nivel(3) as n3:
    print(f"En niveles {n1}, {n2} y {n3} simultáneamente")

################################################################################
# Administradores de Contexto de la Biblioteca Estándar
################################################################################

# Ejemplo 8: Otros administradores de contexto útiles
print("\nEjemplo 8: Otros administradores de contexto útiles")

# contextlib.suppress - Suprime excepciones específicas
from contextlib import suppress

print("suppress:")
with suppress(ZeroDivisionError):
    print("Intentando división por cero...")
    resultado = 1 / 0
    print("Este código no se ejecutará")
print("Continuamos después de la excepción suprimida")

# contextlib.redirect_stdout - Redirige la salida estándar
from contextlib import redirect_stdout

print("\nredirect_stdout:")
with open('salida.txt', 'w') as archivo:
    with redirect_stdout(archivo):
        print("Esta salida va al archivo")
    print("Esta salida va a la consola")

with open('salida.txt', 'r') as archivo:
    print(f"Contenido del archivo: {archivo.read()}")

# contextlib.ExitStack - Gestiona múltiples contextos dinámicamente
from contextlib import ExitStack

print("\nExitStack:")
with ExitStack() as stack:
    # Podemos añadir contextos dinámicamente
    archivos = [
        stack.enter_context(open(f'archivo{i}.txt', 'w'))
        for i in range(1, 4)
    ]
    
    for i, archivo in enumerate(archivos, 1):
        archivo.write(f"Contenido del archivo {i}")
    
    print(f"Abiertos {len(archivos)} archivos simultáneamente")
# Todos los archivos se cierran automáticamente al salir del contexto

# Leer los archivos creados
for i in range(1, 4):
    with open(f'archivo{i}.txt', 'r') as archivo:
        print(f"archivo{i}.txt: {archivo.read()}")

################################################################################
# Patrones Avanzados
################################################################################

# Ejemplo 9: Administrador de contexto reentrante
print("\nEjemplo 9: Administrador de contexto reentrante")

class Recurso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.en_uso = False
        
    def __enter__(self):
        if self.en_uso:
            print(f"Recurso '{self.nombre}' ya está en uso (reentrante)")
        else:
            print(f"Adquiriendo recurso '{self.nombre}'")
            self.en_uso = True
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.en_uso:
            print(f"Advertencia: Intentando liberar recurso '{self.nombre}' que no está en uso")
        else:
            print(f"Liberando recurso '{self.nombre}'")
            self.en_uso = False
        return False

# Crear un recurso compartido
recurso_compartido = Recurso("compartido")

# Uso reentrante
with recurso_compartido as r1:
    print(f"Usando recurso: {r1.nombre}")
    with recurso_compartido as r2:
        print(f"Usando recurso nuevamente: {r2.nombre}")
    print("Saliendo del contexto interno")
print("Saliendo del contexto externo")

# Ejemplo 10: Administrador de contexto asíncrono (Python 3.7+)
print("\nEjemplo 10: Administrador de contexto asíncrono")
import asyncio

class ContextoAsincrono:
    def __init__(self, nombre):
        self.nombre = nombre
        
    async def __aenter__(self):
        print(f"Entrando al contexto asíncrono '{self.nombre}'")
        await asyncio.sleep(0.1)  # Simulamos una operación asíncrona
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"Saliendo del contexto asíncrono '{self.nombre}'")
        await asyncio.sleep(0.1)  # Simulamos una operación asíncrona
        return False

async def ejemplo_asincrono():
    async with ContextoAsincrono("asinc") as ctx:
        print(f"Dentro del contexto asíncrono: {ctx.nombre}")
        await asyncio.sleep(0.2)

# Ejecutar la función asíncrona
asyncio.run(ejemplo_asincrono())

################################################################################
# Buenas Prácticas
################################################################################

'''
1. Usa administradores de contexto para gestionar recursos que necesitan
   inicialización y limpieza, como archivos, conexiones, bloqueos, etc.

2. Implementa __enter__ y __exit__ en tus clases cuando necesiten gestionar
   recursos, o usa el decorador @contextmanager para funciones.

3. Asegúrate de que el método __exit__ maneje correctamente las excepciones:
   - Devuelve True si quieres suprimir la excepción
   - Devuelve False o None si quieres que la excepción se propague

4. Usa administradores de contexto anidados cuando necesites gestionar
   múltiples recursos.

5. Considera usar los administradores de contexto de la biblioteca estándar
   como suppress, redirect_stdout, y ExitStack.

6. Para operaciones asíncronas, usa administradores de contexto asíncronos
   con async with.
'''

################################################################################
# Ejercicios Prácticos
################################################################################

# Ejercicio 1: Implementar un administrador de contexto para un temporizador
print("\nEjercicio 1: Temporizador como administrador de contexto")

class Temporizador:
    def __enter__(self):
        self.inicio = time.time()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fin = time.time()
        self.duracion = self.fin - self.inicio
        print(f"Tiempo transcurrido: {self.duracion:.6f} segundos")
        return False  # No suprimimos excepciones

# Uso del temporizador
with Temporizador():
    # Simulamos una operación que toma tiempo
    time.sleep(0.3)
    print("Operación completada")

# Ejercicio 2: Administrador de contexto para cambiar directorio temporalmente
print("\nEjercicio 2: Cambio temporal de directorio")
import os

@contextmanager
def cambiar_directorio(ruta):
    directorio_original = os.getcwd()
    try:
        os.chdir(ruta)
        print(f"Cambiado al directorio: {os.getcwd()}")
        yield
    finally:
        os.chdir(directorio_original)
        print(f"Volviendo al directorio original: {os.getcwd()}")

# Uso del cambio de directorio
with cambiar_directorio(".."):
    print(f"Directorio actual: {os.getcwd()}")
    # Hacer operaciones en el directorio temporal
print(f"Directorio después del contexto: {os.getcwd()}")

################################################################################
# Conclusiones
################################################################################

'''
Los administradores de contexto son una característica poderosa de Python que:

1. Simplifican la gestión de recursos, asegurando su correcta inicialización
   y liberación.

2. Mejoran la legibilidad del código al encapsular patrones de uso de recursos.

3. Aumentan la robustez del código al garantizar la limpieza incluso cuando
   ocurren excepciones.

4. Permiten implementar patrones complejos como la gestión de transacciones,
   bloqueos, y cambios temporales de estado.

5. Se integran perfectamente con el modelo de excepciones de Python.

Los administradores de contexto, junto con las expresiones generadoras y las
transformaciones de datos en pipeline, forman parte de las herramientas que
hacen que Python sea un lenguaje elegante y expresivo para una amplia variedad
de tareas de programación.
'''

# Limpieza de archivos creados durante la ejecución
import os
for archivo in ['ejemplo.txt', 'salida.txt', 'archivo1.txt', 'archivo2.txt', 'archivo3.txt']:
    if os.path.exists(archivo):
        os.remove(archivo)