# Actividad 1:

multiplos_de_4 = list(range(4, 101, 4)) # crea una lista que recorre los multiplos de 4 entre 4 y 100
print(multiplos_de_4) # imprime la lista

# Actividad 2:

lista_elementos = ["Juan", "Pedro", "Jose", "Maria", "Rita"] # crea una lista con 5 elementos
print(lista_elementos[-2]) # imprime el penúltimo elemento de la lista usando indexación negativa

# Actividad 3:

lista_vacia = [] # crea una lista vacia
lista_vacia.append("Perro") # agrega un elemento a "lista_vacia"
lista_vacia.append("Gato") # agrega un elemento a "lista_vacia"
lista_vacia.append("Conejo") # agrega un elemento a "lista_vacia"
print(lista_vacia) # imprime la lista

# Actividad 4:

animales = ["perro", "gato", "conejo", "pez"] #crea una lista con 3 elementos
animales[1] = "loro" # reemplaza el segundo elemento de la lista
animales[-1] = "oso" # reemplaza el ultimo elemento de la lista
print(animales) # imprime la lista

# Actividad 5:

numeros = [8, 15, 3, 22, 7] # crea una lista con 5 numeros
numeros.remove(max(numeros)) # remueve el mayor número de la lista
print(numeros) # imprime la lista

# Actividad 6:

lista_numeros = list(range(10, 31, 5)) # crea una lista que recorre los números del 10 al 30 (incluído) con saltos de 5 en 5
print(lista_numeros[:2]) # imprime los primeros 2 elementos de la lista

# Actividad 7:

autos = ["sedan", "polo", "suran", "gol"] # rea una lista con 4 elementos
autos[1:3] = [True, 3.14] # reemplaza los elementos desde el índice 1 hasta el 3
print(autos) # imprime la lista

# Actividad 8:

dobles = [] # crea una lista vacia
dobles.append(5 * 2) # calcula 5*2 (10) y lo agrega a la lista "dobles" 
dobles.append(10 * 2) # calcula 10*2 (20) y lo agrega a la lista "dobles" 
dobles.append(15 * 2) # calcula 15*2 (30) y lo agrega a la lista "dobles" 
print(dobles) # imprime la lista

# Actividad 9:

compras = [ #crea una lista de "compras" que contiene 3 clientes
"cliente_1: ",[["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]], # crea una lista de compras anidada en "cliente_1"
"cliente_2: ",[["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]], # crea una lista de compras anidada en "cliente_2"
"cliente_3: ",[["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] # crea una lista de compras anidada en "cliente_3"
]
compras[5][2].append("jugo") # agrega "jugo" en cliente_3
compras[3][1][1] = "tallarines" # cambia "fideos" por "tallarines" en cliente_2 
compras[1][0].remove ("pan") # elimina "pan" de cliente_1
print(compras) # imprime la lista

# Actividad 10:

lista_anidada = [15, True, [25.5, 57.9, 30.6], False] # crea una lista de 4 elementos, con una lista anidada de 3 elementos en la segunda posición
print(lista_anidada) # imprime la lista
