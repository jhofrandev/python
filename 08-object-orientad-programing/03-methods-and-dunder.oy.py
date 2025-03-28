################################################################################
# Profundizando en Métodos y Dunder Methods en Python
################################################################################

'''
Los métodos son funciones definidas dentro de una clase que describen
el comportamiento de los objetos. Los "dunder methods" (double underscore methods)
son métodos especiales con nombres que comienzan y terminan con doble guion bajo,
que permiten a las clases interactuar con las funcionalidades incorporadas de Python.
'''

################################################################################
# 1. Tipos de Métodos en Python
################################################################################

class Calculadora:
    """Clase que demuestra los diferentes tipos de métodos en Python."""
    
    # Atributo de clase
    nombre = "Calculadora Básica"
    
    def __init__(self, marca="Genérica"):
        """Constructor (método de instancia)."""
        self.marca = marca
        self.ultimo_resultado = 0
    
    # Método de instancia
    def sumar(self, a, b):
        """Método de instancia que suma dos números."""
        self.ultimo_resultado = a + b
        return self.ultimo_resultado
    
    def restar(self, a, b):
        """Método de instancia que resta dos números."""
        self.ultimo_resultado = a - b
        return self.ultimo_resultado
    
    # Método de clase
    @classmethod
    def cambiar_nombre(cls, nuevo_nombre):
        """
        Método de clase que cambia el nombre de la calculadora.
        
        Actúa sobre la clase, no sobre instancias específicas.
        """
        cls.nombre = nuevo_nombre
        return f"Nombre cambiado a: {cls.nombre}"
    
    @classmethod
    def crear_cientifica(cls):
        """
        Método de clase que crea una instancia con marca predefinida.
        
        Funciona como un constructor alternativo.
        """
        return cls("Científica")
    
    # Método estático
    @staticmethod
    def es_par(numero):
        """
        Método estático que verifica si un número es par.
        
        No depende del estado de la clase ni de instancias.
        """
        return numero % 2 == 0
    
    @staticmethod
    def convertir_a_binario(numero):
        """Método estático que convierte un número a binario."""
        return bin(numero)

# Crear instancias
calc1 = Calculadora()
calc2 = Calculadora("Premium")

# Usar métodos de instancia
print(f"Suma: {calc1.sumar(5, 3)}")
print(f"Resta: {calc1.restar(10, 4)}")
print(f"Último resultado: {calc1.ultimo_resultado}")

# Usar métodos de clase
print(f"Nombre original: {Calculadora.nombre}")
print(Calculadora.cambiar_nombre("Super Calculadora"))
print(f"Nuevo nombre (desde clase): {Calculadora.nombre}")
print(f"Nuevo nombre (desde instancia): {calc1.nombre}")

# Crear instancia usando método de clase
calc_cientifica = Calculadora.crear_cientifica()
print(f"Calculadora científica: {calc_cientifica.marca}")

# Usar métodos estáticos
print(f"¿Es par 7? {Calculadora.es_par(7)}")
print(f"¿Es par 8? {calc1.es_par(8)}")  # También se puede llamar desde una instancia
print(f"10 en binario: {Calculadora.convertir_a_binario(10)}")

################################################################################
# 2. Dunder Methods: Inicialización y Representación
################################################################################

class Persona:
    """Clase que demuestra métodos dunder de inicialización y representación."""
    
    def __init__(self, nombre, edad):
        """
        Inicializa una nueva instancia de Persona.
        
        Este método se llama automáticamente al crear un objeto.
        """
        self.nombre = nombre
        self.edad = edad
        print(f"Se ha creado una persona: {nombre}")
    
    def __str__(self):
        """
        Retorna una representación en cadena para usuarios.
        
        Este método se llama cuando se usa str() o print().
        """
        return f"{self.nombre}, {self.edad} años"
    
    def __repr__(self):
        """
        Retorna una representación en cadena para desarrolladores.
        
        Este método se llama cuando se muestra el objeto en el intérprete
        o cuando se usa repr().
        """
        return f"Persona('{self.nombre}', {self.edad})"
    
    def __del__(self):
        """
        Método llamado cuando el objeto está a punto de ser destruido.
        
        Útil para liberar recursos, aunque en Python no se usa mucho
        debido al recolector de basura.
        """
        print(f"Eliminando a {self.nombre}")

