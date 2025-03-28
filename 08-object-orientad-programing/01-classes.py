################################################################################
# Profundizando en las Clases en Python
################################################################################

'''
Las clases son el núcleo de la Programación Orientada a Objetos en Python.
Permiten definir nuevos tipos de datos con:
- Atributos (datos)
- Métodos (funciones)
- Comportamientos personalizados
'''

################################################################################
# 1. Anatomía de una Clase
################################################################################

class Persona:
    """
    Clase que representa a una persona.
    
    Esta es la documentación de la clase (docstring) que describe
    qué hace la clase y cómo se utiliza.
    """
    
    # Atributo de clase (compartido por todas las instancias)
    especie = "Homo sapiens"
    contador = 0
    
    # Método inicializador (constructor)
    def __init__(self, nombre, edad):
        """
        Inicializa una nueva instancia de Persona.
        
        Args:
            nombre (str): El nombre de la persona
            edad (int): La edad de la persona
        """
        # Atributos de instancia (específicos de cada objeto)
        self.nombre = nombre
        self.edad = edad
        self._id = Persona.contador  # Atributo "protegido" (convención)
        self.__dni = None  # Atributo "privado" (name mangling)
        
        # Incrementar el contador de personas
        Persona.contador += 1
    
    # Método de instancia
    def presentarse(self):
        """Retorna una presentación de la persona."""
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."
    
    # Método de instancia que modifica el estado
    def cumplir_anos(self):
        """Incrementa la edad de la persona en 1 año."""
        self.edad += 1
        return f"{self.nombre} ahora tiene {self.edad} años."
    
    # Método de clase (opera sobre la clase, no sobre instancias)
    @classmethod
    def crear_desde_nacimiento(cls, nombre, anio_nacimiento):
        """
        Crea una persona a partir de su año de nacimiento.
        
        Args:
            nombre (str): El nombre de la persona
            anio_nacimiento (int): El año de nacimiento
            
        Returns:
            Persona: Una nueva instancia de Persona
        """
        import datetime
        edad = datetime.datetime.now().year - anio_nacimiento
        return cls(nombre, edad)
    
    # Método estático (no depende de la clase ni de instancias)
    @staticmethod
    def es_adulto(edad):
        """
        Determina si una edad corresponde a un adulto.
        
        Args:
            edad (int): La edad a verificar
            
        Returns:
            bool: True si es adulto, False en caso contrario
        """
        return edad >= 18
    
    # Método especial para representación de cadena
    def __str__(self):
        """Representación en cadena para usuarios."""
        return f"Persona(nombre='{self.nombre}', edad={self.edad})"
    
    # Método especial para representación para desarrolladores
    def __repr__(self):
        """Representación en cadena para desarrolladores."""
        return f"Persona('{self.nombre}', {self.edad})"
    
    # Método especial para comparación de igualdad
    def __eq__(self, otro):
        """
        Compara si dos personas son iguales.
        
        Args:
            otro: Otra instancia de Persona
            
        Returns:
            bool: True si son iguales, False en caso contrario
        """
        if not isinstance(otro, Persona):
            return False
        return self.nombre == otro.nombre and self.edad == otro.edad

################################################################################
# 2. Creación y Uso de Instancias
################################################################################

# Crear instancias (objetos) de la clase Persona
persona1 = Persona("Ana", 30)
persona2 = Persona("Carlos", 25)

# Acceder a atributos de instancia
print(f"Nombre de persona1: {persona1.nombre}")
print(f"Edad de persona2: {persona2.edad}")

# Acceder a atributos de clase
print(f"Especie de persona1: {persona1.especie}")
print(f"Especie de la clase Persona: {Persona.especie}")

# Llamar a métodos de instancia
print(persona1.presentarse())
print(persona2.cumplir_anos())

# Modificar atributos
persona1.nombre = "Ana María"
print(persona1.presentarse())

# Usar método de clase
persona3 = Persona.crear_desde_nacimiento("Luis", 1990)
print(persona3.presentarse())

