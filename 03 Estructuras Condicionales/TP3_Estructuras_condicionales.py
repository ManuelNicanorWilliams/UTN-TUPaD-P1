
#Actividad 6:
#importar del paquete statistics las funciones mode, median y mean
from statistics import mode, median, mean

#imoportar random
import random

#crear lista de 50 números aleatorios del 1 al 100
numeros_aleatorios = [random.randint(1,100) for i in range(50)]

#verificar si hay sesgo positivo
if (mean(numeros_aleatorios) > median (numeros_aleatorios)) and (median(numeros_aleatorios) > mode(numeros_aleatorios)):
    print("Hay sesgo positivo ")

#verificar si hay sesgo negativo
elif (mean(numeros_aleatorios) < median(numeros_aleatorios)) and (median(numeros_aleatorios) < mode(numeros_aleatorios)):
    print("Hay sesgo negativo ")

#en el caso que no haya sesgo mostrar el mensaje
else:
    print("Sin sesgo ")


#Actividad 7:

# Definir lista de vocales
VOCALES = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

# Solicitar al usuario que ingrese una frase o palabra
frase = input("Ingrese una frase o palabra: ")

# Verificar si la ultima letra del string es una vocal
if frase and frase[-1] in VOCALES:
  print(frase + "!")

else:
  print(frase)

#Actividad 8:

# Solicitar al usuario que ingrese su nombre
nombre = input("Ingrese su nombre: ")

# Solicitar al usuario que ingrese una opción
opcion = int(input("Ingrese una opción (1 si quiere su nombre en mayúsculas, 2 si quiere su nombre en minúsculas o 3 si quiere su nombre con la primera letra mayúscula): "))

# Si quiere su nombre en mayúsculas
if opcion == 1:
    print(nombre.upper())

# Si quiere su nombre en minúsculas
elif opcion == 2:
    print(nombre.lower())

# Si quiere su nombre con la primera letra mayúscula  
elif opcion == 3:
    print(nombre.title())

# Si ingresa una opción incorrecta
else:
    print("Opción incorrecta")

#Actividad 9:

# Solicitar al usuario la magnitud del terremoto
magnitud = float(input("Ingrese la magnitud del terremoto en la escala de Richter: "))

# Clasificar el terremoto según su magnitud
if magnitud < 3:
    categoria = "Muy leve (imperceptible)"
elif 3 <= magnitud < 4:
    categoria = "Leve (ligeramente perceptible)"
elif 4 <= magnitud < 5:
    categoria = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif 5 <= magnitud < 6:
    categoria = "Fuerte (puede causar daños en estructuras débiles)"
elif 6 <= magnitud < 7:
    categoria = "Muy Fuerte (puede causar daños significativos)"
else:
    categoria = "Extremo (puede causar graves daños a gran escala)"

# Mostrar el resultado por pantalla
print(f"La magnitud {magnitud} corresponde a un terremoto: {categoria}")

#Actividad 10:

# Solicitar datos al usuario
hemisferio = input("¿En qué hemisferio te encuentras? (N para Norte / S para Sur): ").upper()
mes = int(input("Ingresa el mes (del 1-12): "))
dia = int(input("Ingresa el día (del 1-31): "))

# Determinar la estación según el hemisferio
if hemisferio == 'N':
    if (mes == 12 and dia >= 21) or (mes == 1 or mes == 2) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes == 4 or mes == 5) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes == 7 or mes == 8) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes == 10 or mes == 11) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
    else:
        estacion = "Fecha no válida"
elif hemisferio == 'S':
    if (mes == 12 and dia >= 21) or (mes == 1 or mes == 2) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes == 4 or mes == 5) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes == 7 or mes == 8) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes == 10 or mes == 11) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
    else:
        estacion = "Fecha no válida"
else:
    estacion = "Hemisferio no válido"

# Mostrar resultado
print(f"Estación actual: {estacion}")