# Actividad 1:

# Crea el diccionario dado
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añade frutas con sus respectivos precios
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Muestra el diccionario actualizado
print(precios_frutas)

# Actividad 2:

# Actualiza precios de frutas
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Muestra el diccionario actualizado
print(precios_frutas)

# Actividad 3:

# Crea una lista de las frutas sin los precios
lista_frutas = list(precios_frutas.keys())

# Imprime la lista de las frutas son los precios
print(lista_frutas)

# Actividad 4:

# Crear un diccionario para almacenar los contactos
contactos = {}

# Cargar 5 contactos
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto #{i+1}: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    contactos[nombre] = numero

# Consultar un número por nombre
consulta = input("Ingresá el nombre del contacto que querés buscar: ")

if consulta in contactos:
    print(f"El número de {consulta} es {contactos[consulta]}")
else:
    print("El contacto ingresado no está en la agenda.")

# Actividad 5:

# Pedir al usuario que ingrese una frase
frase = input("Ingresá una frase: ")

# Dividir la frase en una lista de palabras, usando espacios como separadores
palabras = frase.split()

# Crear un conjunto de palabras únicas (sin repeticiones)
palabras_unicas = set(palabras)

# Crear un diccionario vacío para almacenar la cantidad de apariciones de cada palabra
diccionario = {}

# Recorrer cada palabra única
for palabra in palabras_unicas:
    # Contar cuántas veces aparece esa palabra en la lista original y guardarla en el diccionario
    diccionario[palabra] = palabras.count(palabra)

# Mostrar el conjunto de palabras únicas
print("Palabras únicas:", palabras_unicas)

# Mostrar cuántas veces aparece cada palabra
print("Cantidad de veces que aparece cada palabra:", diccionario)

# Actividad 6:

# Crear un diccionario para almacenar alumnos y sus notas
alumnos = {}

# Ingresar los datos de 3 alumnos
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno #{i+1}: ")
    print(f"Ingresá las 3 notas de {nombre}:")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    alumnos[nombre] = (nota1, nota2, nota3)

# Calcular y mostrar el promedio de cada alumno
print("\nPromedios:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

# Actividad 7:

# Sets de estudiantes que aprobaron cada parcial
parcial1 = {"Ana", "Luis", "Sofía", "Carlos", "Julián"}
parcial2 = {"Sofía", "Carlos", "Valeria", "Lucía", "Julián"}

# Estudiantes que aprobaron ambos parciales
ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

# Estudiantes que aprobaron solo uno de los dos
solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los dos parciales:", solo_uno)

# Estudiantes que aprobaron al menos un parcial
al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)

# Actividad 8:

# Diccionario con productos y sus stocks
stock_productos = {
    "manzanas": 10,
    "naranjas": 5,
    "peras": 7
}

# Mostrar el stock actual
print("Stock inicial:", stock_productos)

# Consultar o actualizar/agregar producto
producto = input("\nIngresá el nombre del producto: ").lower()

if producto in stock_productos:
    print(f"Stock actual de {producto}: {stock_productos[producto]}")
    agregar = int(input(f"¿Cuántas unidades querés agregar a {producto}?: "))
    stock_productos[producto] += agregar
    print(f"Nuevo stock de {producto}: {stock_productos[producto]}")
else:
    nuevo_stock = int(input(f"{producto} no existe. Ingresá el stock inicial para agregarlo: "))
    stock_productos[producto] = nuevo_stock
    print(f"{producto} agregado con un stock de {nuevo_stock} unidades.")

# Mostrar stock actualizado
print("\nStock actualizado:", stock_productos)

# Actividad 9:

# Crear agenda vacía
agenda = {}

# Cargar eventos
for i in range(3):
    dia = input(f"Ingresá el día del evento #{i+1} (ej. lunes): ").lower()
    hora = input(f"Ingresá la hora del evento #{i+1} (ej. 14:00): ")
    evento = input("Descripción del evento: ")
    clave = (dia, hora)
    agenda[clave] = evento

# Mostrar agenda
print("\nAgenda:")
for clave, evento in agenda.items():
    dia, hora = clave
    print(f"{dia.title()} a las {hora}: {evento}")

# Actividad 10:

# Diccionario original: país : capital
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Bolivia": "La Paz",
    "Chile": "Santiago de Chile",
    "Brasil": "Brasilia",
    "Peru": "Lima",
    "Uruguay": "Montevideo"
}

# Mostrar el diccionario original
print("Diccionario original (país : capital):")
for pais, capital in paises_capitales.items():
    print(f"{pais} : {capital}")

# Crear nuevo diccionario invertido: capital : país
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

# Mostrar el nuevo diccionario
print("\nDiccionario invertido (capital : país):")
for capital, pais in capitales_paises.items():
    print(f"{capital} : {pais}")
