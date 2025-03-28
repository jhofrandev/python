################################################################################
# Profundizando en la Herencia en Python
################################################################################

'''
La herencia es un mecanismo que permite crear nuevas clases a partir de clases existentes.
La nueva clase (subclase) hereda atributos y métodos de la clase base (superclase),
permitiendo la reutilización de código y la creación de jerarquías de clases.

Ventajas de la herencia:
- Reutilización de código
- Extensibilidad
- Polimorfismo
- Organización jerárquica
'''

################################################################################
# 1. Herencia Básica
################################################################################

class Animal:
    """Clase base para todos los animales."""
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def comer(self):
        return f"{self.nombre} está comiendo."
    
    def dormir(self):
        return f"{self.nombre} está durmiendo."
    
    def describir(self):
        return f"{self.nombre} es un animal de {self.edad} años."

# Subclase que hereda de Animal
class Perro(Animal):
    """Clase que representa a un perro, hereda de Animal."""
    
    def __init__(self, nombre, edad, raza):
        # Llamar al constructor de la clase base
        super().__init__(nombre, edad)
        # Añadir atributos específicos de Perro
        self.raza = raza
    
    # Método específico de Perro
    def ladrar(self):
        return f"{self.nombre} dice: ¡Guau!"
    
    # Sobrescribir un método de la clase base
    def describir(self):
        return f"{self.nombre} es un perro de raza {self.raza} y tiene {self.edad} años."

# Otra subclase que hereda de Animal
class Gato(Animal):
    """Clase que representa a un gato, hereda de Animal."""
    
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color
    
    def maullar(self):
        return f"{self.nombre} dice: ¡Miau!"
    
    def describir(self):
        return f"{self.nombre} es un gato de color {self.color} y tiene {self.edad} años."

# Crear instancias
animal = Animal("Genérico", 5)
perro = Perro("Rex", 3, "Pastor Alemán")
gato = Gato("Whiskers", 2, "naranja")

# Usar métodos heredados
print(animal.comer())
print(perro.comer())  # Método heredado de Animal
print(gato.dormir())  # Método heredado de Animal

# Usar métodos específicos
print(perro.ladrar())
print(gato.maullar())

# Usar métodos sobrescritos
print(animal.describir())
print(perro.describir())
print(gato.describir())

# Verificar relaciones de herencia
print(f"\n¿perro es instancia de Perro? {isinstance(perro, Perro)}")
print(f"¿perro es instancia de Animal? {isinstance(perro, Animal)}")
print(f"¿animal es instancia de Perro? {isinstance(animal, Perro)}")
print(f"¿Perro es subclase de Animal? {issubclass(Perro, Animal)}")

################################################################################
# 2. Herencia Múltiple
################################################################################

class Volador:
    """Clase que proporciona capacidades de vuelo."""
    
    def volar(self):
        return f"{self.nombre} está volando."
    
    def aterrizar(self):
        return f"{self.nombre} está aterrizando."

class Nadador:
    """Clase que proporciona capacidades de natación."""
    
    def nadar(self):
        return f"{self.nombre} está nadando."
    
    def bucear(self):
        return f"{self.nombre} está buceando."
    
    def aterrizar(self):
        return f"{self.nombre} está saliendo del agua."

# Herencia múltiple
class Pato(Animal, Volador, Nadador):
    """Clase que representa a un pato, hereda de Animal, Volador y Nadador."""
    
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    
    def graznar(self):
        return f"{self.nombre} dice: ¡Cuac!"
    
    # Este método resolverá el conflicto entre Volador.aterrizar y Nadador.aterrizar
    def aterrizar(self):
        return f"{self.nombre} está aterrizando en el agua."

# Crear un pato
pato = Pato("Donald", 3)

# Usar métodos de todas las clases base
print(f"\n{pato.comer()}")  # De Animal
print(pato.volar())  # De Volador
print(pato.nadar())  # De Nadador
print(pato.graznar())  # De Pato
print(pato.aterrizar())  # De Pato (sobrescribe a Volador y Nadador)

# Orden de Resolución de Métodos (MRO)
print(f"\nMRO de Pato: {[cls.__name__ for cls in Pato.__mro__]}")

################################################################################
# 3. Herencia Multinivel
################################################################################

class Vehiculo:
    """Clase base para todos los vehículos."""
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def arrancar(self):
        return f"{self.marca} {self.modelo} está arrancando."
    
    def detener(self):
        return f"{self.marca} {self.modelo} se ha detenido."
    
    def __str__(self):
        return f"{self.marca} {self.modelo}"

