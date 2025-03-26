################################################################################
# Expresiones Regulares en Python
################################################################################

'''
Las expresiones regulares (regex) son patrones de búsqueda que se utilizan para
encontrar y manipular texto. Son extremadamente poderosas para validar formatos,
extraer información y realizar sustituciones complejas en cadenas de texto.

En Python, las expresiones regulares se implementan a través del módulo 're'.
'''

import re

################################################################################
# Conceptos Básicos
################################################################################

# Ejemplo 1: Coincidencia simple
print("Ejemplo 1: Coincidencia simple")
texto = "Python es un lenguaje de programación poderoso y fácil de aprender."

# Buscar la palabra 'Python' en el texto
resultado = re.search(r'Python', texto)
if resultado:
    print(f"Encontrado: '{resultado.group()}' en la posición {resultado.start()}")
else:
    print("No encontrado")

# Ejemplo 2: Metacaracteres básicos
print("\nEjemplo 2: Metacaracteres básicos")
texto = "El precio es $100 y el código es ABC-123"

# \d busca dígitos (0-9)
digitos = re.findall(r'\d', texto)
print(f"Dígitos encontrados: {digitos}")

# \w busca caracteres alfanuméricos [a-zA-Z0-9_]
alfanumericos = re.findall(r'\w', texto)
print(f"Caracteres alfanuméricos: {alfanumericos[:10]}...")

# \s busca espacios en blanco
espacios = re.findall(r'\s', texto)
print(f"Espacios encontrados: {len(espacios)}")

################################################################################
# Cuantificadores
################################################################################

# Ejemplo 3: Cuantificadores
print("\nEjemplo 3: Cuantificadores")
texto = "Python 3.9.5"

# * (cero o más repeticiones)
print(re.findall(r'Py.*n', texto))  # Encuentra 'Python'

# + (una o más repeticiones)
print(re.findall(r'\d+', texto))  # Encuentra '3', '9', '5'

# ? (cero o una repetición)
print(re.findall(r'Python\s?', texto))  # Encuentra 'Python '

# {n} (exactamente n repeticiones)
print(re.findall(r'\d{1}', texto))  # Encuentra '3', '9', '5'

# {n,m} (entre n y m repeticiones)
print(re.findall(r'\d{1,2}', texto))  # Encuentra '3', '9', '5'

################################################################################
# Conjuntos de Caracteres y Rangos
################################################################################

# Ejemplo 4: Conjuntos y rangos
print("\nEjemplo 4: Conjuntos y rangos")
texto = "abc123ABC"

# Conjunto de caracteres [...]
print(re.findall(r'[abc]', texto))  # Encuentra 'a', 'b', 'c'

# Rango de caracteres [a-z]
print(re.findall(r'[a-z]', texto))  # Encuentra 'a', 'b', 'c'

# Negación de conjunto [^...]
print(re.findall(r'[^a-z]', texto))  # Encuentra '1', '2', '3', 'A', 'B', 'C'

# Combinación de rangos
print(re.findall(r'[a-zA-Z]', texto))  # Encuentra todas las letras

################################################################################
# Anclas y Límites
################################################################################

# Ejemplo 5: Anclas
print("\nEjemplo 5: Anclas")
texto = "Python es genial\nJava también es bueno"

# ^ (inicio de línea)
print(re.findall(r'^Python', texto))  # Encuentra 'Python'
print(re.findall(r'^Java', texto))  # No encuentra nada en modo normal

# $ (fin de línea)
print(re.findall(r'genial$', texto, re.MULTILINE))  # Encuentra 'genial' con multiline
print(re.findall(r'bueno$', texto))  # Encuentra 'bueno'

# \b (límite de palabra)
texto = "Python es un lenguaje, python es genial"
print(re.findall(r'\bPython\b', texto))  # Encuentra solo 'Python' con P mayúscula

################################################################################
# Grupos y Capturas
################################################################################

# Ejemplo 6: Grupos de captura
print("\nEjemplo 6: Grupos de captura")
texto = "Mi correo es usuario@ejemplo.com y mi teléfono es 123-456-7890"

# Capturar correo electrónico
patron_email = r'(\w+)@(\w+)\.(\w+)'
match_email = re.search(patron_email, texto)
if match_email:
    print(f"Email completo: {match_email.group(0)}")
    print(f"Usuario: {match_email.group(1)}")
    print(f"Dominio: {match_email.group(2)}")
    print(f"TLD: {match_email.group(3)}")

# Capturar número de teléfono
patron_telefono = r'(\d{3})-(\d{3})-(\d{4})'
match_telefono = re.search(patron_telefono, texto)
if match_telefono:
    print(f"Teléfono completo: {match_telefono.group(0)}")
    print(f"Código de área: {match_telefono.group(1)}")
    print(f"Prefijo: {match_telefono.group(2)}")
    print(f"Número: {match_telefono.group(3)}")

