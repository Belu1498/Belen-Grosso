# Ejercicio 1:
# Crea una función recursiva que calcule el factorial de un número. 
# Luego, utiliza esa función para calcular y 
# mostrar en pantalla el factorial de todos los 
# números enteros entre 1 y el número que indique el usuario.

def num_factorial(num):

    if num == 0:
        return 1
    else: 
        return num_factorial(num - 1) * num

# Invocando funcion recursiva

from Trabajo_Practico_N7_Belen_Grosso import num_factorial

num = int(input("Ingrese un numero: "))

for i in range(num):
    if num >= 1:
        i = i + 1
        print(f"El factorial de {i} es: {num_factorial(i)}")

# ------------------------------

# Ejercicio 2:
# Crea una función recursiva que calcule el valor de la 
# serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la 
# posición que el usuario especifique.

def fibonacci_recursivo(posicion):
    
    if posicion==0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recursivo(posicion-1) + fibonacci_recursivo(posicion-2)

# Invocando funcion recursiva 

from Trabajo_Practico_N7_Belen_Grosso import fibonacci_recursivo

num = int(input("Ingrese un numero: "))

for i in range (num):
    i = i + 1
    print(f"Posicion {i}: {fibonacci_recursivo(i)}")


# --------------------------------

# Ejercicio 3:
# Crea una función recursiva que calcule la potencia de un número base 
# elevado a un exponente, utilizando la fórmula 𝑛**𝑚= 𝑛∗𝑛**(𝑚−1). 
# Prueba esta función en un algoritmo general.

def potencia(num_base,exponente):

    if exponente == 0:
        return 1
    else: 
        return num_base* potencia(num_base, exponente - 1)
    
# Invocando funcion recursiva 

from Trabajo_Practico_N7_Belen_Grosso import potencia

num_base = int(input("Ingrese un numero base: "))
exponente = int(input("Ingrese un exponente: "))

print(potencia(num_base,exponente))

# ---------------------------------

# Ejercicio 4:
# Crear una función recursiva en Python que reciba un número entero 
# positivo en base decimal y devuelva su representación en binario 
# como una cadena de texto.

def binario(decimal):

    if decimal == 0:
        return ""
    elif decimal > 0:
        return binario(decimal // 2) + str(decimal % 2)
    
# Invocando funcion 

from Trabajo_Practico_N7_Belen_Grosso import binario

decimal = int(input("Ingrese un numero entero positivo: "))

print(binario(decimal))

# ---------------------------------

# Ejercicio 5:
# Implementá una función recursiva llamada es_palindromo(palabra) 
# que reciba una cadena de texto sin espacios ni tildes, y devuelva 
# True si es un palíndromo o False si no lo es.

def es_palindromo(palabra):

    if len(palabra) <= 1:
        return True
    elif palabra[0] == palabra [-1]:
        return es_palindromo(palabra[1:-1])
    else:
        palabra[0] != palabra[-1]
        return False
    
# Invocanco funcion

from Trabajo_Practico_N7_Belen_Grosso import es_palindromo

palabra = input("Ingrese una palabra: ")

print(es_palindromo(palabra))

# ---------------------------------

# Ejercicio 6:
# Escribí una función recursiva en Python llamada suma_digitos(n) 
# que reciba un número entero positivo y devuelva la suma de todos 
# sus dígitos.

def suma_digitos(n):

    if n == 0:
        return 0
    elif n > 0:
        digito = n % 10
        n //= 10
        return digito + suma_digitos(n)
    
# Invocanco funcion

from Trabajo_Practico_N7_Belen_Grosso import suma_digitos

n = int(input("Ingrese un numero: "))

print(suma_digitos(n))


# ---------------------------------

# Ejercicio 7:
# Un niño está construyendo una pirámide con bloques. 
# En el nivel más bajo coloca n bloques, en el siguiente 
# nivel uno menos (n - 1), y así sucesivamente hasta 
# llegar al último nivel con un solo bloque.

def contar_bloques(n):


    if n == 1:
        return 1
    else: 
        return contar_bloques(n - 1) + n
    
# Invocanco funcion
    
from Trabajo_Practico_N7_Belen_Grosso import contar_bloques

n = int(input("Ingrese cantidad de bloques: "))

print(f"El total de bloques son: {contar_bloques(n)}")

# ---------------------------------

# Ejercicio 8:
# Escribí una función recursiva llamada 
# contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito 
# (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.

def contar_digito(numero, digito):


    if numero == 0 and digito == 0:
        return 1
    elif numero == 0 and digito != 0:
        return 0
    else:
        digito_por_digito = numero % 10 
        numero //= 10
        return (digito_por_digito == digito) + contar_digito(numero, digito)
    
# Invocanco funcion
        
from Trabajo_Practico_N7_Belen_Grosso import contar_digito

print(contar_digito(12548966544744, 4))