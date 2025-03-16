"""
  Las estructuras condicionales son fundamentales en cualquier lenguaje de programacion, ya que permiten que el programa tome decisiones basadas en condiciones especificas.
"""

################################################################################## Estructuras Condicionales en Python
################################################################################

# Las estructuras condicionales permiten ejecutar diferentes bloques de codigo dependiendo de si una condicion es verdadera o falsa


################################################################################## Operadores de comparacion
################################################################################

# == (igual a)
# != (diferente de)
# > (mayor que)
# < (menor que)
# >= (mayor o igual que)
# <= (menor o igual que)


################################################################################## Estructura if
################################################################################

# Sintaxis basica
edad = 18

if edad >= 18:
  print("Eres mayor de edad")

# El bloque de codigo dentro del if solo se ejecuta si la condicion es True
# En python, la identacion (espacios al inicio de la linea) es obligatoria y define los bloque de codigo

################################################################################## Estructura if-else
################################################################################

edad = 16

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
    
# El bloque else se ejecuta cuando la condición del if es False

################################################################################## Estructura if-elif-else
################################################################################

nota = 85

if nota >= 90:
    print("Sobresaliente")
elif nota >= 80:
    print("Notable")
elif nota >= 70:
    print("Bien")
elif nota >= 60:
    print("Suficiente")
else:
    print("Insuficiente")
    
# Podemos tener múltiples condiciones con elif (else if)
# Se evalúan en orden y se ejecuta el primer bloque cuya condición sea True
# Si ninguna condición es True, se ejecuta el bloque else (si existe)


################################################################################## Operadores logicos
################################################################################

# and: Verdadero si ambas condiciones son verdaderas
# or: Verdadero si al menos una condición es verdadera
# not: Invierte el valor de la condición

edad = 25
tiene_licencia = True

if edad >= 18 and tiene_licencia:
    print("Puede conducir")
    
if edad < 18 or not tiene_licencia:
    print("No puede conducir")


################################################################################## Condicionales anidados
################################################################################

edad = 20
es_estudiante = True

if edad >= 18:
    if es_estudiante:
        print("Es mayor de edad y estudiante")
    else:
        print("Es mayor de edad pero no estudiante")
else:
    print("Es menor de edad")

# También se puede escribir con and
if edad >= 18 and es_estudiante:
    print("Es mayor de edad y estudiante")


################################################################################## Operador ternario (exprecion condicional)
################################################################################

# Sintaxis: valor_si_verdadero if condicion else valor_si_falso
edad = 20
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)  # Imprime "Mayor de edad"


################################################################################## Verificacion de valores en colecciones
################################################################################

frutas = ["manzana", "banana", "naranja"]

if "manzana" in frutas:
    print("Hay manzanas en la lista")


################################################################################## Evaluacion de valores como booleanos
################################################################################

# Los siguientes valores se evalúan como False:
# - False
# - None
# - 0 (cero)
# - "" (cadena vacía)
# - [] (lista vacía)
# - {} (diccionario vacío)
# - set() (conjunto vacío)
# - () (tupla vacía)

# Cualquier otro valor se evalúa como True

nombre = ""
if not nombre:
    print("El nombre está vacío")

lista = [1, 2, 3]
if lista:
    print("La lista tiene elementos")

################################################################################## Consejo y buenas practicas
################################################################################

# 1. Evita condiciones complejas, divídelas en variables con nombres descriptivos
es_adulto = edad >= 18
tiene_permiso = tiene_licencia and ha_pagado_cuota
if es_adulto and tiene_permiso:
    print("Acceso concedido")

# 2. Usa paréntesis para clarificar el orden de evaluación en condiciones complejas
if (a > b and c > d) or (e > f):
    print("Condición compleja cumplida")

# 3. Aprovecha el cortocircuito de los operadores lógicos
# - En 'and', si el primer operando es False, el segundo no se evalúa
# - En 'or', si el primer operando es True, el segundo no se evalúa

# 4. Evita comparar directamente con True o False
# En lugar de:
if es_valido == True:
    print("Es válido")
    
# Mejor usar:
if es_valido:
    print("Es válido")