# Ejemplo 7: Grupos con nombre
print("\nEjemplo 7: Grupos con nombre")
patron_email_named = r'(?P<usuario>\w+)@(?P<dominio>\w+)\.(?P<tld>\w+)'
match_email_named = re.search(patron_email_named, texto)
if match_email_named:
    print(f"Usuario: {match_email_named.group('usuario')}")
    print(f"Dominio: {match_email_named.group('dominio')}")
    print(f"TLD: {match_email_named.group('tld')}")

################################################################################
# Funciones Principales del Módulo re
################################################################################

# Ejemplo 8: Funciones principales
print("\nEjemplo 8: Funciones principales")
texto = "Python es un lenguaje de programación. Python es fácil de aprender."

# re.search() - Busca la primera coincidencia
resultado = re.search(r'Python', texto)
print(f"search: {resultado.group() if resultado else 'No encontrado'}")

# re.match() - Busca al inicio de la cadena
resultado = re.match(r'Python', texto)
print(f"match: {resultado.group() if resultado else 'No encontrado'}")

# re.findall() - Encuentra todas las coincidencias
resultado = re.findall(r'Python', texto)
print(f"findall: {resultado}")

# re.finditer() - Iterador de coincidencias
print("finditer:")
for match in re.finditer(r'Python', texto):
    print(f"  Encontrado en posición {match.start()}-{match.end()}")

# re.sub() - Sustituye coincidencias
resultado = re.sub(r'Python', 'Ruby', texto)
print(f"sub: {resultado}")

# re.split() - Divide la cadena por coincidencias
resultado = re.split(r'\.', texto)
print(f"split: {resultado}")

################################################################################
# Banderas (Flags)
################################################################################

# Ejemplo 9: Banderas
print("\nEjemplo 9: Banderas")
texto = "Python es genial\nPYTHON ES PODEROSO"

# re.IGNORECASE (o re.I) - Ignora mayúsculas/minúsculas
print(f"IGNORECASE: {re.findall(r'python', texto, re.IGNORECASE)}")

# re.MULTILINE (o re.M) - ^ y $ coinciden con inicio/fin de cada línea
print(f"MULTILINE: {re.findall(r'^python', texto, re.MULTILINE | re.IGNORECASE)}")

# re.DOTALL (o re.S) - El punto coincide con cualquier carácter, incluido \n
texto_multilinea = "Línea 1\nLínea 2"
print(f"DOTALL: {re.findall(r'Línea.+2', texto_multilinea, re.DOTALL)}")

# re.VERBOSE (o re.X) - Permite comentarios y espacios en el patrón
patron_complejo = re.compile(r'''
    \b          # Límite de palabra
    [A-Z]       # Primera letra mayúscula
    [a-z]*      # Resto de letras minúsculas
    \b          # Límite de palabra
''', re.VERBOSE)
texto = "Hola Mundo python Java"
print(f"VERBOSE: {patron_complejo.findall(texto)}")

################################################################################
# Patrones Comunes
################################################################################

# Ejemplo 10: Patrones comunes
print("\nEjemplo 10: Patrones comunes")

# Email
patron_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = ["usuario@ejemplo.com", "invalid@.com", "otro@dominio.co.uk"]
for email in emails:
    if re.match(patron_email, email):
        print(f"{email}: Válido")
    else:
        print(f"{email}: Inválido")

# URL
patron_url = r'https?://(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:/[a-zA-Z0-9-._~:/?#[\]@!$&\'()*+,;=]*)?'
urls = ["https://www.ejemplo.com", "http://ejemplo.com/ruta", "ftp://invalido.com"]
for url in urls:
    if re.match(patron_url, url):
        print(f"{url}: Válido")
    else:
        print(f"{url}: Inválido")

# Fecha (formato DD/MM/YYYY)
patron_fecha = r'\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}\b'
fechas = ["01/01/2022", "31/02/2022", "15/12/2022"]
for fecha in fechas:
    if re.match(patron_fecha, fecha):
        print(f"{fecha}: Formato válido")
    else:
        print(f"{fecha}: Formato inválido")

################################################################################
# Aplicaciones Prácticas
################################################################################

# Ejemplo 11: Validación de contraseña
print("\nEjemplo 11: Validación de contraseña")