# Usar método estático
print(f"¿Es adulto alguien de 15 años? {Persona.es_adulto(15)}")
print(f"¿Es adulto alguien de 21 años? {Persona.es_adulto(21)}")

# Usar métodos especiales
print(f"Representación de persona1: {persona1}")
print(f"Representación para desarrolladores: {repr(persona1)}")

# Comparar instancias
persona4 = Persona("Ana María", 30)
print(f"¿persona1 == persona4? {persona1 == persona4}")
print(f"¿persona1 == persona2? {persona1 == persona2}")

# Ver el contador de instancias
print(f"Número de personas creadas: {Persona.contador}")

################################################################################
# 3. Atributos de Clase vs Atributos de Instancia
################################################################################

class Ejemplo:
    # Atributo de clase
    atributo_clase = "Valor compartido"
    
    def __init__(self, valor):
        # Atributo de instancia
        self.atributo_instancia = valor

# Crear instancias
ejemplo1 = Ejemplo("valor1")
ejemplo2 = Ejemplo("valor2")

# Acceder a atributos
print(f"\nAtributo de clase desde la clase: {Ejemplo.atributo_clase}")
print(f"Atributo de clase desde ejemplo1: {ejemplo1.atributo_clase}")
print(f"Atributo de clase desde ejemplo2: {ejemplo2.atributo_clase}")

print(f"Atributo de instancia de ejemplo1: {ejemplo1.atributo_instancia}")
print(f"Atributo de instancia de ejemplo2: {ejemplo2.atributo_instancia}")

# Modificar atributo de clase desde la clase
Ejemplo.atributo_clase = "Nuevo valor compartido"
print(f"Después de modificar, desde la clase: {Ejemplo.atributo_clase}")
print(f"Después de modificar, desde ejemplo1: {ejemplo1.atributo_clase}")
print(f"Después de modificar, desde ejemplo2: {ejemplo2.atributo_clase}")

# Modificar atributo de clase desde una instancia
ejemplo1.atributo_clase = "Valor específico de ejemplo1"
print(f"Después de modificar desde instancia:")
print(f"Desde la clase: {Ejemplo.atributo_clase}")
print(f"Desde ejemplo1: {ejemplo1.atributo_clase}")  # Ahora es un atributo de instancia
print(f"Desde ejemplo2: {ejemplo2.atributo_clase}")

################################################################################
# 4. Encapsulamiento y Convenciones de Nombres
################################################################################

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular  # Público
        self._saldo = saldo_inicial  # "Protegido" (convención)
        self.__numero_cuenta = "123456789"  # "Privado" (name mangling)
    
    def depositar(self, cantidad):
        """Deposita dinero en la cuenta."""
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False
    
    def retirar(self, cantidad):
        """Retira dinero de la cuenta si hay saldo suficiente."""
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
            return True
        return False
    
    def consultar_saldo(self):
        """Retorna el saldo actual."""
        return self._saldo
    
    def _metodo_protegido(self):
        """
        Método "protegido" (convención).
        No debería ser llamado desde fuera de la clase o subclases.
        """
        return "Este método es protegido"
    
    def __metodo_privado(self):
        """
        Método "privado" (name mangling).
        No debería ser accesible desde fuera de la clase.
        """
        return "Este método es privado"
    
    def obtener_numero_cuenta_enmascarado(self):
        """Retorna una versión enmascarada del número de cuenta."""
        return "****" + self.__numero_cuenta[-5:]

# Crear cuenta
cuenta = CuentaBancaria("Juan Pérez", 1000)

# Acceder a atributos y métodos públicos
print(f"\nTitular: {cuenta.titular}")
print(f"Saldo inicial: {cuenta.consultar_saldo()}")

# Operaciones
cuenta.depositar(500)
print(f"Saldo después de depósito: {cuenta.consultar_saldo()}")
cuenta.retirar(200)
print(f"Saldo después de retiro: {cuenta.consultar_saldo()}")

# Acceder a atributos y métodos "protegidos" (posible pero no recomendado)
print(f"Acceso directo al saldo (no recomendado): {cuenta._saldo}")
print(f"Llamada a método protegido (no recomendado): {cuenta._metodo_protegido()}")

