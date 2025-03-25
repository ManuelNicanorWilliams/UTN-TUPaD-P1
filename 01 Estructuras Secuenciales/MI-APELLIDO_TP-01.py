# Ejercicio 1 
print ("Hola Mundo!")


# Ejercicio 2 
nombre = input("Ingresa tu nombre: ")
print (f"hola {nombre} como estas?")


# Ejercicio 3
nombre = input("Hola, ingrese su nombre: ")
apellido = input("Ahora ingrese su apellido: ")
edad = input("ingrese su edad: ")
residencia = input("Por ultimo ingrese su lugar de residencia: ")
print (f"Soy {nombre}, {apellido} tengo {30} años y vivo en {residencia}")


# Ejercicio 4
radio = input("ingrese el valor del radio de un circulo: ")
radio = float(radio) 
area = 3.14 * radio ** 2  
perimetro = 2 * 3.14 * radio
print(f"El area del circulo es: {area} y su perimetro es: {perimetro}")


# Ejercicio 5
segundos = int (input ("Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print (f"{segundos} segundos equivalen a {horas} horas.")


# Ejercicio 6
numero = int(input("Ingrese un numero entero: "))
print(f"La tabla de multiplicar del número {numero} es: ")
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")


# Ejercicio 7
while True:
    numero1 = int(input("Ingrese el primer número entero: "))
    if numero1 != 0:
        break
    print("El número no puede ser 0, ingresa otro número")

while True:
    numero2 = int(input("Ingrese el segundo número entero: "))
    if numero2 != 0:
        break
    print("El número no puede ser 0, ingresa otro número")

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f"La suma de {numero1} + {numero2} es = {suma}")
print(f"La resta de {numero1} - {numero2} es = {resta}")
print(f"La multiplicación de {numero1} x {numero2} es = {multiplicacion}")
print(f"La división de {numero1} / {numero2} es = {division}")


# Ejercicio 8
altura = float(input("Ingrese su altura (en Metros): "))
peso = float(input("Ahora ingrese su peso (en Kilos): "))
imc = peso / altura ** 2
print(f"Su índice de masa corporal (IMC) es: {imc}")


# Ejercicio 9
temp_celsius = float(input ("Ingrese una temperatura en grados Celsius: "))
temp_fahrenheit = (temp_celsius * 9/5) + 32
print(f"La temperatura {temp_celsius} grados Celcius equivale a {temp_fahrenheit} grados Fahrenheit")


# Ejercicio 10
numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
numero3 = float(input("Ingrese el tercer numero: "))

promedio = (numero1 + numero2 + numero3) / 3

print(f"El promedio de {numero1}, {numero2}, {numero3} es: {promedio}")