def validar_password(password):
    """
    Valida que una contraseña cumpla con los siguientes requisitos:
    - Al menos 8 caracteres
    - Al menos una letra mayúscula
    - Al menos una letra minúscula
    - Al menos un número
    - Al menos un carácter especial
    """
    # Verificar longitud
    if len(password) < 8:
        return False, "La contraseña debe tener al menos 8 caracteres"
    
    # Verificar mayúscula
    if not re.search(r'[A-Z]', password):
        return False, "La contraseña debe tener al menos una letra mayúscula"
    
    # Verificar minúscula
    if not re.search(r'[a-z]', password):
        return False, "La contraseña debe tener al menos una letra minúscula"
    
    # Verificar número
    if not re.search(r'\d', password):
        return False, "La contraseña debe tener al menos un número"
    
    # Verificar carácter especial
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "La contraseña debe tener al menos un carácter especial"
    
    return True, "Contraseña válida"

passwords = ["abc123", "Password1", "Secure2022!", "NoSpecial123"]
for pwd in passwords:
    valido, mensaje = validar_password(pwd)
    print(f"'{pwd}': {mensaje}")

# Ejemplo 12: Extracción de información
print("\nEjemplo 12: Extracción de información")

texto_html = """
<div class="producto">
    <h2>Laptop HP</h2>
    <p class="precio">$999.99</p>
    <p class="descripcion">Laptop con 16GB RAM, 512GB SSD</p>
</div>
<div class="producto">
    <h2>Monitor Dell</h2>
    <p class="precio">$299.50</p>
    <p class="descripcion">Monitor 27 pulgadas 4K</p>
</div>
"""

# Extraer información de productos
patron_producto = r'<div class="producto">\s*<h2>(.+?)</h2>\s*<p class="precio">\$(.+?)</p>\s*<p class="descripcion">(.+?)</p>\s*</div>'

productos = []
for match in re.finditer(patron_producto, texto_html, re.DOTALL):
    producto = {
        'nombre': match.group(1),
        'precio': float(match.group(2)),
        'descripcion': match.group(3)
    }
    productos.append(producto)

for producto in productos:
    print(f"Producto: {producto['nombre']}")
    print(f"Precio: ${producto['precio']}")
    print(f"Descripción: {producto['descripcion']}")
    print("-" * 30)

# Ejemplo 13: Sustitución avanzada
print("\nEjemplo 13: Sustitución avanzada")

# Función para procesar cada coincidencia
def reemplazar_formato(match):
    texto = match.group(1)
    if match.group(0).startswith('**'):
        return f"<strong>{texto}</strong>"
    elif match.group(0).startswith('*'):
        return f"<em>{texto}</em>"
    elif match.group(0).startswith('`'):
        return f"<code>{texto}</code>"

# Texto en formato markdown
texto_markdown = """
# Título

Este es un párrafo con *texto en cursiva*, **texto en negrita**
y `código inline`.
"""

# Convertir markdown a HTML
texto_html = re.sub(r'\*\*(.+?)\*\*|\*(.+?)\*|`(.+?)`', reemplazar_formato, texto_markdown)
print(texto_html)

################################################################################
# Optimización y Rendimiento
################################################################################

# Ejemplo 14: Compilación de patrones
print("\nEjemplo 14: Compilación de patrones")
import time

texto_largo = "Python " * 100000

# Medir tiempo sin compilar
inicio = time.time()
re.findall(r'Python', texto_largo)
fin = time.time()
print(f"Tiempo sin compilar: {fin - inicio:.6f} segundos")

# Medir tiempo con patrón compilado
patron_compilado = re.compile(r'Python')
inicio = time.time()
patron_compilado.findall(texto_largo)
fin = time.time()
print(f"Tiempo con patrón compilado: {fin - inicio:.6f} segundos")

################################################################################
# Consejos y Buenas Prácticas
################################################################################

'''
1. Compila patrones que uses repetidamente con re.compile()
2. Usa grupos con nombre para mayor claridad
3. Utiliza la bandera re.VERBOSE para patrones complejos
4. Evita la recursión excesiva (backtracking) en patrones
5. Prueba tus expresiones regulares con herramientas como regex101.com
6. Para tareas simples, considera usar métodos de string como .startswith(), .endswith()
7. Documenta tus expresiones regulares complejas
'''

################################################################################
# Conclusiones
################################################################################

'''
Las expresiones regulares son una herramienta poderosa para:

1. Validar formatos (emails, teléfonos, fechas, etc.)
2. Extraer información de textos estructurados
3. Realizar sustituciones complejas
4. Analizar y procesar grandes volúmenes de texto

Aunque tienen una curva de aprendizaje pronunciada, dominar las expresiones
regulares te permite resolver problemas complejos de procesamiento de texto
de manera eficiente y elegante.

Python proporciona una implementación completa y flexible de expresiones
regulares a través del módulo 're', con funciones para buscar, extraer,
sustituir y dividir texto basado en patrones.
'''