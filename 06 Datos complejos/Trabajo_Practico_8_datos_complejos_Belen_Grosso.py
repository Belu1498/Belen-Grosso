# Ejercicio 1: 
# Dado el diccionario precios_frutas 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 

# Añadir las siguientes frutas con sus respectivos precios: 
# ● Naranja = 1200 
# ● Manzana = 1500 
# ● Pera = 2300 

precios_frutas["Manzana"] = 1200
precios_frutas["Naranja"] = 1500
precios_frutas["Pera"] = 2300
print(precios_frutas)

# Ejercicio 2:
# Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
# ● Banana = 1330 
# ● Manzana = 1700 
# ● Melón = 2800 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, "Naranja" : 1500, "Pera": 2300, "Manzana": 1200} 

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800
print(precios_frutas)

# Ejercicio 3:
# Siguiendo con el diccionario precios_frutas que resulta luego de 
# ejecutar el código desarrollado en el punto anterior, crear 
# una lista que contenga únicamente las frutas sin los precios. 

precios_frutas = {"Banana", "Ananá", "Melón", "Uva", "Naranja", "Manzana", "Pera"} 

print(precios_frutas)

# Ejercicio 4:
# Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
# • Luego, pedí un nombre y mostrale el número asociado, si existe. 

contacto={}

for i in range(5):
    numero = int(input("Ingresa numero de telefono: "))
    nombre = input(f"Ingresa numero de nombre #{i + 1}: ")
    contacto[nombre] = numero

    
buscar_nombre = input("Ingresa el nombre que desea buscar: ")

print(f"Numero del contacto: {contacto[buscar_nombre]}")

# Ejercicio 5: 
# Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")

palabras_frase = frase.split()

frase_set = set(palabras_frase)



recuento={}

for cantidad in palabras_frase:
    if cantidad in recuento:
        recuento[cantidad] += 1
    else: 
        recuento[cantidad] = 1

print(recuento)

# Ejercicio 6:
# Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno.


lista_alumnos = []

for cantidad in range(2):
    alumno = input("Ingresa nombre: ")
    notas = []  # Lista para guardar las 3 notas

    for i in range(3):
        nota = int(input(f"Ingrese nota {i + 1}: "))
        notas.append(nota)  # Acumular las notas en una lista

    promedio = sum(notas) / len(notas)
    tupla = (alumno, notas)  # Crear tupla con el nombre y la lista de notas
    lista_alumnos.append(tupla)  # Agregar la tupla a la lista
    lista_alumnos.append(f"promedio: {promedio}")

print(lista_alumnos)

# Ejercicio 7:
# Dado dos sets de números, representando dos listas de estudiantes que 
# aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial_1 = {"Lucas": 8, "Carlos": 7, "Ana": 2, "Lucía": 10}
parcial_2 = {"Lucas": 9, "Carlos": 3, "Ana": 9, "Lucía": 7}


# Estudiantes que aprobaron ambos parciales
aprobados_ambos = {nombre for nombre in parcial_1 if parcial_1[nombre] >= 6 and parcial_2.get(nombre, 0) >= 6}

# Estudiantes que aprobaron solo uno de los dos parciales
aprobados_solo_uno = {nombre for nombre in parcial_1 if (parcial_1[nombre] >= 6) ^ (parcial_2.get(nombre, 0) >= 6)}

# Estudiantes que aprobaron al menos un parcial
aprobados_al_menos_uno = {nombre for nombre in parcial_1 if parcial_1[nombre] >= 6 or parcial_2.get(nombre, 0) >= 6}

# Mostrar resultados
print("Aprobaron ambos parciales:", aprobados_ambos)
print("Aprobaron solo uno:", aprobados_solo_uno)
print("Aprobaron al menos un parcial:", aprobados_al_menos_uno)

# Ejercicio 8:
# Armá un diccionario donde las claves sean nombres de 
#productos y los valores su stock. Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

repetir = True

productos = {
    "papel higienico": 5,
    "escobas": 9,
    "lampazo": 0,
    "shampoo": 2,
    "jabon": 0,
    "esponjas": 8
}

consultar_stock = input("¿Que producto desea consultar?: ")

if consultar_stock in productos.keys():
    print(productos[consultar_stock])
    productos[consultar_stock] = int(input("Agregar stock: ")) + productos[consultar_stock]
    print(productos)
else:
    input("Ups, parece que el produdcto que ingresaste no existe.")
    pregunta = input("¿Agregar nuevo producto? (si o no) ").lower()
    while repetir:
        if pregunta == "si":
            nuevo_producto = input("Ingresar nuevo producto: ")
            nuevo_stock = int(input("Ingresar stock: "))
            productos[nuevo_producto] = nuevo_stock
            input(f"El producto '{nuevo_producto}' fue agregado al inventario.")
            print(productos)
            break
        else:
            repetir = False
            break

# Ejercicio 9:
# Creá una agenda donde las claves sean tuplas de 
# (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.

agenda = {
    ("lunes", "9:00"): "Taller de cerámica",
    ("martes", "12:00"): "Reunión escolar",
    ("miercoles", "15:00"): "Pilates",
    ("jueves", "20:00"): "Reunión de amigos",
    ("viernes", "11:00"): "Turno médico",
}

clave_buscar = input("¿Que dia u horario queres consultar?: ").lower()

for clave in agenda:
    if clave_buscar in clave:
        print(f"{agenda[clave]}")

# Ejercicio 10:
# Dado un diccionario que mapea nombres de países con sus capitales, 
# construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.


lista_original = {
    "Argentina": "Buenos Aires",
    "Paraguay": "Asunción",
    "Bolivia": "Sucre",
    "Uruguay": "Montevideo",
    "Perú": "Lima",
    "España": "Madrid",
    "Portugal": "Lisboa",
    "Italia": "Roma",
}

lista_invertida = {valor: clave for clave, valor in lista_original.items()}

print(lista_original)
print(lista_invertida)
