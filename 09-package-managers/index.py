'''
# Gestores de Paquetes en Python
Los gestores de paquetes son herramientas que automatizan el proceso de instalación, actualización, configuración y eliminación de paquetes de software. En el contexto de Python, los gestores de paquetes permiten a los desarrolladores instalar y administrar fácilmente bibliotecas y dependencias de terceros.
'''

################################################################################## Principales Gestores de Paquetes en Python
################################################################################

'''
### 1. pip
pip es el gestor de paquetes más utilizado en Python y viene instalado por defecto con las versiones recientes de Python.

Características principales:

- Instalación de paquetes desde PyPI (Python Package Index)
- Gestión de dependencias
- Instalación desde diferentes fuentes (GitHub, archivos locales, etc.)
- Creación de entornos virtuales (con venv )
Comandos básicos:

# Instalar un paquete
pip install nombre_paquete

# Instalar una versión específica
pip install nombre_paquete==1.0.0

# Actualizar un paquete
pip install --upgrade nombre_paquete

# Desinstalar un paquete
pip uninstall nombre_paquete

# Listar paquetes instalados
pip list

# Generar un archivo de requisitos
pip freeze > requirements.txt

# Instalar desde un archivo de requisitos
pip install -r requirements.txt

### 2. conda
conda es un gestor de paquetes y entornos que se utiliza principalmente en ciencia de datos y aprendizaje automático.

Características principales:

- Gestión de paquetes para múltiples lenguajes (no solo Python)
- Gestión de entornos virtuales integrada
- Manejo de dependencias a nivel de sistema operativo
- Distribuciones preconfiguradas como Anaconda y Miniconda
Comandos básicos:

# Crear un entorno
conda create --name mi_entorno python=3.9

# Activar un entorno
conda activate mi_entorno

# Instalar un paquete
conda install nombre_paquete

# Actualizar un paquete
conda update nombre_paquete

# Listar paquetes instalados
conda list

# Exportar entorno
conda env export > environment.yml

# Crear entorno desde archivo
conda env create -f environment.yml

### 3. poetry
poetry es una herramienta moderna para la gestión de dependencias y empaquetado en Python.

Características principales:

- Resolución de dependencias avanzada
- Gestión de entornos virtuales integrada
- Publicación de paquetes simplificada
- Archivo de configuración único (pyproject.toml)
Comandos básicos:

# Iniciar un nuevo proyecto
poetry new mi_proyecto

# Añadir una dependencia
poetry add nombre_paquete

# Instalar dependencias
poetry install

# Actualizar dependencias
poetry update

# Ejecutar un comando en el entorno virtual
poetry run python script.py


## Ventajas de Usar Gestores de Paquetes
1. Reproducibilidad : Permiten especificar exactamente qué versiones de paquetes se necesitan para un proyecto.
2. Aislamiento : Los entornos virtuales evitan conflictos entre dependencias de diferentes proyectos.
3. Automatización : Simplifican la instalación de múltiples paquetes y sus dependencias.
4. Mantenimiento : Facilitan la actualización y eliminación de paquetes.
## Mejores Prácticas
1. Usar entornos virtuales : Siempre trabaja en entornos virtuales para aislar las dependencias de cada proyecto.
2. Especificar versiones : Define versiones específicas o rangos de versiones para evitar problemas de compatibilidad.
3. Documentar dependencias : Mantén archivos como requirements.txt o pyproject.toml actualizados.
4. Revisar licencias : Verifica las licencias de los paquetes que instalas para asegurar compatibilidad con tu proyecto.
Para tu proyecto actual, podrías crear un archivo requirements.txt que liste las dependencias necesarias, lo que facilitaría a otros desarrolladores reproducir tu entorno de desarrollo.
'''