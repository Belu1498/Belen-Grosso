# Ejercicio 1: 

edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad.")


# Ejercicio 2:

nota = int(input("Ingrese una nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# Ejercicio 3:

numero = int(input("Ingrese un numero: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


# Ejercicio 4:

edad = int(input("Ingrese su edad: "))

if edad <= 12:
    print("Niño")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# Ejercicio 5:

contraseña = input("Ingrese una contraseña: ")
longitud = len(contraseña)

if longitud >= 8 and longitud <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese un contraseña de entre 8 y 14 caracteres.")


# Ejercicio 6

from statistics import mode, median, mean
import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 

if mean(numeros_aleatorios) > median(numeros_aleatorios) and median(numeros_aleatorios) > mode(numeros_aleatorios):
    print("Sesgo positivo")
elif mean(numeros_aleatorios) < median(numeros_aleatorios) and median(numeros_aleatorios) < mode(numeros_aleatorios):
    print("Sesgo negativo")
else:
    print("Sin sesgo")


#Ejercicio 7

frase = input("Ingrese una palabra o frase: ")

if frase[-1].lower() in ("a", "e", "i", "o", "u"):
    print(frase, "!")
else:
    print(frase)


# Ejercicio 8

nombre = input("Ingrese su nombre: ")
numero = int(input("Ingrese un numero: "))

nombre_mayuscula = nombre.upper()
nombre_minuscula = nombre.lower()
nombre_letra_mayuscula = nombre.title()

if numero == 1:
    print(nombre_mayuscula)
elif numero == 2:
    print(nombre_minuscula)
elif numero == 3:
    print(nombre_letra_mayuscula)


# Ejercicio 9

magnitud = int(input("Ingrese la magnitud de un terremoto: "))

if magnitud < 3:
    print( "Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte")
elif magnitud >= 7:
    print("Extremo")


# Ejercicio 10


hemisferio = input("Ingrese en que hemisfério se encuentra: ")
mes = input("Ingrese el mes:  ")
dia = int(input("Ingrese el día:  "))


# ===========NORTE===============

periodo_norte_diciembre = range(20,32)
periodo_norte_enero = range(1,32)
periodo_norte_febrero = range(1,28)
periodo_norte_marzo = range(1,21)


if hemisferio == "norte" and mes == ("diciembre") and dia in periodo_norte_diciembre:
    print("Invierno")
elif hemisferio == "norte" and mes == ("enero") and dia in periodo_norte_enero:
    print("Invierno")
elif hemisferio == "norte" and mes == ("febrero") and dia in periodo_norte_febrero:
    print("Invierno")
elif hemisferio == "norte" and mes == ("marzo") and dia in periodo_norte_marzo:
    print("Invierno")

periodo_norte_marzo = range(21, 32)
periodo_norte_abril = range(1,32)
periodo_norte_mayo = range(1,32)
periodo_norte_junio = range(1,21)

if hemisferio == "norte" and mes == ("marzo") and dia in periodo_norte_marzo:
    print("Primavera")
elif hemisferio == "norte" and mes == ("abril") and dia in periodo_norte_abril:
    print("Primavera")
elif hemisferio == "norte" and mes == ("mayo") and dia in periodo_norte_mayo:
    print("Primavera")
elif hemisferio == "norte" and mes == ("junio") and dia in periodo_norte_junio:
    print("Primavera")

periodo_norte_junio = range(21, 31)
periodo_norte_julio = range(1,31)
periodo_norte_agosto = range(1,32)
periodo_norte_septiembre = range(1,21)

if hemisferio == "norte" and mes == ("junio") and dia in periodo_norte_junio:
    print("Verano")
elif hemisferio == "norte" and mes == ("julio") and dia in periodo_norte_julio:
    print("Verano")
elif hemisferio == "norte" and mes == ("agosto") and dia in periodo_norte_agosto:
    print("Verano")
elif hemisferio == "norte" and mes == ("septiembre") and dia in periodo_norte_septiembre:
    print("Verano")

periodo_norte_septiembre = range(21, 31)
periodo_norte_octubre = range(1,31)
periodo_norte_noviembre = range(1,31)
periodo_norte_diciembre = range(1,21)

if hemisferio == "norte" and mes == ("septiembre") and dia in periodo_norte_septiembre:
    print("Otoño")
elif hemisferio == "norte" and mes == ("octubre") and dia in periodo_norte_octubre:
    print("Otoño")
elif hemisferio == "norte" and mes == ("noviembre") and dia in periodo_norte_noviembre:
    print("Otoño")
elif hemisferio == "norte" and mes == ("diciembre") and dia in periodo_norte_diciembre:
    print("Otoño")

# ===========SUR===============

periodo_sur_diciembre = range(20,32)
periodo_sur_enero = range(1,32)
periodo_sur_febrero = range(1,28)
periodo_sur_marzo = range(1,21)


if hemisferio == "sur"and mes == ("diciembre") and dia in periodo_sur_diciembre:
    print("Verano")
elif hemisferio == "sur" and mes == ("enero") and dia in periodo_sur_enero:
    print("Verano")
elif hemisferio == "sur" and mes == ("febrero") and dia in periodo_sur_febrero:
    print("Verano")
elif hemisferio == "sur" and mes == ("marzo") and dia in periodo_sur_marzo:
    print("Verano")

periodo_sur_marzo = range(21, 32)
periodo_sur_abril = range(1,32)
periodo_sur_mayo = range(1,32)
periodo_sur_junio = range(1,21)

if hemisferio == "sur" and mes == ("marzo") and dia in periodo_sur_marzo:
    print("Otoño")
elif hemisferio == "sur" and mes == ("abril") and dia in periodo_sur_abril:
    print("Otoño")
elif hemisferio == "sur" and mes == ("mayo") and dia in periodo_sur_mayo:
    print("Otoño")
elif hemisferio == "sur" and mes == ("junio") and dia in periodo_sur_junio:
    print("Otoño")

periodo_sur_junio = range(21, 31)
periodo_sur_julio = range(1,31)
periodo_sur_agosto = range(1,32)
periodo_sur_septiembre = range(1,21)

if hemisferio == "sur" and mes == ("junio") and dia in periodo_sur_junio:
    print("Invierno")
elif hemisferio == "sur" and mes == ("julio") and dia in periodo_sur_julio:
    print("Invierno")
elif hemisferio == "sur" and mes == ("agosto") and dia in periodo_sur_agosto:
    print("Invierno")
elif hemisferio == "sur" and mes == ("septiembre") and dia in periodo_sur_septiembre:
    print("Invierno")

periodo_sur_septiembre = range(21, 31)
periodo_sur_octubre = range(1,31)
periodo_sur_noviembre = range(1,31)
periodo_sur_diciembre = range(1,21)

if hemisferio == "sur" and mes == ("septiembre") and dia in periodo_sur_septiembre:
    print("Primavera")
elif hemisferio == "sur" and mes == ("octubre") and dia in periodo_sur_octubre:
    print("Primavera")
elif hemisferio == "sur" and mes == ("noviembre") and dia in periodo_sur_noviembre:
    print("Primavera")
elif hemisferio == "sur" and mes == ("diciembre") and dia in periodo_sur_diciembre:
    print("Primavera")