# Crear instancia
persona = Persona("Ana", 30)

# Usar representaciones
print(f"str(persona): {str(persona)}")
print(f"repr(persona): {repr(persona)}")

# La representación str se usa automáticamente con print
print(f"print(persona): {persona}")

# La representación repr se usa en el intérprete
print(f"Representación en el intérprete: {persona!r}")

################################################################################
# 3. Dunder Methods: Operadores Matemáticos
################################################################################

class Vector2D:
    """Clase que representa un vector 2D con soporte para operadores matemáticos."""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    # Operadores aritméticos
    def __add__(self, otro):
        """Implementa el operador + (suma)."""
        if isinstance(otro, Vector2D):
            return Vector2D(self.x + otro.x, self.y + otro.y)
        return NotImplemented
    
    def __sub__(self, otro):
        """Implementa el operador - (resta)."""
        if isinstance(otro, Vector2D):
            return Vector2D(self.x - otro.x, self.y - otro.y)
        return NotImplemented
    
    def __mul__(self, otro):
        """
        Implementa el operador * (multiplicación).
        
        Permite multiplicar por un escalar o calcular el producto punto con otro vector.
        """
        if isinstance(otro, (int, float)):
            # Multiplicación por escalar
            return Vector2D(self.x * otro, self.y * otro)
        elif isinstance(otro, Vector2D):
            # Producto punto
            return self.x * otro.x + self.y * otro.y
        return NotImplemented
    
    def __rmul__(self, otro):
        """
        Implementa el operador * cuando el vector está a la derecha.
        
        Permite expresiones como: 2 * vector
        """
        return self.__mul__(otro)
    
    def __neg__(self):
        """Implementa el operador unario - (negación)."""
        return Vector2D(-self.x, -self.y)
    
    def __abs__(self):
        """
        Implementa la función abs().
        
        Retorna la magnitud (longitud) del vector.
        """
        import math
        return math.sqrt(self.x**2 + self.y**2)
    
    # Operadores de comparación
    def __eq__(self, otro):
        """Implementa el operador == (igualdad)."""
        if not isinstance(otro, Vector2D):
            return NotImplemented
        return self.x == otro.x and self.y == otro.y
    
    def __lt__(self, otro):
        """
        Implementa el operador < (menor que).
        
        Compara basándose en la magnitud del vector.
        """
        if not isinstance(otro, Vector2D):
            return NotImplemented
        return abs(self) < abs(otro)

# Crear vectores
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

# Usar operadores
print(f"\nVector v1: {v1}")
print(f"Vector v2: {v2}")

# Suma y resta
v3 = v1 + v2
print(f"v1 + v2 = {v3}")

v4 = v1 - v2
print(f"v1 - v2 = {v4}")

# Multiplicación
v5 = v1 * 2
print(f"v1 * 2 = {v5}")

v6 = 3 * v1  # Usa __rmul__
print(f"3 * v1 = {v6}")

# Producto punto
producto_punto = v1 * v2
print(f"v1 · v2 (producto punto) = {producto_punto}")

# Negación
v7 = -v1
print(f"-v1 = {v7}")

# Magnitud
print(f"Magnitud de v1: {abs(v1)}")

# Comparaciones
print(f"¿v1 == v2? {v1 == v2}")
print(f"¿v1 == Vector2D(3, 4)? {v1 == Vector2D(3, 4)}")
print(f"¿v1 < v2? {v1 < v2}")
print(f"¿v2 < v1? {v2 < v1}")

################################################################################
# 4. Dunder Methods: Contenedores y Secuencias
################################################################################

