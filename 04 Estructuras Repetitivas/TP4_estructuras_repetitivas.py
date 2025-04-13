# Actividad 1

# Este bucle imprime los números del 0 al 100
for i in range(101): # genera números desde 0 hasta 100
    print (i)          # Imprime el valor actual de i en cada iteración


# Actividad 2

# Este código calcula la cantidad de dígitos de un número entero ingresado por el usuario
numero = int(input("ingrese un número: ")) # 1. Solicita y convierte la entrada
print(len(str(numero)))                    # 2. Calcula e imprime la longitud


# Actividad 3

# Este código calcula la suma de todos los números enteros entre dos números ingresados por el usuario
numero1 = int(input("ingrese un número:"))  # 1. Primer número ingresado
numero2 = int(input("ingrese un número:"))  # 2. Segundo número ingresado
suma = 0                                    # 3. Inicializa acumulador de suma
for i in range(numero1 + 1, numero2):       # 4. Bucle entre los números (excluyendo extremos)
    suma += i                               # 5. Acumula cada número en la suma
print(suma)                                 # 6. Imprime el resultado final


# Actividad 4

# Este código implementa un sumador acumulativo que:
# 1. Solicita números al usuario repetidamente
# 2. Acumula la suma de todos los números ingresados
# 3. Termina cuando se ingresa 0 (condición de salida)
# 4. Muestra la suma total acumulada

numero = int(input("ingrese un número:"))     # 1. Primer número ingresado
suma = 0                                       # 2. Inicializa el acumulador
while numero != 0:                             # 3. Condición de continuación
    suma += numero                             # 4. Acumula el número actual
    numero = int(input("ingrese un número:"))  # 5. Solicita nuevo número
print(suma)                                    # 6. Imprime la suma total


# Actividad 5

# Este código implementa un juego de adivinanza donde:
# 1. Se genera un número aleatorio entre 0 y 9
# 2. El usuario debe adivinarlo ingresando números
# 3. El programa cuenta los intentos hasta acertar
# 4. Finalmente muestra el total de intentos realizados

import random # Importa el módulo para generar números aleatorios

# 1. Generación del número a adivinar (entre 0 y 9 inclusive)
numero_aleatorio = random.randint(0,9)

# 2. Primer intento del usuario
numero = int(input("ingrese un número:"))
intentos = 1 # Contador de intentos (inicia en 1 por el primer intento)

# 3. Bucle while para seguir pidiendo números hasta acertar
while numero != numero_aleatorio:
    intentos += 1 # Incrementa el contador de intentos
    numero = int(input("ingrese un número: "))

# 4. Mensaje final cuando se adivina el número
print(f"¡Es correcto! realizaste {intentos} intentos")


# Actividad 6

# Este código imprime todos los números pares en orden descendente desde 100 hasta 0

for i in range(100, -1, -1):  # Bucle desde 100 hasta 0 (inclusive), decrementando de 1 en 1
    if i % 2 == 0:            # Verifica si el número es par
        print(i)              # Imprime el número si es par


# Actividad 7

# Este código calcula la suma de todos los números enteros desde 0 hasta un número N ingresado por el usuario

numero = int(input("Ingrese un número: "))  # 1. Solicita y convierte el número de entrada
suma = 0                                    # 2. Inicializa el acumulador de suma
for i in range(numero + 1):                 # 3. Bucle desde 0 hasta numero (inclusive)
    suma += i                               # 4. Acumula cada número en la suma
print(suma)                                 # 5. Imprime el resultado final


# Actividad 8

# Este código analiza 100 números ingresados por el usuario, contando:
# - Cantidad de números pares e impares
# - Cantidad de números negativos y positivos/cero

numeros = 100           # Cantidad total de números a procesar
cantidad_pares = 0      # Contador para números pares
cantidad_impares = 0    # Contador para números impares
cantidad_negativos = 0  # Contador para números negativos
cantidad_positivos = 0  # Contador para números positivos o cero

for i in range(numeros):                        # Bucle para solicitar 100 números
    numero = int(input("Ingrese un número: "))  # Solicita cada número
    
    # Clasificación par/impar
    if numero % 2 == 0:          # Si el número es divisible entre 2
        cantidad_pares += 1      # Incrementa contador de pares
    else:
        cantidad_impares += 1    # Incrementa contador de impares
    
    # Clasificación positivo/negativo
    if numero < 0:               # Si el número es menor que 0
        cantidad_negativos += 1  # Incrementa contador de negativos
    else:
        cantidad_positivos += 1  # Incrementa contador de positivos/cero

# Mostrar resultados
print(f"Pares: {cantidad_pares}")
print(f"Impares: {cantidad_impares}")
print(f"Negativos: {cantidad_negativos}")
print(f"Positivos: {cantidad_positivos}")


# Actividad 9

# Este código calcula la media aritmética de 100 números ingresados por el usuario

numeros = 100  # Cantidad total de números a procesar
suma = 0       # Inicializa el acumulador de la suma total

for i in range(numeros):                        # Bucle para solicitar los 100 números
    numero = int(input("Ingrese un número: "))  # Solicita cada número
    suma += numero                              # Acumula cada número en la suma total
    media = suma / numeros                      # Calcula la media actualizada

print(f"La media de los valores ingresados es: {media}")


# Actividad 10

# Este código invierte el orden de los dígitos de un número ingresado como cadena de texto

numero = input("Ingrese un número: ")                 # 1. Recibe el número como string
numero_invertido = numero[::-1]                       # 2. Invierte la cadena
print(f"Su número invertido es: {numero_invertido}")  # 3. Muestra el resultado