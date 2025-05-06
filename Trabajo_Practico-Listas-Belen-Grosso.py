# Ejercicio 1

lista = list(range(4,101,4))
print(lista)

# Ejercicio 2

elementos = ["milanesa", "pure", "ensalada", "pollo", "pizza"]

posicion = elementos[2]
print(posicion)

# Ejercicio 3

lista_vacia = []

lista_vacia.append("Argentina")

print(lista_vacia)

# Ejercicio 4

animales = ["perro", "gato", "conejo", "pez"]

animales[-1] = "oso"
animales[-2] = "loro"
print(animales)

# Ejercicio 5

# La funcion "max" devuelve el elemento mas grande dentro de la lista "numeros".
# Pero tambien tenemos "remove" dentro del codigo lo que significa que
# el elemento de mayor valor será eliminado, en este caso el numero 22 quedando como
# resultado: [8, 15, 3, 7]

# Ejercicio 6

lista = list(range(10,31,5))

posicion = lista[0:2]
print(posicion)

# Ejercicio 7

autos = ["sedan", "polo", "suran", "gol"] 

autos[1] = "ram"
autos[2] = "meriva"

print(autos)

# Ejercicio 8

dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)

# Ejercicio 9

# A

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 

cliente_3 = compras[2]

cliente_3.append("jugo")

# B

compras[1][1] = "tallarines"

# C

cliente_1 = compras[0]

cliente_1.remove("pan")

# D

print(compras)

# Ejercicio 10

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)