class Automovil(Vehiculo):
    """Clase que representa un automóvil, hereda de Vehículo."""
    
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas
    
    def tocar_claxon(self):
        return f"{self.marca} {self.modelo} está tocando el claxon."
    
    def __str__(self):
        return f"Automóvil {self.marca} {self.modelo} de {self.puertas} puertas"

class Deportivo(Automovil):
    """Clase que representa un automóvil deportivo, hereda de Automóvil."""
    
    def __init__(self, marca, modelo, puertas, velocidad_maxima):
        super().__init__(marca, modelo, puertas)
        self.velocidad_maxima = velocidad_maxima
    
    def modo_sport(self):
        return f"{self.marca} {self.modelo} ha activado el modo deportivo."
    
    def __str__(self):
        return f"Deportivo {self.marca} {self.modelo} con velocidad máxima de {self.velocidad_maxima} km/h"

# Crear instancias
vehiculo = Vehiculo("Genérico", "Base")
auto = Automovil("Toyota", "Corolla", 4)
deportivo = Deportivo("Ferrari", "F8", 2, 340)

# Usar métodos en diferentes niveles
print(f"\n{vehiculo.arrancar()}")
print(auto.arrancar())  # Heredado de Vehiculo
print(auto.tocar_claxon())
print(deportivo.arrancar())  # Heredado de Vehiculo a través de Automovil
print(deportivo.tocar_claxon())  # Heredado de Automovil
print(deportivo.modo_sport())

# Representación en cadena
print(f"\n{vehiculo}")
print(auto)
print(deportivo)

# Verificar relaciones
print(f"\n¿deportivo es instancia de Deportivo? {isinstance(deportivo, Deportivo)}")
print(f"¿deportivo es instancia de Automovil? {isinstance(deportivo, Automovil)}")
print(f"¿deportivo es instancia de Vehiculo? {isinstance(deportivo, Vehiculo)}")

################################################################################
# 4. Herencia y Constructores
################################################################################

class Persona:
    """Clase base para representar personas."""
    
    def __init__(self, nombre, edad):
        print("Constructor de Persona llamado")
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"{self.nombre}, {self.edad} años"

class Empleado(Persona):
    """Clase que representa a un empleado."""
    
    def __init__(self, nombre, edad, id_empleado, salario):
        print("Constructor de Empleado llamado")
        # Llamar al constructor de la clase base
        super().__init__(nombre, edad)
        # Inicializar atributos propios
        self.id_empleado = id_empleado
        self.salario = salario
    
    def __str__(self):
        return f"Empleado: {super().__str__()}, ID: {self.id_empleado}, Salario: ${self.salario}"

class Gerente(Empleado):
    """Clase que representa a un gerente."""
    
    def __init__(self, nombre, edad, id_empleado, salario, departamento):
        print("Constructor de Gerente llamado")
        # Llamar al constructor de la clase base
        super().__init__(nombre, edad, id_empleado, salario)
        # Inicializar atributos propios
        self.departamento = departamento
    
    def __str__(self):
        return f"Gerente: {self.nombre}, {self.edad} años, ID: {self.id_empleado}, Departamento: {self.departamento}"

# Crear instancias
print("\nCreando una persona:")
persona = Persona("Juan", 30)

print("\nCreando un empleado:")
empleado = Empleado("Ana", 25, "E12345", 50000)

print("\nCreando un gerente:")
gerente = Gerente("Carlos", 40, "G98765", 80000, "Tecnología")

# Mostrar información
print(f"\n{persona}")
print(empleado)
print(gerente)

################################################################################
# 5. Herencia y Métodos Privados/Protegidos
################################################################################

class Base:
    """Clase base para demostrar visibilidad de métodos y atributos."""
    
    def __init__(self):
        self.publico = "Atributo público"
        self._protegido = "Atributo protegido"
        self.__privado = "Atributo privado"
    
    def metodo_publico(self):
        return "Método público"
    
    def _metodo_protegido(self):
        return "Método protegido"
    
    def __metodo_privado(self):
        return "Método privado"
    
    def acceder_privado(self):
        """Método público que accede a miembros privados."""
        return f"Accediendo a: {self.__privado} y {self.__metodo_privado()}"

