# Actividad 1:

# Decfinir la mayoria de edad
MAYOR_DE_EDAD = 18 

# Solicitar la edad del usuario
edad = int(input("Ingrese su edad: "))

# Verificar si el usuario es mayor de 18 años
if edad >= MAYOR_DE_EDAD:
    print("Es mayor de edad ")

else:
    print("Es menor de edad ")

# Actividad 2:

# Definir nota para aprobar
NOTA_APROBADO = 6

# Solicitar nota al usuario
nota = int(input("Ingrese su nota: "))

# Verificar si esta aprobado
if nota >= NOTA_APROBADO:
    print("Estas aprobado")

# Mensaje si no aprobo
else :
    print("estas desaprobado")


# Actividad 3:

# Solicitar número al usuario
numero = int(input("Ingrese un número par: "))

# Verificar si el numero es par
if numero % 2 == 0:
    # mostrar un mensaje en pantalla
    print("Ha ingresado un número par ")

# Mensaje si no es par
else:
    print("Por favor, ingrese un número par ")


# Actividad 4:

# Solicitar la edad al usuario
edad = int(input("Ingrese su edad: "))

# Verificar si es menor de 12 años
if edad < 12:
    print("Eres un Niño/a ")

# Verificar si es mayor o igual que 12 años y menor que 18 años.
elif edad >= 12 and edad <18:
    print("Eres un adolecente ")

# Verificar si es mayor o igual que 18 años y menor que 30 años.
elif edad >= 18 and edad < 30:
    print("Eres un adulto/a joven ")

# En los demas casos mostrar este mensaje
else:
    print("Eres un adulto/a ")    


# Actividad 5:

# Definir constantes
LONG_MIN = 8
LONG_MAX = 14

# Solicitar al usuario que ingrese una contraseña
contraseña= input("Por favor, igrese una contraseña (debe terner al menos 8 caracteres y no mas de 14)")

# Verificar que la contraseña sea correcta
if len(contraseña) >= LONG_MIN and len(contraseña) <= LONG_MAX:
    print("Ha ingresado una contraseña correcta ")

# En caso que se incorrecta mostrar este mensaje
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


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