# Intentar acceder a atributos y métodos "privados"
try:
    print(cuenta.__numero_cuenta)  # Esto fallará
except AttributeError as e:
    print(f"Error al acceder a atributo privado: {e}")

try:
    print(cuenta.__metodo_privado())  # Esto fallará
except AttributeError as e:
    print(f"Error al llamar método privado: {e}")

# Acceso real a atributos y métodos "privados" (name mangling)
print(f"Acceso real al número de cuenta: {cuenta._CuentaBancaria__numero_cuenta}")
print(f"Llamada real al método privado: {cuenta._CuentaBancaria__metodo_privado()}")

# Forma correcta de acceder a información "privada"
print(f"Número de cuenta enmascarado: {cuenta.obtener_numero_cuenta_enmascarado()}")

################################################################################
# 5. Herencia y Composición
################################################################################

# Herencia: "es un"
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        return "..."

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"
    
    def mover_cola(self):
        return f"{self.nombre} está moviendo la cola"

# Composición: "tiene un"
class Motor:
    def __init__(self, tipo):
        self.tipo = tipo
        self.encendido = False
    
    def encender(self):
        self.encendido = True
        return f"Motor de {self.tipo} encendido"
    
    def apagar(self):
        self.encendido = False
        return f"Motor de {self.tipo} apagado"

class Coche:
    def __init__(self, marca, modelo, tipo_motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor(tipo_motor)  # Composición
    
    def encender(self):
        return f"{self.marca} {self.modelo}: {self.motor.encender()}"
    
    def apagar(self):
        return f"{self.marca} {self.modelo}: {self.motor.apagar()}"

# Usar herencia
perro = Perro("Rex")
print(f"\nSonido del perro: {perro.hacer_sonido()}")
print(perro.mover_cola())

# Usar composición
coche = Coche("Toyota", "Corolla", "gasolina")
print(coche.encender())
print(coche.apagar())

################################################################################
# 6. Métodos Especiales (Dunder Methods)
################################################################################

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Representación para usuarios
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    # Representación para desarrolladores
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    # Suma de vectores
    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y)
    
    # Resta de vectores
    def __sub__(self, otro):
        return Vector(self.x - otro.x, self.y - otro.y)
    
    # Multiplicación por escalar
    def __mul__(self, escalar):
        return Vector(self.x * escalar, self.y * escalar)
    
    # Multiplicación por escalar (conmutativa)
    def __rmul__(self, escalar):
        return self.__mul__(escalar)
    
    # Igualdad
    def __eq__(self, otro):
        if not isinstance(otro, Vector):
            return False
        return self.x == otro.x and self.y == otro.y
    
    # Longitud (magnitud del vector)
    def __abs__(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)
    
    # Hacer el objeto "llamable"
    def __call__(self, mensaje):
        return f"Vector {self} dice: {mensaje}"
    
    # Acceso como diccionario
    def __getitem__(self, clave):
        if clave == 'x':
            return self.x
        elif clave == 'y':
            return self.y
        else:
            raise KeyError(f"Clave no válida: {clave}")
    
    # Iteración
    def __iter__(self):
        yield self.x
        yield self.y

# Crear vectores
v1 = Vector(3, 4)
v2 = Vector(1, 2)

# Usar métodos especiales
print(f"\nVector v1: {v1}")
print(f"Representación para desarrolladores: {repr(v1)}")

# Operaciones
v3 = v1 + v2
print(f"v1 + v2 = {v3}")

v4 = v1 - v2
print(f"v1 - v2 = {v4}")

v5 = v1 * 2
print(f"v1 * 2 = {v5}")

v6 = 3 * v1
print(f"3 * v1 = {v6}")

# Comparación
print(f"¿v1 == v2? {v1 == v2}")
print(f"¿v1 == Vector(3, 4)? {v1 == Vector(3, 4)}")

# Magnitud
print(f"Magnitud de v1: {abs(v1)}")

# Llamar al objeto
print(v1("¡Hola!"))

