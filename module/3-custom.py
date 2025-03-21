################################################################################
## Módulos Personalizados Avanzados
################################################################################

# Ejemplo: Creación de un módulo de geometría avanzada
"""
Estructura de archivos:
mi_paquete_geometrico/
│   __init__.py
│   geometria.py
│   trigonometria.py
└───utilidades/
    │   __init__.py
    │   calculos.py
"""

# Contenido de geometria.py
class Circulo:
    """Clase para representar un círculo y sus operaciones"""
    def __init__(self, radio):
        self.radio = radio
        
    def area(self):
        return 3.1416 * self.radio ** 2
    
    def perimetro(self):
        return 2 * 3.1416 * self.radio

class Rectangulo:
    """Clase para representar un rectángulo y sus operaciones"""
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)

# Contenido de utilidades/calculos.py
def redondear_valor(valor, decimales=2):
    """Redondea un valor a un número específico de decimales"""
    factor = 10 ** decimales
    return round(valor * factor) / factor

# Contenido de __init__.py principal
__version__ = "1.0.0"
__all__ = ['Circulo', 'Rectangulo']  # Controla qué se exporta con import *

# Uso del módulo personalizado
from mi_paquete_geometrico.geometria import Circulo, Rectangulo
from mi_paquete_geometrico.utilidades.calculos import redondear_valor

circulo = Circulo(5)
print(f"\nÁrea del círculo: {redondear_valor(circulo.area())} m²")

rectangulo = Rectangulo(4, 7)
print(f"Perímetro del rectángulo: {rectangulo.perimetro()} m")

################################################################################
## Buenas Prácticas para Módulos Personalizados
################################################################################

# 1. Documentación completa con docstrings
# 2. Control de imports con __all__
# 3. Manejo de versiones con __version__
# 4. Organización lógica en subpaquetes
# 5. Pruebas unitarias dentro del módulo

# Ejemplo de prueba integrada en el módulo
if __name__ == "__main__":
    # Pruebas rápidas
    test_circulo = Circulo(2)
    assert redondear_valor(test_circulo.area()) == 12.57, "Error en cálculo de área círculo"
    print("\nPruebas pasadas exitosamente!")

################################################################################
## Patrones Avanzados
################################################################################

# 1. Singleton usando módulo
# configuracion.py
_CONFIG = {
    "modo_debug": True,
    "max_intentos": 3
}

def obtener_config():
    return _CONFIG.copy()

# 2. Registro de plugins
class Plugin:
    _registro = []
    
    @classmethod
    def registrar(cls, func):
        cls._registro.append(func)
        return func

@Plugin.registrar
def mi_plugin():
    print("Plugin ejecutado")

# 3. Manejo de recursos externos
class GestorRecursos:
    def __init__(self):
        self._recursos = []
        
    def agregar_recurso(self, recurso):
        self._recursos.append(recurso)
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Liberando recursos...")
        self._recursos.clear()

# Uso del gestor de recursos
with GestorRecursos() as gr:
    gr.agregar_recurso("conexion_db")
    gr.agregar_recurso("archivo_temporal")
    print("Recursos durante el bloque:", gr._recursos)