class Derivada(Base):
    """Clase derivada para demostrar herencia y visibilidad."""
    
    def __init__(self):
        super().__init__()
        # Podemos acceder a miembros públicos y protegidos
        self.desde_derivada_publico = self.publico
        self.desde_derivada_protegido = self._protegido
        # No podemos acceder directamente a miembros privados
        # self.desde_derivada_privado = self.__privado  # Esto causaría un error
    
    def mostrar_acceso(self):
        """Muestra a qué miembros podemos acceder."""
        return f"""
        Desde Derivada:
        - Público: {self.publico}
        - Protegido: {self._protegido}
        - Método público: {self.metodo_publico()}
        - Método protegido: {self._metodo_protegido()}
        - Acceso a privado a través de método público: {self.acceder_privado()}
        """

# Crear instancias
base = Base()
derivada = Derivada()

# Acceso desde fuera de las clases
print("\nAcceso desde fuera de las clases:")
print(f"Base - Público: {base.publico}")
print(f"Base - Protegido (no recomendado): {base._protegido}")
print(f"Base - Método público: {base.metodo_publico()}")
print(f"Base - Método protegido (no recomendado): {base._metodo_protegido()}")
print(f"Base - Acceso a privado a través de método público: {base.acceder_privado()}")

# Intentar acceder a miembros privados
try:
    print(base.__privado)
except AttributeError as e:
    print(f"Error al acceder a atributo privado: {e}")

try:
    print(base.__metodo_privado())
except AttributeError as e:
    print(f"Error al llamar método privado: {e}")

# Acceso desde la clase derivada
print(derivada.mostrar_acceso())

################################################################################
# 6. Polimorfismo a través de Herencia
################################################################################

class Figura:
    """Clase base para figuras geométricas."""
    
    def area(self):
        """Calcula el área de la figura."""
        raise NotImplementedError("Las subclases deben implementar este método")
    
    def perimetro(self):
        """Calcula el perímetro de la figura."""
        raise NotImplementedError("Las subclases deben implementar este método")
    
    def describir(self):
        """Describe la figura."""
        return "Esta es una figura geométrica"

class Rectangulo(Figura):
    """Clase que representa un rectángulo."""
    
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto
    
    def perimetro(self):
        return 2 * (self.ancho + self.alto)
    
    def describir(self):
        return f"Rectángulo de {self.ancho}x{self.alto}"

class Circulo(Figura):
    """Clase que representa un círculo."""
    
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        import math
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        import math
        return 2 * math.pi * self.radio
    
    def describir(self):
        return f"Círculo de radio {self.radio}"

class Triangulo(Figura):
    """Clase que representa un triángulo."""
    
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def area(self):
        # Fórmula de Herón
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        import math
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
    
    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    
    def describir(self):
        return f"Triángulo con lados {self.lado1}, {self.lado2} y {self.lado3}"

# Función que trabaja con cualquier figura
def mostrar_informacion_figura(figura):
    """Muestra información de cualquier figura."""
    print(f"Descripción: {figura.describir()}")
    print(f"Área: {figura.area():.2f}")
    print(f"Perímetro: {figura.perimetro():.2f}")
    print()

# Crear figuras
rectangulo = Rectangulo(5, 3)
circulo = Circulo(4)
triangulo = Triangulo(3, 4, 5)

# Usar polimorfismo
print("\nInformación de figuras:")
mostrar_informacion_figura(rectangulo)
mostrar_informacion_figura(circulo)
mostrar_informacion_figura(triangulo)

# Lista de figuras (polimorfismo)
figuras = [rectangulo, circulo, triangulo]
print("Áreas de todas las figuras:")
for i, figura in enumerate(figuras, 1):
    print(f"Figura {i}: {figura.area():.2f}")

################################################################################
# 7. Herencia y super()
################################################################################

class A:
    def metodo(self):
        return "Método de A"

class B(A):
    def metodo(self):
        return f"Método de B, llamando a A: {super().metodo()}"

class C(A):
    def metodo(self):
        return f"Método de C, llamando a A: {super().metodo()}"

class D(B, C):
    def metodo(self):
        return f"Método de D, llamando a B y C: {super().metodo()}"

# Crear instancia
d = D()

# Ver MRO
print(f"\nMRO de D: {[cls.__name__ for cls in D.__mro__]}")

# Llamar al método
print(f"Resultado de d.metodo(): {d.metodo()}")

################################################################################
# 8. Clases Abstractas
################################################################################

from abc import ABC, abstractmethod

class InstrumentoMusical(ABC):
    """Clase abstracta para instrumentos musicales."""
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    @abstractmethod
    def tocar(self):
        """Método abstracto que debe ser implementado por las subclases."""
        pass
    
    @abstractmethod
    def afinar(self):
        """Método abstracto que debe ser implementado por las subclases."""
        pass
    
    def describir(self):
        """Método concreto que pueden usar las subclases."""
        return f"Este es un {self.nombre}"

