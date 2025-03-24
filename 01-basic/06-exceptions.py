"""
  Las excepciones en Python son eventos que ocurren durante la ejecución de un programa
  que interrumpen el flujo normal de las instrucciones. El manejo adecuado de excepciones
  es fundamental para crear programas robustos.
"""

################################################################################
## Tipos comunes de excepciones
################################################################################

# Python tiene muchos tipos de excepciones predefinidas:

# SyntaxError: Error en la sintaxis del código
# print("Hola"  # Falta un paréntesis de cierre

# NameError: Cuando se intenta usar una variable no definida
try:
    print(variable_no_definida)
except NameError as e:
    print(f"Error de nombre: {e}")

# TypeError: Operación aplicada a un objeto de tipo inapropiado
try:
    resultado = "5" + 5
except TypeError as e:
    print(f"Error de tipo: {e}")

# ValueError: Argumento correcto de tipo pero valor inapropiado
try:
    numero = int("abc")
except ValueError as e:
    print(f"Error de valor: {e}")

# IndexError: Índice fuera de rango
try:
    lista = [1, 2, 3]
    print(lista[10])
except IndexError as e:
    print(f"Error de índice: {e}")

# KeyError: Clave no encontrada en un diccionario
try:
    diccionario = {"a": 1, "b": 2}
    print(diccionario["c"])
except KeyError as e:
    print(f"Error de clave: {e}")

# ZeroDivisionError: División por cero
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"Error de división: {e}")

# FileNotFoundError: Archivo no encontrado
try:
    archivo = open("archivo_inexistente.txt", "r")
except FileNotFoundError as e:
    print(f"Error de archivo: {e}")

################################################################################
## Estructura básica try-except
################################################################################

# La estructura básica para manejar excepciones es try-except
try:
    # Código que puede generar una excepción
    resultado = 10 / 0
except ZeroDivisionError:
    # Código que se ejecuta si ocurre la excepción
    print("¡Error! División por cero.")

# Capturando múltiples excepciones
try:
    numero = int(input("Ingrese un número: "))
    resultado = 10 / numero
except ValueError:
    print("Error: Debe ingresar un número válido.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")

# Capturando múltiples excepciones en un solo bloque
try:
    # Algún código que puede generar diferentes excepciones
    pass
except (ValueError, TypeError, ZeroDivisionError) as e:
    print(f"Se produjo un error: {e}")

################################################################################
## Cláusulas adicionales: else y finally
################################################################################

# else: Se ejecuta si no ocurre ninguna excepción en el bloque try
try:
    numero = int("10")
except ValueError:
    print("No es un número válido")
else:
    print(f"Conversión exitosa: {numero}")

# finally: Se ejecuta siempre, haya ocurrido o no una excepción
try:
    archivo = open("ejemplo.txt", "w")
    archivo.write("Hola mundo")
except IOError:
    print("Error al escribir en el archivo")
finally:
    # Este bloque se ejecuta siempre
    archivo.close()
    print("Archivo cerrado")

################################################################################
## Lanzar excepciones con raise
################################################################################

# Podemos lanzar excepciones manualmente con la instrucción raise
def verificar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    if edad < 18:
        raise ValueError("Debe ser mayor de edad")
    return "Edad válida"

# Uso de la función con manejo de excepciones
try:
    resultado = verificar_edad(-5)
except ValueError as e:
    print(f"Error: {e}")

################################################################################
## Creando excepciones personalizadas
################################################################################

# Podemos crear nuestras propias clases de excepciones
class ErrorSaldoInsuficiente(Exception):
    """Excepción lanzada cuando no hay saldo suficiente en una cuenta."""
    def __init__(self, saldo, cantidad):
        self.saldo = saldo
        self.cantidad = cantidad
        self.mensaje = f"Saldo insuficiente: {saldo}. Intentó retirar: {cantidad}"
        super().__init__(self.mensaje)

# Uso de la excepción personalizada
class CuentaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo
        
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise ErrorSaldoInsuficiente(self.saldo, cantidad)
        self.saldo -= cantidad
        return self.saldo

# Ejemplo de uso
try:
    cuenta = CuentaBancaria(100)
    cuenta.retirar(150)
except ErrorSaldoInsuficiente as e:
    print(f"Error en la transacción: {e}")

################################################################################
## Excepciones en contexto (with)
################################################################################

# El bloque with maneja automáticamente excepciones y cierre de recursos
try:
    with open("ejemplo.txt", "w") as archivo:
        archivo.write("Hola mundo")
    # El archivo se cierra automáticamente al salir del bloque with
except IOError as e:
    print(f"Error de E/S: {e}")

################################################################################
## Encadenamiento de excepciones
################################################################################

# Podemos encadenar excepciones para proporcionar más contexto
try:
    try:
        # Código que puede generar una excepción
        resultado = int("abc")
    except ValueError as e:
        # Lanzamos una nueva excepción con más contexto
        raise RuntimeError("Error al procesar el dato") from e
except RuntimeError as e:
    print(f"Error: {e}")
    # Accedemos a la excepción original
    print(f"Causa: {e.__cause__}")

################################################################################
## Buenas prácticas en el manejo de excepciones
################################################################################

# 1. Sé específico con las excepciones que capturas
try:
    # Código específico
    pass
except SpecificException:
    # Manejo específico
    pass

# 2. No uses excepciones para flujo de control normal
# Mal ejemplo:
def es_par(numero):
    try:
        return numero % 2 == 0
    except:
        return False

# Mejor ejemplo:
def es_par(numero):
    if isinstance(numero, (int, float)):
        return numero % 2 == 0
    return False

# 3. Usa finally para liberar recursos
# 4. Proporciona mensajes de error informativos
# 5. Documenta las excepciones que puede lanzar tu función

# 6. Evita capturar Exception o BaseException genéricamente
try:
    # Algún código
    pass
except Exception:  # Demasiado genérico, evitar si es posible
    pass

# 7. Usa logging en lugar de print para errores en aplicaciones reales
import logging
try:
    # Código que puede fallar
    pass
except ValueError as e:
    logging.error(f"Error de valor: {e}")

################################################################################
## Depuración con excepciones
################################################################################

# Las excepciones proporcionan información valiosa para depuración
import traceback

try:
    # Código que genera una excepción
    1 / 0
except Exception as e:
    # Imprime el traceback completo
    print("Error detectado:")
    traceback.print_exc()
    
    # O guárdalo como string
    error_msg = traceback.format_exc()
    print(f"Mensaje de error guardado: {len(error_msg)} caracteres")