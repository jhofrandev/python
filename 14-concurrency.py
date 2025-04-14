'''
La concurrency (concurrencia) en Python se refiere a la capacidad de un programa para realizar múltiples tareas de manera simultánea o intercalada, mejorando la eficiencia y el rendimiento, especialmente en operaciones de entrada/salida (I/O) o tareas que no dependen de la CPU.

Principales enfoques de concurrencia en Python:
'''


################################################################################## 
# 1. Multithreading:
################################################################################

'''
Usa múltiples hilos (threads) dentro de un proceso.
Ideal para tareas I/O intensivas (como leer/escribir archivos o realizar solicitudes de red).
Limitado por el Global Interpreter Lock (GIL), lo que significa que solo un hilo puede ejecutar código Python a la vez en un intérprete, lo que lo hace menos eficiente para tareas intensivas en CPU.
'''

import threading

def tarea():
    print("Ejecutando tarea en un hilo")

hilo = threading.Thread(target=tarea)
hilo.start()
hilo.join()

################################################################################## 
# 2. Multiprocessing:
################################################################################

'''
- Usa múltiples procesos en lugar de hilos.
- Cada proceso tiene su propio intérprete Python, evitando el GIL.
- Ideal para tareas intensivas en CPU, como cálculos matemáticos complejos.
'''

from multiprocessing import Process

def tarea():
    print("Ejecutando tarea en un proceso")

proceso = Process(target=tarea)
proceso.start()
proceso.join()

################################################################################## 3. Asyncio (Programación Asíncrona):
################################################################################

'''
- Usa un solo hilo y un bucle de eventos para manejar tareas concurrentes.
- Ideal para tareas I/O intensivas que pueden esperar (como solicitudes HTTP o acceso a bases de datos).
- No está limitado por el GIL porque no usa múltiples hilos.
'''

import asyncio

async def tarea():
    print("Iniciando tarea")
    await asyncio.sleep(1)
    print("Tarea completada")

asyncio.run(tarea())

################################################################################## 4. Bibliotecas de concurrencia avanzadas:
################################################################################

'''
- Concurrent.futures: Proporciona una abstracción de alto nivel para trabajar con hilos o procesos.
- ThreadPoolExecutor y ProcessPoolExecutor permiten ejecutar tareas concurrentes fácilmente
'''

from concurrent.futures import ThreadPoolExecutor

def tarea(nombre):
    print(f"Tarea {nombre} ejecutada")

with ThreadPoolExecutor() as executor:
    executor.submit(tarea, "1")
    executor.submit(tarea, "2")

'''
Diferencia entre concurrencia y paralelismo:

- Concurrencia: Múltiples tareas progresan de manera intercalada (pueden no ejecutarse al mismo tiempo).
- Paralelismo: Múltiples tareas se ejecutan exactamente al mismo tiempo en diferentes núcleos de CPU.

En Python, la concurrencia es útil para mejorar la eficiencia en tareas I/O, mientras que el paralelismo es más adecuado para tareas intensivas en CPU.
'''