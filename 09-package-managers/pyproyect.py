'''
El archivo pyproject.toml es un archivo de configuración moderno para proyectos Python que se ha convertido en el estándar actual para gestionar la configuración de proyectos.
'''

################################################################################## ¿Qué es pyproject.toml?
################################################################################

'''
Es un archivo en formato TOML (Tom's Obvious, Minimal Language) que fue introducido en la PEP 518 y ampliado en la PEP 621. Este archivo reemplaza o complementa los archivos tradicionales como setup.py y proporciona una forma estandarizada para especificar:

1. Metadatos del proyecto (nombre, versión, dependencias)
2. Requisitos del sistema de construcción
3. Configuraciones de herramientas (linters, formateadores, herramientas de prueba)
'''

################################################################################## Usos principales
################################################################################

'''
- Metadatos del proyecto : Reemplaza a setup.py para información del paquete
- Gestión de dependencias : Especifica las dependencias del proyecto
- Configuración del sistema de construcción : Define cómo debe construirse el paquete
- Configuración de herramientas : Centraliza configuraciones para varias herramientas
'''


################################################################################## Ejemplo de estructura
################################################################################

[project]
name = "regex-utils"
version = "0.1.0"
description = "Utilidades para expresiones regulares en Python"
authors = [
    # {name = "Tu Nombre", email = "tu.email@ejemplo.com"},
]
readme = "README.md"
# requires-python = ">=3.8"
# license = {text = "MIT"}

dependencies = [
    "requests>=2.25.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=6.0.0",
    "black>=21.0",
    "flake8>=3.9.0",
]

[build-system]
requires = ["setuptools>=42", "wheel"]
# build-backend = "setuptools.build_meta"

[tool.black]
# line-length = 88
# target-version = ['py38']

[tool.pytest.ini_options]
minversion = "6.0"
addopts = "--verbose"
testpaths = ["tests"]

################################################################################## ¿Por qué usar pyproject.toml?
################################################################################

'''
- Estandarización : Proporciona un formato de configuración unificado
- Independencia de herramientas : Funciona con pip, poetry, flit y otras herramientas
- Fuente única de verdad : Toda la configuración del proyecto en un solo lugar
- Mejor gestión de dependencias : Clara separación entre dependencias de construcción y de ejecución
- Soporte para herramientas modernas : Requerido por herramientas más nuevas como black, pytest, mypy
'''