class ListaPersonalizada:
    """Clase que implementa una lista personalizada usando dunder methods."""
    
    def __init__(self, elementos=None):
        self.elementos = elementos if elementos is not None else []
    
    def __str__(self):
        return str(self.elementos)
    
    # Métodos para comportarse como contenedor
    def __len__(self):
        """
        Implementa la función len().
        
        Permite usar len(objeto).
        """
        return len(self.elementos)
    
    def __getitem__(self, indice):
        """
        Implementa el acceso por índice.
        
        Permite usar objeto[indice].
        """
        return self.elementos[indice]
    
    def __setitem__(self, indice, valor):
        """
        Implementa la asignación por índice.
        
        Permite usar objeto[indice] = valor.
        """
        self.elementos[indice] = valor
    
    def __delitem__(self, indice):
        """
        Implementa la eliminación por índice.
        
        Permite usar del objeto[indice].
        """
        del self.elementos[indice]
    
    def __contains__(self, item):
        """
        Implementa el operador in.
        
        Permite usar item in objeto.
        """
        return item in self.elementos
    
    # Métodos para comportarse como iterable
    def __iter__(self):
        """
        Implementa la iteración.
        
        Permite usar for item in objeto.
        """
        return iter(self.elementos)
    
    def __reversed__(self):
        """
        Implementa la función reversed().
        
        Permite usar reversed(objeto).
        """
        return reversed(self.elementos)

# Crear lista personalizada
lista = ListaPersonalizada([1, 2, 3, 4, 5])

# Usar métodos de contenedor
print(f"\nLista: {lista}")
print(f"Longitud: {len(lista)}")
print(f"Elemento en índice 2: {lista[2]}")

# Modificar elemento
lista[1] = 20
print(f"Después de modificar: {lista}")

# Eliminar elemento
del lista[0]
print(f"Después de eliminar: {lista}")

# Verificar pertenencia
print(f"¿3 está en la lista? {3 in lista}")
print(f"¿10 está en la lista? {10 in lista}")

# Iterar
print("Elementos de la lista:", end=" ")
for elemento in lista:
    print(elemento, end=" ")
print()

# Iterar en reversa
print("Elementos en reversa:", end=" ")
for elemento in reversed(lista):
    print(elemento, end=" ")
print()

################################################################################
# 5. Dunder Methods: Llamadas y Contextos
################################################################################