class Guitarra(InstrumentoMusical):
    """Clase que representa una guitarra."""
    
    def __init__(self, nombre, num_cuerdas):
        super().__init__(nombre)
        self.num_cuerdas = num_cuerdas
    
    def tocar(self):
        return f"Tocando {self.nombre} de {self.num_cuerdas} cuerdas"
    
    def afinar(self):
        return f"Afinando {self.nombre}"
    
    def rasguear(self):
        return f"Rasgueando {self.nombre}"

class Piano(InstrumentoMusical):
    """Clase que representa un piano."""
    
    def __init__(self, nombre, tipo):
        super().__init__(nombre)
        self.tipo = tipo
    
    def tocar(self):
        return f"Tocando {self.nombre} {self.tipo}"
    
    def afinar(self):
        return f"Afinando {self.nombre} {self.tipo}"
    
    def presionar_tecla(self, tecla):
        return f"Presionando la tecla {tecla} en el {self.nombre}"

# Intentar instanciar una clase abstracta
try:
    instrumento = InstrumentoMusical("Genérico")
except TypeError as e:
    print(f"\nError al instanciar clase abstracta: {e}")

# Crear instancias de clases concretas
guitarra = Guitarra("Guitarra acústica", 6)
piano = Piano("Piano", "de cola")

# Usar métodos
print(guitarra.describir())  # Método heredado
print(guitarra.tocar())  # Método implementado
print(guitarra.rasguear())  # Método específico

print(piano.describir())  # Método heredado
print(piano.tocar())  # Método implementado
print(piano.presionar_tecla("Do"))  # Método específico

################################################################################
# 9. Herencia y Composición: ¿Cuándo usar cada una?
################################################################################

'''
Herencia vs Composición:

1. Herencia ("es un"):
   - Usar cuando existe una relación "es un" clara
   - Ejemplo: Un perro es un animal

2. Composición ("tiene un"):
   - Usar cuando existe una relación "tiene un"
   - Ejemplo: Un coche tiene un motor

Regla general: "Favorece la composición sobre la herencia"
'''

# Ejemplo de herencia (relación "es un")
class Empleado2:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    
    def trabajar(self):
        return f"{self.nombre} está trabajando"

class Programador(Empleado2):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje
    
    def programar(self):
        return f"{self.nombre} está programando en {self.lenguaje}"

# Ejemplo de composición (relación "tiene un")
class Motor2:
    def __init__(self, tipo):
        self.tipo = tipo
    
    def arrancar(self):
        return f"Motor de {self.tipo} arrancado"
    
    def detener(self):
        return f"Motor de {self.tipo} detenido"

class Coche2:
    def __init__(self, marca, modelo, tipo_motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor2(tipo_motor)  # Composición
    
    def conducir(self):
        return f"Conduciendo {self.marca} {self.modelo}"
    
    def arrancar(self):
        return f"{self.marca} {self.modelo}: {self.motor.arrancar()}"

# Usar herencia
programador = Programador("Ana", 60000, "Python")
print(f"\n{programador.trabajar()}")  # Método heredado
print(programador.programar())  # Método específico

# Usar composición
coche = Coche2("Toyota", "Corolla", "gasolina")
print(coche.conducir())  # Método propio
print(coche.arrancar())  # Delega al componente

################################################################################
# 10. Conclusiones sobre Herencia
################################################################################

'''
Conclusiones sobre Herencia en Python:

1. La herencia permite crear jerarquías de clases y reutilizar código.

2. Python soporta:
   - Herencia simple
   - Herencia múltiple
   - Herencia multinivel

3. Mecanismos importantes:
   - super() para llamar a métodos de la clase base
   - Método Resolution Order (MRO) para resolver conflictos en herencia múltiple
   - Clases abstractas para definir interfaces

4. Mejores prácticas:
   - Usar herencia para relaciones "es un"
   - Preferir composición sobre herencia cuando sea posible
   - Mantener jerarquías de herencia simples y poco profundas
   - Documentar claramente la intención de las clases base
   - Usar clases abstractas para definir interfaces comunes

5. Consideraciones:
   - La herencia múltiple debe usarse con cuidado
   - Los atributos privados (__nombre) no se heredan directamente
   - El polimorfismo permite tratar objetos de diferentes clases de manera uniforme

La herencia es una herramienta poderosa, pero debe usarse juiciosamente.
'''

print("\n--- Fin de la exploración de herencia en Python ---")