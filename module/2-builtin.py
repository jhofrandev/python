"""
  Módulos Incorporados de Python - Exploración Avanzada
  
  Este módulo cubre funcionalidades clave de la biblioteca estándar de Python.
"""

################################################################################
## Módulo argparse - Creación de interfaces de línea de comandos
################################################################################
import argparse

# Ejemplo básico de parser
parser = argparse.ArgumentParser(description='Ejemplo de argparse')
parser.add_argument('-v', '--verbose', action='store_true', help='Modo verbose')
parser.add_argument('archivo', type=str, help='Archivo a procesar')
args = parser.parse_args()

print(f"Archivo seleccionado: {args.archivo}")
print(f"Modo verbose: {args.verbose}")

################################################################################
## Módulo logging - Sistema de registro avanzado
################################################################################
import logging

# Configurar logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info('Este es un mensaje informativo')
logger.warning('Este es un mensaje de advertencia')

################################################################################
## Módulo subprocess - Ejecución de comandos del sistema
################################################################################
import subprocess

# Ejecutar comando y capturar salida
resultado = subprocess.run(
    ['echo', 'Hola desde subprocess'], 
    capture_output=True, 
    text=True, 
    shell=True
)
print(f"Salida del comando: {resultado.stdout}")

################################################################################
## Módulo multiprocessing - Programación paralela
################################################################################
import multiprocessing
import time

def worker(num):
    print(f'Worker {num} iniciado')
    time.sleep(2)
    print(f'Worker {num} finalizado')

if __name__ == '__main__':
    procesos = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        procesos.append(p)
        p.start()
    
    for p in procesos:
        p.join()

################################################################################
## Módulo asyncio - Programación asíncrona
################################################################################
import asyncio

async def tarea_asincrona(num):
    print(f'Tarea {num} iniciada')
    await asyncio.sleep(1)
    print(f'Tarea {num} completada')

async def main():
    await asyncio.gather(
        tarea_asincrona(1),
        tarea_asincrona(2),
        tarea_asincrona(3)
    )

asyncio.run(main())

################################################################################
## Módulo unittest - Pruebas unitarias
################################################################################
import unittest

def suma(a, b):
    return a + b

class TestSuma(unittest.TestCase):
    def test_suma_positivos(self):
        self.assertEqual(suma(3, 5), 8)
    
    def test_suma_negativos(self):
        self.assertEqual(suma(-2, -3), -5)

if __name__ == '__main__':
    unittest.main()

################################################################################
## Módulo pathlib - Manejo moderno de rutas
################################################################################
from pathlib import Path

# Crear ruta
ruta = Path('ejemplo/directorio')
ruta.mkdir(parents=True, exist_ok=True)

# Crear archivo
archivo = ruta / 'test.txt'
archivo.write_text('Hola desde pathlib!')

# Leer archivo
print(f"Contenido del archivo: {archivo.read_text()}")

################################################################################
## Módulo secrets - Generación segura de tokens
################################################################################
import secrets

# Generar token seguro
token = secrets.token_urlsafe(16)
print(f"Token seguro: {token}")

# Comparación segura de cadenas
segura = secrets.compare_digest("miclave", "miclave")
print(f"Comparación segura: {segura}")

################################################################################
## Módulo statistics - Cálculos estadísticos
################################################################################
import statistics

datos = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(f"Media: {statistics.mean(datos)}")
print(f"Mediana: {statistics.median(datos)}")
print(f"Desviación estándar: {statistics.stdev(datos)}")

################################################################################
## Módulo zipfile - Manipulación de archivos ZIP
################################################################################
import zipfile

# Crear archivo ZIP
with zipfile.ZipFile('archivos.zip', 'w') as zipf:
    zipf.write('ejemplo.txt')
    
# Listar contenido ZIP
with zipfile.ZipFile('archivos.zip') as zipf:
    print(f"Archivos en ZIP: {zipf.namelist()}")

################################################################################
## Módulo sqlite3 - Bases de datos embebidas
################################################################################
import sqlite3

# Crear y conectar a base de datos
conn = sqlite3.connect('ejemplo.db')
c = conn.cursor()

# Crear tabla
c.execute('''CREATE TABLE IF NOT EXISTS usuarios
             (id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER)''')

# Insertar datos
c.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ('Ana', 30))
conn.commit()

# Consultar datos
c.execute("SELECT * FROM usuarios")
print(f"Usuarios: {c.fetchall()}")

conn.close()