class Contador:
    """Clase que implementa un objeto llamable y un gestor de contexto."""
    
    def __init__(self, inicio=0):
        self.valor = inicio
    
    def __call__(self, incremento=1):
        """
        Hace que el objeto sea llamable como una función.
        
        Permite usar objeto() para incrementar el contador.
        """
        self.valor += incremento
        return self.valor
    
    def __enter__(self):
        """
        Método llamado al entrar en un bloque with.
        
        Parte del protocolo de gestor de contexto.
        """
        print(f"Entrando al contexto. Valor inicial: {self.valor}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Método llamado al salir de un bloque with.
        
        Parte del protocolo de gestor de contexto.
        """
        print(f"Saliendo del contexto. Valor final: {self.valor}")
        # Retornar False permite que las excepciones se propaguen
        # Retornar True las suprime
        return False

# Usar objeto como función (callable)
contador = Contador(10)
print(f"\nValor inicial: {contador.valor}")
print(f"Después de llamar: {contador()}")
print(f"Incrementar en 5: {contador(5)}")

# Usar como gestor de contexto
with Contador(100) as c:
    print(f"Dentro del contexto. Valor: {c.valor}")
    c(10)  # Incrementar
    print(f"Después de incrementar: {c.valor}")
    # Al salir del bloque with, se llama a __exit__

################################################################################
# 6. Dunder Methods: Atributos y Descriptores
################################################################################

class Temperatura:
    """Clase que demuestra el uso de __getattr__, __setattr__ y __delattr__."""
    
    def __init__(self, celsius=0):
        # Usamos el método __dict__ directamente para evitar llamar a __setattr__
        self.__dict__['_celsius'] = celsius
    
    def __getattr__(self, nombre):
        """
        Llamado cuando se accede a un atributo que no existe.
        
        Permite manejar atributos dinámicos.
        """
        if nombre == 'fahrenheit':
            return self._celsius * 9/5 + 32
        elif nombre == 'kelvin':
            return self._celsius + 273.15
        raise AttributeError(f"'{type(self).__name__}' no tiene atributo '{nombre}'")
    
    def __setattr__(self, nombre, valor):
        """
        Llamado cuando se asigna un valor a un atributo.
        
        Permite validar o transformar valores antes de asignarlos.
        """
        if nombre == 'celsius':
            if valor < -273.15:
                raise ValueError("La temperatura no puede ser menor que el cero absoluto")
            self.__dict__['_celsius'] = valor
        elif nombre == 'fahrenheit':
            self.__dict__['_celsius'] = (valor - 32) * 5/9
        elif nombre == 'kelvin':
            if valor < 0:
                raise ValueError("La temperatura en Kelvin no puede ser negativa")
            self.__dict__['_celsius'] = valor - 273.15
        else:
            self.__dict__[nombre] = valor
    
    def __delattr__(self, nombre):
        """
        Llamado cuando se elimina un atributo.
        
        Permite controlar qué atributos pueden eliminarse.
        """
        if nombre in ('_celsius', 'celsius', 'fahrenheit', 'kelvin'):
            raise AttributeError(f"No se puede eliminar el atributo '{nombre}'")
        super().__delattr__(nombre)
    
    # Propiedad para acceder a celsius directamente
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("La temperatura no puede ser menor que el cero absoluto")
        self._celsius = valor

# Crear objeto
temp = Temperatura(25)
print(f"\nTemperatura en Celsius: {temp.celsius}")
print(f"Temperatura en Fahrenheit: {temp.fahrenheit}")
print(f"Temperatura en Kelvin: {temp.kelvin}")

# Modificar temperatura
temp.celsius = 30
print(f"Después de cambiar Celsius: {temp.celsius}°C, {temp.fahrenheit}°F")

temp.fahrenheit = 68
print(f"Después de cambiar Fahrenheit: {temp.celsius}°C, {temp.fahrenheit}°F")

# Añadir atributo personalizado
temp.unidad_preferida = "Celsius"
print(f"Unidad preferida: {temp.unidad_preferida}")

# Intentar eliminar atributo protegido
try:
    del temp.celsius
except AttributeError as e:
    print(f"Error: {e}")

# Eliminar atributo personalizado
del temp.unidad_preferida
try:
    print(temp.unidad_preferida)
except AttributeError as e:
    print(f"Error: {e}")

################################################################################
# 7. Descriptores
################################################################################

class Validador:
    """
    Descriptor que valida valores según una función de validación.
    
    Los descriptores son objetos que definen cómo se accede a los atributos
    de otras clases mediante los métodos __get__, __set__ y __delete__.
    """
    
    def __init__(self, nombre, funcion_validacion, mensaje_error):
        self.nombre = nombre
        self.funcion_validacion = funcion_validacion
        self.mensaje_error = mensaje_error
    
    def __get__(self, instancia, propietario):
        """Obtiene el valor del atributo."""
        if instancia is None:
            return self
        return instancia.__dict__.get(self.nombre, None)
    
    def __set__(self, instancia, valor):
        """Establece el valor del atributo con validación."""
        if not self.funcion_validacion(valor):
            raise ValueError(self.mensaje_error)
        instancia.__dict__[self.nombre] = valor
    
    def __delete__(self, instancia):
        """Elimina el atributo."""
        if self.nombre in instancia.__dict__:
            del instancia.__dict__[self.nombre]

class Persona2:
    """Clase que usa descriptores para validar atributos."""
    
    nombre = Validador('nombre', lambda x: isinstance(x, str) and len(x) > 0, 
                      "El nombre debe ser una cadena no vacía")
    
    edad = Validador('edad', lambda x: isinstance(x, int) and 0 <= x <= 120,
                    "La edad debe ser un entero entre 0 y 120")
    
    email = Validador('email', lambda x: isinstance(x, str) and '@' in x,
                     "El email debe contener @")
    
    def __init__(self, nombre, edad, email):
        self.nombre = nombre
        self.edad = edad
        self.email = email
    
    def __str__(self):
        return f"Persona: {self.nombre}, {self.edad} años, {self.email}"

# Crear persona con valores válidos
persona2 = Persona2("Juan", 30, "juan@ejemplo.com")
print(f"\n{persona2}")

# Intentar asignar valores inválidos
try:
    persona2.nombre = ""  # Nombre vacío
except ValueError as e:
    print(f"Error al asignar nombre: {e}")

try:
    persona2.edad = 150  # Edad fuera de rango
except ValueError as e:
    print(f"Error al asignar edad: {e}")

try:
    persona2.email = "correo_invalido"  # Email sin @
except ValueError as e:
    print(f"Error al asignar email: {e}")

################################################################################
# 8. Métodos Mágicos Adicionales
################################################################################

class Fraccion:
    """Clase que representa una fracción con métodos mágicos adicionales."""
    
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero")
        
        # Simplificar la fracción
        mcd = self._mcd(abs(numerador), abs(denominador))
        self.numerador = numerador // mcd
        self.denominador = denominador // mcd
        
        # Asegurar que el signo esté en el numerador
        if self.denominador < 0:
            self.numerador = -self.numerador
            self.denominador = -self.denominador
    
    def _mcd(self, a, b):
        """Calcula el máximo común divisor usando el algoritmo de Euclides."""
        while b:
            a, b = b, a % b
        return a
    
    def __str__(self):
        if self.denominador == 1:
            return str(self.numerador)
        return f"{self.numerador}/{self.denominador}"
    
    def __repr__(self):
        return f"Fraccion({self.numerador}, {self.denominador})"
    
    # Operaciones aritméticas
    def __add__(self, otro):
        if isinstance(otro, int):
            otro = Fraccion(otro, 1)
        if not isinstance(otro, Fraccion):
            return NotImplemented
        
        nuevo_num = self.numerador * otro.denominador + otro.numerador * self.denominador
        nuevo_den = self.denominador * otro.denominador
        return Fraccion(nuevo_num, nuevo_den)
    
    def __radd__(self, otro):
        """Suma cuando la fracción está a la derecha."""
        return self.__add__(otro)
    
    def __sub__(self, otro):
        if isinstance(otro, int):
            otro = Fraccion(otro, 1)
        if not isinstance(otro, Fraccion):
            return NotImplemented
        
        nuevo_num = self.numerador * otro.denominador - otro.numerador * self.denominador
        nuevo_den = self.denominador * otro.denominador
        return Fraccion(nuevo_num, nuevo_den)
    
    def __mul__(self, otro):
        if isinstance(otro, int):
            otro = Fraccion(otro, 1)
        if not isinstance(otro, Fraccion):
            return NotImplemented
        
        return Fraccion(self.numerador * otro.numerador, self.denominador * otro.denominador)
    
    def __truediv__(self, otro):
        if isinstance(otro, int):
            otro = Fraccion(otro, 1)
        if not isinstance(otro, Fraccion):
            return NotImplemented
        
        return Fraccion(self.numerador * otro.denominador, self.denominador * otro.numerador)
    
    # Operaciones de comparación
    def __eq__(self, otro):
        if isinstance(otro, int):
            otro = Fraccion(otro, 1)
        if not isinstance(otro, Fraccion):
            return NotImplemented
        
        return (self.numerador == otro.numerador and 
                self.denominador == otro.denominador)
    
    def __lt__(self, otro):
        if isinstance(otro, int):
            otro = Fraccion(otro, 1)
        if not isinstance(otro, Fraccion):
            return NotImplemented
        
        return (self.numerador * otro.denominador < 
                otro.numerador * self.denominador)
    
    # Conversión a tipos numéricos
    def __float__(self):
        """Permite convertir la fracción a float."""
        return self.numerador / self.denominador
    
    def __int__(self):
        """Permite convertir la fracción a int."""
        return int(float(self))
    
    def __round__(self, ndigits=0):
        """Implementa la función round()."""
        return round(float(self), ndigits)
    
    # Métodos para operaciones con números complejos
    def __complex__(self):
        """Permite convertir la fracción a complex."""
        return complex(float(self), 0)
    
    # Métodos para operaciones bit a bit
    def __index__(self):
        """
        Permite usar la fracción como índice.
        
        También permite usar la fracción en operaciones bit a bit.
        """
        return int(self)

# Crear fracciones
f1 = Fraccion(1, 2)
f2 = Fraccion(3, 4)

print(f"\nFracción 1: {f1}")
print(f"Fracción 2: {f2}")

# Operaciones aritméticas
print(f"f1 + f2 = {f1 + f2}")
print(f"f1 - f2 = {f1 - f2}")
print(f"f1 * f2 = {f1 * f2}")
print(f"f1 / f2 = {f1 / f2}")

# Operaciones con enteros
print(f"f1 + 1 = {f1 + 1}")
print(f"2 + f1 = {2 + f1}")

# Comparaciones
print(f"¿f1 == f2? {f1 == f2}")
print(f"¿f1 < f2? {f1 < f2}")
print(f"¿f1 > f2? {f1 > f2}")

# Conversiones
print(f"float(f1) = {float(f1)}")
print(f"int(f1) = {int(f1)}")
print(f"round(f1, 2) = {round(f1, 2)}")
print(f"complex(f2) = {complex(f2)}")

# Usar como índice
lista_ejemplo = ["a", "b", "c", "d"]
print(f"lista_ejemplo[int(f1)] = {lista_ejemplo[int(f1)]}")

################################################################################
# 9. Conclusiones sobre Métodos y Dunder Methods
################################################################################

'''
Conclusiones sobre Métodos y Dunder Methods en Python:

1. Tipos de métodos:
   - Métodos de instancia: Operan sobre instancias específicas (self)
   - Métodos de clase: Operan sobre la clase (@classmethod)
   - Métodos estáticos: No dependen de la clase ni de instancias (@staticmethod)

2. Dunder methods (métodos mágicos):
   - Permiten que las clases interactúen con las funcionalidades incorporadas de Python
   - Hacen que los objetos se comporten como tipos integrados
   - Proporcionan una interfaz intuitiva para las operaciones

3. Categorías principales de dunder methods:
   - Inicialización y representación: __init__, __str__, __repr__
   - Operadores matemáticos: __add__, __sub__, __mul__, etc.
   - Contenedores y secuencias: __len__, __getitem__, __iter__, etc.
   - Llamadas y contextos: __call__, __enter__, __exit__
   - Atributos y descriptores: __getattr__, __setattr__, __get__, __set__

4. Beneficios de usar dunder methods:
   - Código más intuitivo y pythónico
   - Mejor integración con las funcionalidades del lenguaje
   - Mayor expresividad en las operaciones

5. Mejores prácticas:
   - Implementar __repr__ siempre que se implemente __str__
   - Devolver NotImplemented para operaciones no soportadas
   - Mantener la simetría en operadores (implementar __radd__ si se implementa __add__)
   - Usar descriptores para validación y comportamiento complejo de atributos
   - Documentar el comportamiento esperado de los métodos mágicos

Los métodos y dunder methods son herramientas poderosas que permiten crear
clases con comportamiento rico e intuitivo en Python.
'''

print("\n--- Fin de la exploración de métodos y dunder methods en Python ---")