# Acceso como diccionario
print(f"v1['x'] = {v1['x']}")
print(f"v1['y'] = {v1['y']}")

# Iteración
print("Componentes de v1:", end=" ")
for componente in v1:
    print(componente, end=" ")
print()

################################################################################
# 7. Propiedades
################################################################################

class Temperatura:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    # Propiedad celsius
    @property
    def celsius(self):
        """Obtiene la temperatura en grados Celsius."""
        return self._celsius
    
    @celsius.setter
    def celsius(self, valor):
        """Establece la temperatura en grados Celsius."""
        if valor < -273.15:
            raise ValueError("Temperatura por debajo del cero absoluto")
        self._celsius = valor
    
    # Propiedad fahrenheit (calculada)
    @property
    def fahrenheit(self):
        """Obtiene la temperatura en grados Fahrenheit."""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, valor):
        """Establece la temperatura en grados Fahrenheit."""
        self.celsius = (valor - 32) * 5/9

# Usar propiedades
temp = Temperatura(25)
print(f"\nTemperatura inicial: {temp.celsius}°C")
print(f"En Fahrenheit: {temp.fahrenheit}°F")

# Modificar con setters
temp.celsius = 30
print(f"Después de cambiar Celsius: {temp.celsius}°C, {temp.fahrenheit}°F")

temp.fahrenheit = 68
print(f"Después de cambiar Fahrenheit: {temp.celsius}°C, {temp.fahrenheit}°F")

# Validación
try:
    temp.celsius = -300
except ValueError as e:
    print(f"Error: {e}")

################################################################################
# 8. Clases Anidadas
################################################################################

class Exterior:
    """Clase exterior que contiene una clase anidada."""
    
    def __init__(self, valor):
        self.valor = valor
        # Crear una instancia de la clase anidada
        self.interno = self.Interno(self)
    
    def metodo_exterior(self):
        return f"Método de la clase exterior, valor: {self.valor}"
    
    # Clase anidada
    class Interno:
        """Clase anidada dentro de Exterior."""
        
        def __init__(self, exterior):
            self.exterior = exterior
        
        def metodo_interno(self):
            return f"Método de la clase interna, valor exterior: {self.exterior.valor}"

# Usar clases anidadas
ext = Exterior(10)
print(f"\nDesde la clase exterior: {ext.metodo_exterior()}")
print(f"Desde la clase interna: {ext.interno.metodo_interno()}")

# También se puede acceder directamente a la clase interna
interno_directo = Exterior.Interno(ext)
print(f"Desde instancia directa de la clase interna: {interno_directo.metodo_interno()}")

################################################################################
# 9. Conclusiones
################################################################################

'''
Puntos clave sobre las clases en Python:

1. Las clases son plantillas para crear objetos (instancias).

2. Componentes principales:
   - Atributos de clase: Compartidos por todas las instancias
   - Atributos de instancia: Específicos de cada objeto
   - Métodos: Funciones que definen el comportamiento

3. Tipos de métodos:
   - Métodos de instancia: Operan sobre una instancia específica (self)
   - Métodos de clase: Operan sobre la clase (@classmethod)
   - Métodos estáticos: No dependen de la clase ni de instancias (@staticmethod)

4. Encapsulamiento:
   - Atributos/métodos públicos: Sin prefijo especial
   - Atributos/métodos "protegidos": Prefijo _ (convención)
   - Atributos/métodos "privados": Prefijo __ (name mangling)

5. Métodos especiales (dunder methods):
   - Permiten personalizar el comportamiento de operadores y funciones integradas
   - Ejemplos: __init__, __str__, __repr__, __add__, __eq__, etc.

6. Propiedades:
   - Permiten acceder a atributos mediante métodos getter/setter
   - Facilitan la validación y el cálculo de valores derivados

7. Herencia vs Composición:
   - Herencia: "es un" (subclase hereda de superclase)
   - Composición: "tiene un" (clase contiene instancias de otras clases)

Las clases son fundamentales en la POO y permiten crear código modular,
reutilizable y fácil de mantener.
'''

print("\n--- Fin de la exploración de clases en Python ---")