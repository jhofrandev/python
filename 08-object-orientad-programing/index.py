################################################################################
# Programación Orientada a Objetos en Python
################################################################################

'''
La Programación Orientada a Objetos (POO) es un paradigma de programación
que utiliza "objetos" para modelar datos y comportamientos del mundo real.

Python es un lenguaje multiparadigma, pero tiene un fuerte soporte para POO.

Conceptos fundamentales:
- Clases: Plantillas para crear objetos
- Objetos: Instancias de clases
- Atributos: Datos/propiedades de los objetos
- Métodos: Funciones que definen el comportamiento de los objetos
- Herencia: Mecanismo para crear clases a partir de otras
- Encapsulamiento: Ocultar detalles internos y exponer solo lo necesario
- Polimorfismo: Capacidad de objetos de diferentes clases para responder al mismo mensaje
- Abstracción: Simplificar la complejidad mostrando solo lo esencial
'''

################################################################################
# 1. Clases y Objetos
################################################################################

# Definición básica de una clase
class Persona:
    """Clase que representa a una persona"""
    
    # Atributo de clase (compartido por todas las instancias)
    especie = "Homo sapiens"
    
    # Constructor (inicializador)
    def __init__(self, nombre, edad):
        # Atributos de instancia (específicos de cada objeto)
        self.nombre = nombre
        self.edad = edad
    
    # Método de instancia
    def presentarse(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."
    
    # Método de instancia que modifica atributos
    def cumplir_anos(self):
        self.edad += 1
        return f"{self.nombre} ahora tiene {self.edad} años."

# Crear objetos (instancias de la clase)
persona1 = Persona("Ana", 30)
persona2 = Persona("Carlos", 25)

# Acceder a atributos
print(f"Nombre de persona1: {persona1.nombre}")
print(f"Edad de persona2: {persona2.edad}")
print(f"Especie de persona1: {persona1.especie}")  # Atributo de clase

# Llamar a métodos
print(persona1.presentarse())
print(persona2.cumplir_anos())

# Modificar atributos
persona1.nombre = "Ana María"
print(persona1.presentarse())

################################################################################
# 2. Métodos Especiales (Dunder Methods)
################################################################################

class Punto:
    """Clase que representa un punto en el plano cartesiano"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Representación para desarrolladores
    def __repr__(self):
        return f"Punto({self.x}, {self.y})"
    
    # Representación para usuarios
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    # Sobrecarga del operador +
    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)
    
    # Sobrecarga del operador ==
    def __eq__(self, otro):
        return self.x == otro.x and self.y == otro.y
    
    # Método para calcular la longitud (distancia al origen)
    def __len__(self):
        import math
        return int(math.sqrt(self.x**2 + self.y**2))
    
    # Método para hacer la clase "llamable"
    def __call__(self, factor):
        return Punto(self.x * factor, self.y * factor)

# Crear puntos
p1 = Punto(3, 4)
p2 = Punto(1, 2)

print(f"\nRepresentación de p1: {p1}")
print(f"Representación para desarrolladores: {repr(p1)}")

# Usar operadores sobrecargados
p3 = p1 + p2
print(f"p1 + p2 = {p3}")

# Comparación
print(f"¿p1 == p2? {p1 == p2}")
print(f"¿p1 == Punto(3, 4)? {p1 == Punto(3, 4)}")

# Longitud
print(f"Longitud de p1: {len(p1)}")  # Distancia al origen (5)

# Llamar al objeto como función
p4 = p1(2)  # Equivalente a p1.__call__(2)
print(f"p1 llamado con factor 2: {p4}")

################################################################################
# 3. Herencia
################################################################################

# Clase base
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        return "El animal hace un sonido"
    
    def comer(self):
        return f"{self.nombre} está comiendo"

# Clase derivada
class Perro(Animal):
    def __init__(self, nombre, raza):
        # Llamar al constructor de la clase base
        super().__init__(nombre)
        self.raza = raza
    
    # Sobrescribir un método
    def hablar(self):
        return f"{self.nombre} dice: ¡Guau!"
    
    # Método específico de la clase derivada
    def perseguir_cola(self):
        return f"{self.nombre} está persiguiendo su cola"

# Clase derivada de Perro
class PerroPolicía(Perro):
    def __init__(self, nombre, raza, placa):
        super().__init__(nombre, raza)
        self.placa = placa
    
    def hablar(self):
        # Llamar al método de la clase padre
        return super().hablar() + " ¡Alto ahí!"
    
    def buscar(self):
        return f"{self.nombre} está buscando pistas"

# Crear instancias
animal = Animal("Genérico")
perro = Perro("Rex", "Pastor Alemán")
perro_policia = PerroPolicía("Max", "Rottweiler", "K9-123")

print(f"\nAnimal: {animal.hablar()}")
print(f"Perro: {perro.hablar()}")
print(f"Perro Policía: {perro_policia.hablar()}")
print(f"Perro Policía buscando: {perro_policia.buscar()}")

# Verificar herencia
print(f"¿perro es instancia de Animal? {isinstance(perro, Animal)}")
print(f"¿perro_policia es instancia de Perro? {isinstance(perro_policia, Perro)}")
print(f"¿animal es instancia de Perro? {isinstance(animal, Perro)}")

# Verificar clases
print(f"Clase de animal: {type(animal)}")
print(f"Clase de perro: {type(perro)}")
print(f"Jerarquía de clases de perro_policia: {PerroPolicía.__mro__}")

################################################################################
# 4. Herencia Múltiple
################################################################################

class Volador:
    def volar(self):
        return "Estoy volando"
    
    def aterrizar(self):
        return "Aterrizando"

class Nadador:
    def nadar(self):
        return "Estoy nadando"
    
    def bucear(self):
        return "Buceando"
    
    def aterrizar(self):
        return "Saliendo del agua"

# Herencia múltiple
class Pato(Animal, Volador, Nadador):
    def hablar(self):
        return f"{self.nombre} dice: ¡Cuac!"
    
    # Este método resolverá el conflicto entre Volador.aterrizar y Nadador.aterrizar
    def aterrizar(self):
        return f"{self.nombre} está aterrizando en el agua"

# Crear un pato
pato = Pato("Donald")
print(f"\nPato hablando: {pato.hablar()}")
print(f"Pato volando: {pato.volar()}")
print(f"Pato nadando: {pato.nadar()}")
print(f"Pato aterrizando: {pato.aterrizar()}")

# Orden de resolución de métodos (MRO)
print(f"MRO de Pato: {Pato.__mro__}")

################################################################################
# 5. Encapsulamiento
################################################################################

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular  # Atributo público
        self._saldo = saldo_inicial  # Atributo "protegido" (convención)
        self.__numero_cuenta = "123456789"  # Atributo privado (name mangling)
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            return f"Depósito de {cantidad} realizado. Nuevo saldo: {self._saldo}"
        return "La cantidad debe ser positiva"
    
    def retirar(self, cantidad):
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
            return f"Retiro de {cantidad} realizado. Nuevo saldo: {self._saldo}"
        return "Fondos insuficientes o cantidad inválida"
    
    def consultar_saldo(self):
        return f"Saldo actual de {self.titular}: {self._saldo}"
    
    def _generar_estado_cuenta(self):
        return f"Estado de cuenta para {self.titular}"
    
    def __metodo_privado(self):
        return "Este método es privado"
    
    # Método para acceder al método privado (para demostración)
    def acceder_privado(self):
        return self.__metodo_privado()

# Crear cuenta
cuenta = CuentaBancaria("Juan Pérez", 1000)
print(f"\nCuenta creada: {cuenta.consultar_saldo()}")

# Acceder a atributos
print(f"Titular: {cuenta.titular}")  # Público, acceso normal
print(f"Saldo (protegido): {cuenta._saldo}")  # Protegido, acceso posible pero no recomendado

# Intentar acceder a atributo privado
try:
    print(cuenta.__numero_cuenta)  # Esto fallará
except AttributeError as e:
    print(f"Error al acceder a atributo privado: {e}")

# Acceso real al atributo privado (name mangling)
print(f"Número de cuenta (privado): {cuenta._CuentaBancaria__numero_cuenta}")

# Usar métodos
print(cuenta.depositar(500))
print(cuenta.retirar(200))
print(cuenta._generar_estado_cuenta())  # Protegido, acceso posible pero no recomendado
print(cuenta.acceder_privado())

################################################################################
# 6. Propiedades y Decoradores
################################################################################

class Temperatura:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    # Getter
    @property
    def celsius(self):
        return self._celsius
    
    # Setter
    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("Temperatura por debajo del cero absoluto")
        self._celsius = valor
    
    # Propiedad calculada
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, valor):
        self.celsius = (valor - 32) * 5/9
    
    @property
    def kelvin(self):
        return self._celsius + 273.15
    
    @kelvin.setter
    def kelvin(self, valor):
        self.celsius = valor - 273.15

# Crear objeto
temp = Temperatura(25)
print(f"\nTemperatura inicial: {temp.celsius}°C")

# Usar propiedades
print(f"En Fahrenheit: {temp.fahrenheit}°F")
print(f"En Kelvin: {temp.kelvin}K")

# Modificar con setters
temp.celsius = 30
print(f"Nueva temperatura: {temp.celsius}°C, {temp.fahrenheit}°F, {temp.kelvin}K")

temp.fahrenheit = 68
print(f"Después de cambiar Fahrenheit: {temp.celsius}°C")

temp.kelvin = 300
print(f"Después de cambiar Kelvin: {temp.celsius}°C")

# Validación
try:
    temp.celsius = -300
except ValueError as e:
    print(f"Error: {e}")

################################################################################
# 7. Métodos de Clase y Métodos Estáticos
################################################################################

class Empleado:
    # Atributo de clase
    num_empleados = 0
    
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        Empleado.num_empleados += 1
    
    # Método de instancia
    def mostrar_detalles(self):
        return f"Nombre: {self.nombre}, Salario: {self.salario}"
    
    # Método de clase (opera sobre la clase, no sobre instancias)
    @classmethod
    def desde_cadena(cls, cadena):
        """Crea un empleado a partir de una cadena 'nombre-salario'"""
        nombre, salario = cadena.split('-')
        return cls(nombre, float(salario))
    
    @classmethod
    def obtener_num_empleados(cls):
        return f"Número total de empleados: {cls.num_empleados}"
    
    # Método estático (no depende de la clase ni de instancias)
    @staticmethod
    def es_dia_laboral(dia):
        """Verifica si un día es laboral (lunes a viernes)"""
        return dia.weekday() < 5  # 0-4 son lunes a viernes

# Crear empleados
emp1 = Empleado("Ana", 50000)
emp2 = Empleado("Carlos", 60000)

print(f"\nDetalles de emp1: {emp1.mostrar_detalles()}")
print(Empleado.obtener_num_empleados())

# Usar método de clase para crear instancia
emp3 = Empleado.desde_cadena("María-55000")
print(f"Detalles de emp3: {emp3.mostrar_detalles()}")
print(Empleado.obtener_num_empleados())

# Usar método estático
import datetime
hoy = datetime.date.today()
print(f"¿Hoy ({hoy}) es día laboral? {Empleado.es_dia_laboral(hoy)}")

################################################################################
# 8. Clases Abstractas
################################################################################

from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    """Clase abstracta que define la interfaz para todas las figuras geométricas"""
    
    @abstractmethod
    def area(self):
        """Calcula el área de la figura"""
        pass
    
    @abstractmethod
    def perimetro(self):
        """Calcula el perímetro de la figura"""
        pass
    
    def descripcion(self):
        """Método concreto que pueden usar las subclases"""
        return "Esta es una figura geométrica"

class Rectangulo(FiguraGeometrica):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto
    
    def perimetro(self):
        return 2 * (self.ancho + self.alto)
    
    def __str__(self):
        return f"Rectángulo de {self.ancho}x{self.alto}"

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        import math
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        import math
        return 2 * math.pi * self.radio
    
    def __str__(self):
        return f"Círculo de radio {self.radio}"

# No se puede instanciar una clase abstracta
try:
    figura = FiguraGeometrica()
except TypeError as e:
    print(f"\nError al instanciar clase abstracta: {e}")

# Crear figuras concretas
rectangulo = Rectangulo(5, 3)
circulo = Circulo(4)

print(f"Área del rectángulo: {rectangulo.area()}")
print(f"Perímetro del rectángulo: {rectangulo.perimetro()}")
print(f"Descripción: {rectangulo.descripcion()}")

print(f"Área del círculo: {circulo.area():.2f}")
print(f"Perímetro del círculo: {circulo.perimetro():.2f}")

################################################################################
# 9. Composición vs Herencia
################################################################################

# Composición: "tiene un"
class Motor:
    def __init__(self, tipo="gasolina"):
        self.tipo = tipo
        self.temperatura = 0
        self.encendido = False
    
    def encender(self):
        self.encendido = True
        self.temperatura = 50
        return "Motor encendido"
    
    def apagar(self):
        self.encendido = False
        self.temperatura = 0
        return "Motor apagado"
    
    def __str__(self):
        return f"Motor de {self.tipo}"

class Vehiculo:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor  # Composición
    
    def encender(self):
        return f"{self.marca} {self.modelo}: {self.motor.encender()}"
    
    def apagar(self):
        return f"{self.marca} {self.modelo}: {self.motor.apagar()}"
    
    def __str__(self):
        return f"{self.marca} {self.modelo} con {self.motor}"

# Crear objetos con composición
motor_gasolina = Motor("gasolina")
motor_electrico = Motor("eléctrico")

coche = Vehiculo("Toyota", "Corolla", motor_gasolina)
tesla = Vehiculo("Tesla", "Model 3", motor_electrico)

print(f"\nVehículo creado: {coche}")
print(coche.encender())
print(coche.apagar())

print(f"Vehículo eléctrico: {tesla}")

################################################################################
# 10. Mixins
################################################################################

class SerializableMixin:
    """Mixin que proporciona capacidades de serialización"""
    
    def to_dict(self):
        """Convierte el objeto a un diccionario"""
        return {key: value for key, value in self.__dict__.items() 
                if not key.startswith('_')}
    
    def to_json(self):
        """Convierte el objeto a JSON"""
        import json
        return json.dumps(self.to_dict())

class LogMixin:
    """Mixin que proporciona capacidades de logging"""
    
    def log(self, mensaje):
        print(f"[LOG] {self.__class__.__name__}: {mensaje}")

class Producto(SerializableMixin, LogMixin):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.log(f"Producto creado: {nombre}")
    
    def aplicar_descuento(self, porcentaje):
        descuento = self.precio * porcentaje / 100
        self.precio -= descuento
        self.log(f"Descuento aplicado: {porcentaje}%. Nuevo precio: {self.precio}")

# Usar mixins
producto = Producto("Laptop", 1200)
print(f"\nProducto como diccionario: {producto.to_dict()}")
print(f"Producto como JSON: {producto.to_json()}")

producto.aplicar_descuento(10)
print(f"Después del descuento: {producto.to_dict()}")

################################################################################
# 11. Descriptores
################################################################################

class Validador:
    """Descriptor para validar valores"""
    
    def __init__(self, min_valor=None, max_valor=None):
        self.min_valor = min_valor
        self.max_valor = max_valor
        self.nombre = None
    
    def __set_name__(self, owner, nombre):
        self.nombre = nombre
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.nombre)
    
    def __set__(self, instance, valor):
        if self.min_valor is not None and valor < self.min_valor:
            raise ValueError(f"{self.nombre} debe ser >= {self.min_valor}")
        if self.max_valor is not None and valor > self.max_valor:
            raise ValueError(f"{self.nombre} debe ser <= {self.max_valor}")
        instance.__dict__[self.nombre] = valor

class Persona2:
    """Clase que usa descriptores para validar atributos"""
    
    edad = Validador(min_valor=0, max_valor=120)
    altura = Validador(min_valor=0, max_valor=250)
    peso = Validador(min_valor=0, max_valor=500)
    
    def __init__(self, nombre, edad, altura, peso):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso
    
    def __str__(self):
        return f"{self.nombre}: {self.edad} años, {self.altura}cm, {self.peso}kg"

# Usar descriptores
try:
    persona = Persona2("Juan", 30, 175, 70)
    print(f"\nPersona creada: {persona}")
    
    # Esto debería fallar
    persona.edad = -5
except ValueError as e:
    print(f"Error: {e}")

try:
    # Esto debería fallar
    persona.altura = 300
except ValueError as e:
    print(f"Error: {e}")

################################################################################
# 12. Metaclases
################################################################################

class Meta(type):
    """Metaclase que registra todas las clases que la usan"""
    
    clases = {}
    
    def __new__(mcs, nombre, bases, attrs):
        clase = super().__new__(mcs, nombre, bases, attrs)
        mcs.clases[nombre] = clase
        print(f"Clase {nombre} creada")
        return clase

class ModeloBase(metaclass=Meta):
    """Clase base para modelos que usa la metaclase Meta"""
    
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def guardar(self):
        print(f"Guardando {self.__class__.__name__}")

class Usuario(ModeloBase):
    pass

class Producto2(ModeloBase):
    pass

# Usar metaclases
print("\nClases registradas:", list(Meta.clases.keys()))

usuario = Usuario(nombre="Ana", email="ana@ejemplo.com")
producto = Producto2(nombre="Laptop", precio=1200)

usuario.guardar()
producto.guardar()

################################################################################
# 13. Patrones de Diseño
################################################################################

# Patrón Singleton
class Singleton(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class ConfiguracionApp(metaclass=Singleton):
    def __init__(self):
        self.tema = "claro"
        self.idioma = "es"
        self.notificaciones = True
    
    def __str__(self):
        return f"Configuración: tema={self.tema}, idioma={self.idioma}, notificaciones={self.notificaciones}"

# Patrón Factory
class AnimalFactory:
    @staticmethod
    def crear_animal(tipo, **kwargs):
        if tipo == "perro":
            return Perro(**kwargs)
        elif tipo == "gato":
            return Gato(**kwargs)
        else:
            raise ValueError(f"Tipo de animal desconocido: {tipo}")

class Gato(Animal):
    def __init__(self, nombre, color="naranja"):
        super().__init__(nombre)
        self.color = color
    
    def hablar(self):
        return f"{self.nombre} dice: ¡Miau!"
    
    def __str__(self):
        return f"Gato {self.nombre} de color {self.color}"

# Usar patrones
print("\n--- Patrón Singleton ---")
config1 = ConfiguracionApp()
config2 = ConfiguracionApp()
print(f"¿Son el mismo objeto? {config1 is config2}")
config1.tema = "oscuro"
print(f"Config1: {config1}")
print(f"Config2: {config2}")  # También cambió porque es el mismo objeto

print("\n--- Patrón Factory ---")
factory = AnimalFactory()
mi_perro = factory.crear_animal("perro", nombre="Rex", raza="Labrador")
mi_gato = factory.crear_animal("gato", nombre="Garfield", color="naranja")
print(mi_perro.hablar())
print(mi_gato.hablar())

################################################################################
# 14. Dataclasses (Python 3.7+)
################################################################################

from dataclasses import dataclass, field

@dataclass
class Punto2D:
    """Clase para representar un punto en 2D usando dataclass"""
    x: float
    y: float
    
    def distancia_al_origen(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)

@dataclass
class Rectangulo2D:
    """Rectángulo definido por dos puntos"""
    p1: Punto2D
    p2: Punto2D
    color: str = "negro"
    area: float = field(init=False)
    
    def __post_init__(self):
        self.area = abs(self.p2.x - self.p1.x) * abs(self.p2.y - self.p1.y)
    
    def contiene_punto(self, punto):
        return (self.p1.x <= punto.x <= self.p2.x and 
                self.p1.y <= punto.y <= self.p2.y)

# Usar dataclasses
print("\n--- Dataclasses ---")
p1 = Punto2D(3, 4)
p2 = Punto2D(6, 8)
print(f"Punto: {p1}")
print(f"Distancia al origen: {p1.distancia_al_origen()}")

rect = Rectangulo2D(p1, p2, "rojo")
print(f"Rectángulo: {rect}")
print(f"Área: {rect.area}")

p3 = Punto2D(4, 5)
print(f"¿El rectángulo contiene el punto {p3}? {rect.contiene_punto(p3)}")

################################################################################
# 15. Type Hints (Python 3.5+)
################################################################################

from typing import List, Dict, Tuple, Optional, Union, Callable

class Inventario:
    def __init__(self) -> None:
        self.items: Dict[str, int] = {}
    
    def agregar_item(self, nombre: str, cantidad: int) -> None:
        if nombre in self.items:
            self.items[nombre] += cantidad
        else:
            self.items[nombre] = cantidad
    
    def obtener_cantidad(self, nombre: str) -> int:
        return self.items.get(nombre, 0)
    
    def listar_items(self) -> List[Tuple[str, int]]:
        return [(nombre, cantidad) for nombre, cantidad in self.items.items()]
    
    def procesar_items(self, func: Callable[[str, int], None]) -> None:
        for nombre, cantidad in self.items.items():
            func(nombre, cantidad)

def imprimir_item(nombre: str, cantidad: int) -> None:
    print(f"Item: {nombre}, Cantidad: {cantidad}")

# Usar type hints
print("\n--- Type Hints ---")
inventario = Inventario()
inventario.agregar_item("Laptop", 5)
inventario.agregar_item("Mouse", 10)
inventario.agregar_item("Teclado", 7)

print(f"Cantidad de laptops: {inventario.obtener_cantidad('Laptop')}")
print("Listado de items:")
for item, cantidad in inventario.listar_items():
    print(f"  {item}: {cantidad}")

print("Procesando items:")
inventario.procesar_items(imprimir_item)

################################################################################
# 16. Context Managers
################################################################################

class Temporizador:
    """Context manager para medir el tiempo de ejecución"""
    
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
    
    def __enter__(self) -> 'Temporizador':
        import time
        self.inicio = time.time()
        print(f"Iniciando {self.nombre}...")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        import time
        self.fin = time.time()
        self.duracion = self.fin - self.inicio
        print(f"{self.nombre} completado en {self.duracion:.6f} segundos")
        
        # Si devolvemos True, se suprime cualquier excepción
        return False

class Transaccion:
    """Context manager para simular una transacción"""
    
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
    
    def __enter__(self) -> 'Transaccion':
        print(f"Iniciando transacción {self.nombre}")
        print("BEGIN TRANSACTION")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if exc_type is not None:
            print(f"Error en transacción {self.nombre}: {exc_val}")
            print("ROLLBACK")
            return False  # Propaga la excepción
        else:
            print(f"Transacción {self.nombre} completada")
            print("COMMIT")
            return True

# Usar context managers
print("\n--- Context Managers ---")

with Temporizador("Operación costosa") as t:
    # Simular operación costosa
    import time
    time.sleep(1.5)
    print("Realizando operación...")

# Transacción exitosa
with Transaccion("Guardar usuario"):
    print("Insertando datos de usuario...")

# Transacción con error
try:
    with Transaccion("Actualizar producto"):
        print("Actualizando producto...")
        raise ValueError("Precio inválido")
except ValueError:
    print("Error capturado fuera del context manager")

################################################################################
# 17. Protocolos y Duck Typing
################################################################################

print("\n--- Protocolos y Duck Typing ---")

class Pato:
    def nadar(self):
        return "El pato está nadando"
    
    def volar(self):
        return "El pato está volando"
    
    def graznar(self):
        return "¡Cuac!"

class PatoRobot:
    def nadar(self):
        return "El pato robot está nadando"
    
    def volar(self):
        return "El pato robot está volando"
    
    def graznar(self):
        return "¡Cuac! (electrónico)"

def hacer_cosas_de_pato(pato):
    """Esta función espera un objeto que se comporte como un pato"""
    print(pato.nadar())
    print(pato.volar())
    print(pato.graznar())

# Duck typing en acción
pato_real = Pato()
pato_robot = PatoRobot()

print("Con un pato real:")
hacer_cosas_de_pato(pato_real)

print("\nCon un pato robot:")
hacer_cosas_de_pato(pato_robot)

# Implementación del protocolo de iteración
class ContadorPersonalizado:
    def __init__(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin
        self.valor = inicio - 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.valor += 1
        if self.valor > self.fin:
            raise StopIteration
        return self.valor

print("\nImplementación del protocolo de iteración:")
for num in ContadorPersonalizado(1, 5):
    print(num, end=" ")
print()

################################################################################
# 18. Clases Internas y Anidadas
################################################################################

print("\n--- Clases Internas y Anidadas ---")

class Exterior:
    """Clase exterior que contiene una clase interna"""
    
    contador = 0
    
    def __init__(self, valor):
        self.valor = valor
        Exterior.contador += 1
        self.interno = self.Interno(self)
    
    def metodo_exterior(self):
        return f"Método de la clase exterior, valor: {self.valor}"
    
    class Interno:
        """Clase interna que tiene acceso a la clase exterior"""
        
        def __init__(self, exterior):
            self.exterior = exterior
        
        def metodo_interno(self):
            return f"Método de la clase interna, valor exterior: {self.exterior.valor}"
        
        def obtener_contador(self):
            return f"Contador de la clase exterior: {Exterior.contador}"

# Usar clases anidadas
ext = Exterior(10)
print(ext.metodo_exterior())
print(ext.interno.metodo_interno())
print(ext.interno.obtener_contador())

# También se puede acceder directamente a la clase interna
interno_directo = Exterior.Interno(ext)
print(interno_directo.metodo_interno())

################################################################################
# 19. Métodos de Resolución de Orden (MRO)
################################################################################

print("\n--- Métodos de Resolución de Orden (MRO) ---")

class A:
    def metodo(self):
        return "Método de A"

class B(A):
    def metodo(self):
        return "Método de B"

class C(A):
    def metodo(self):
        return "Método de C"

class D(B, C):
    pass

class E(C, B):
    pass

# Ver el orden de resolución de métodos
print(f"MRO de D: {[cls.__name__ for cls in D.__mro__]}")
print(f"MRO de E: {[cls.__name__ for cls in E.__mro__]}")

# Llamar a métodos
d = D()
e = E()
print(f"d.metodo() llama a: {d.metodo()}")  # Llama a B.metodo()
print(f"e.metodo() llama a: {e.metodo()}")  # Llama a C.metodo()

################################################################################
# 20. Slots
################################################################################

print("\n--- Slots ---")

class PersonaNormal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class PersonaConSlots:
    __slots__ = ['nombre', 'edad']
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Comparar uso de memoria y comportamiento
persona_normal = PersonaNormal("Juan", 30)
persona_slots = PersonaConSlots("Ana", 25)

# Añadir atributo dinámicamente
persona_normal.email = "juan@ejemplo.com"
try:
    persona_slots.email = "ana@ejemplo.com"
except AttributeError as e:
    print(f"Error al añadir atributo a PersonaConSlots: {e}")

# Ver atributos
print(f"Atributos de persona_normal: {persona_normal.__dict__}")
print(f"Slots de persona_slots: {PersonaConSlots.__slots__}")

# Comparar tamaño en memoria
import sys
print(f"Tamaño de persona_normal: {sys.getsizeof(persona_normal.__dict__)} bytes")
print(f"Tamaño aproximado de persona_slots: {sys.getsizeof(persona_slots)} bytes")

################################################################################
# 21. Introspección y Reflexión
################################################################################

print("\n--- Introspección y Reflexión ---")

class Ejemplo:
    """Clase de ejemplo para demostrar introspección"""
    
    atributo_clase = "Valor de clase"
    
    def __init__(self, valor):
        self.valor = valor
    
    def metodo(self, parametro):
        """Este es un método de ejemplo"""
        return f"Método llamado con {parametro}"
    
    @classmethod
    def metodo_clase(cls):
        return "Método de clase"
    
    @staticmethod
    def metodo_estatico():
        return "Método estático"

# Crear instancia
ejemplo = Ejemplo(42)

# Introspección básica
print(f"Tipo: {type(ejemplo)}")
print(f"Clase: {ejemplo.__class__}")
print(f"Módulo: {ejemplo.__class__.__module__}")
print(f"Docstring: {Ejemplo.__doc__}")
print(f"Atributos y métodos: {dir(ejemplo)[:10]}...")

# Verificar tipos y relaciones
print(f"¿ejemplo es instancia de Ejemplo? {isinstance(ejemplo, Ejemplo)}")
print(f"¿Ejemplo es subclase de object? {issubclass(Ejemplo, object)}")

# Obtener atributos y métodos dinámicamente
print(f"Valor del atributo 'valor': {getattr(ejemplo, 'valor')}")
print(f"Llamar al método 'metodo': {getattr(ejemplo, 'metodo')('test')}")

# Modificar dinámicamente
setattr(ejemplo, 'nuevo_atributo', 100)
print(f"Nuevo atributo: {ejemplo.nuevo_atributo}")

# Listar métodos y atributos
import inspect

print("\nMétodos:")
for nombre, objeto in inspect.getmembers(Ejemplo, inspect.isfunction):
    print(f"  {nombre}: {objeto}")

print("\nAtributos:")
for nombre, objeto in inspect.getmembers(Ejemplo, lambda x: not inspect.isroutine(x) and not nombre.startswith('__')):
    print(f"  {nombre}: {objeto}")

################################################################################
# 22. Clases Funcionales y Decoradores de Clases
################################################################################

print("\n--- Clases Funcionales y Decoradores de Clases ---")

# Decorador de clase
def agregar_metodos(cls):
    """Decorador que agrega métodos a una clase"""
    
    def metodo_nuevo(self, x):
        return f"Método nuevo con {x}"
    
    cls.metodo_nuevo = metodo_nuevo
    cls.atributo_nuevo = "Valor agregado por el decorador"
    
    return cls

@agregar_metodos
class ClaseDecorada:
    def __init__(self, valor):
        self.valor = valor
    
    def metodo_original(self):
        return f"Método original, valor: {self.valor}"

# Usar la clase decorada
obj = ClaseDecorada(10)
print(obj.metodo_original())
print(obj.metodo_nuevo("parámetro"))
print(f"Atributo nuevo: {obj.atributo_nuevo}")

# Clase funcional (creada dinámicamente)
def crear_clase(nombre, atributos, metodos):
    """Crea una clase dinámicamente"""
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    cls_dict = {'__init__': __init__}
    
    # Agregar atributos de clase
    for key, value in atributos.items():
        cls_dict[key] = value
    
    # Agregar métodos
    for nombre_metodo, func in metodos.items():
        cls_dict[nombre_metodo] = func
    
    # Crear la clase
    return type(nombre, (object,), cls_dict)

# Definir un método para la clase dinámica
def saludar(self):
    return f"Hola, soy {self.nombre}"

# Crear una clase dinámicamente
PersonaDinamica = crear_clase(
    "PersonaDinamica",
    {"especie": "Humano"},
    {"saludar": saludar}
)

# Usar la clase dinámica
persona_din = PersonaDinamica(nombre="Carlos", edad=35)
print(f"Clase dinámica: {PersonaDinamica.__name__}")
print(f"Atributos: nombre={persona_din.nombre}, edad={persona_din.edad}, especie={persona_din.especie}")
print(persona_din.saludar())

################################################################################
# 23. Patrones Avanzados
################################################################################

print("\n--- Patrones Avanzados ---")

# Patrón Observer
class Sujeto:
    """Sujeto que notifica a los observadores cuando cambia su estado"""
    
    def __init__(self):
        self._observadores = []
        self._estado = None
    
    def agregar_observador(self, observador):
        if observador not in self._observadores:
            self._observadores.append(observador)
    
    def eliminar_observador(self, observador):
        if observador in self._observadores:
            self._observadores.remove(observador)
    
    def notificar_observadores(self):
        for observador in self._observadores:
            observador.actualizar(self)
    
    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self, valor):
        self._estado = valor
        self.notificar_observadores()

class Observador:
    """Interfaz para los observadores"""
    
    def actualizar(self, sujeto):
        pass

class ObservadorConcreto(Observador):
    """Implementación concreta de un observador"""
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def actualizar(self, sujeto):
        print(f"Observador {self.nombre} notificado. Nuevo estado: {sujeto.estado}")

# Usar el patrón Observer
sujeto = Sujeto()
observador1 = ObservadorConcreto("Obs1")
observador2 = ObservadorConcreto("Obs2")

sujeto.agregar_observador(observador1)
sujeto.agregar_observador(observador2)

print("Cambiando estado del sujeto:")
sujeto.estado = "Estado 1"

print("Eliminando un observador y cambiando estado:")
sujeto.eliminar_observador(observador1)
sujeto.estado = "Estado 2"

# Patrón Strategy
class Estrategia:
    """Interfaz para las estrategias"""
    
    def ejecutar(self, datos):
        pass

class EstrategiaSuma(Estrategia):
    def ejecutar(self, datos):
        return sum(datos)

class EstrategiaPromedio(Estrategia):
    def ejecutar(self, datos):
        return sum(datos) / len(datos)

class EstrategiaMax(Estrategia):
    def ejecutar(self, datos):
        return max(datos)

class Contexto:
    """Contexto que usa una estrategia"""
    
    def __init__(self, estrategia=None):
        self.estrategia = estrategia
    
    def establecer_estrategia(self, estrategia):
        self.estrategia = estrategia
    
    def ejecutar_estrategia(self, datos):
        if self.estrategia is None:
            raise ValueError("No se ha establecido una estrategia")
        return self.estrategia.ejecutar(datos)

# Usar el patrón Strategy
datos = [1, 2, 3, 4, 5]
contexto = Contexto()

print("\nUsando diferentes estrategias:")
contexto.establecer_estrategia(EstrategiaSuma())
print(f"Suma: {contexto.ejecutar_estrategia(datos)}")

contexto.establecer_estrategia(EstrategiaPromedio())
print(f"Promedio: {contexto.ejecutar_estrategia(datos)}")

contexto.establecer_estrategia(EstrategiaMax())
print(f"Máximo: {contexto.ejecutar_estrategia(datos)}")

################################################################################
# 24. Programación Orientada a Aspectos
################################################################################

print("\n--- Programación Orientada a Aspectos ---")

# Implementación básica de AOP con decoradores
def aspecto_logging(func):
    """Aspecto que agrega logging a un método"""
    def wrapper(*args, **kwargs):
        print(f"[LOG] Llamando a {func.__name__} con args={args}, kwargs={kwargs}")
        resultado = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} retornó {resultado}")
        return resultado
    return wrapper

def aspecto_tiempo(func):
    """Aspecto que mide el tiempo de ejecución"""
    def wrapper(*args, **kwargs):
        import time
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"[TIEMPO] {func.__name__} tardó {fin - inicio:.6f} segundos")
        return resultado
    return wrapper

def aspecto_cache(func):
    """Aspecto que implementa caché de resultados"""
    cache = {}
    def wrapper(*args):
        if args in cache:
            print(f"[CACHE] Usando resultado en caché para {args}")
            return cache[args]
        resultado = func(*args)
        cache[args] = resultado
        return resultado
    return wrapper

# Aplicar aspectos a una clase
class Calculadora:
    @aspecto_logging
    @aspecto_tiempo
    def sumar(self, a, b):
        return a + b
    
    @aspecto_cache
    @aspecto_tiempo
    def factorial(self, n):
        if n <= 1:
            return 1
        return n * self.factorial(n - 1)

# Usar la clase con aspectos
calc = Calculadora()
print(f"Suma: {calc.sumar(5, 3)}")
print(f"Factorial de 5: {calc.factorial(5)}")
print(f"Factorial de 5 (de nuevo): {calc.factorial(5)}")  # Debería usar caché

################################################################################
# 25. Conclusiones y Mejores Prácticas
################################################################################

'''
Conclusiones sobre Programación Orientada a Objetos en Python:

1. Python implementa POO de manera flexible y dinámica, permitiendo:
   - Herencia múltiple
   - Métodos especiales para personalizar comportamiento
   - Propiedades para encapsulamiento
   - Metaclases para personalizar la creación de clases

2. Principios de diseño importantes:
   - DRY (Don't Repeat Yourself)
   - SOLID:
     - Single Responsibility (Responsabilidad Única)
     - Open/Closed (Abierto/Cerrado)
     - Liskov Substitution (Sustitución de Liskov)
     - Interface Segregation (Segregación de Interfaces)
     - Dependency Inversion (Inversión de Dependencias)
   - Composición sobre herencia
   - Programar hacia interfaces, no implementaciones

3. Mejores prácticas:
   - Usar nombres descriptivos para clases y métodos
   - Documentar clases y métodos con docstrings
   - Mantener las clases cohesivas y con responsabilidad única
   - Preferir composición sobre herencia profunda
   - Usar propiedades en lugar de getters/setters explícitos
   - Implementar métodos especiales para comportamiento intuitivo
   - Usar type hints para mejorar la legibilidad y el soporte de herramientas
   - Aplicar patrones de diseño cuando sea apropiado

4. Características avanzadas:
   - Metaclases para casos especiales
   - Descriptores para control fino de atributos
   - Context managers para gestión de recursos
   - Decoradores para aspectos transversales
   - Slots para optimización de memoria

La POO en Python es una herramienta poderosa que, cuando se usa correctamente,
puede llevar a código más mantenible, extensible y reutilizable.
'''

print("\n--- Fin del tutorial de POO en Python ---")