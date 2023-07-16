"""1 - Crear una funcion o procedimiento que pida como parametro un nombre
y que muestre en pantalla un saludo con el nombre pasado como argumento."""

def saludo():
    nombre = input("Ingrese su nombre -> ")
    return nombre
    
print(f"Hola {saludo()}, Bienvenido al programa.")
    

"""2 - Crear una funcion o procedimiento que pida una lista de numeros por parametro
y que muestre en pantalla, la suma de todos los numeros, el promedio,
el numero mas alto y el mas bajo."""

import random
lista = []
num = 0
cont = 0 
for num in range(10):
    num = random.randint(0, 100)
    cont += num
    lista.append(num)

print(lista)

def suma(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma

def promedio(lista):
    suma = 0
    prom = 0
    for i in range(len(lista)):
        suma += lista[i]
    prom = suma / len(lista)
    return prom

def Maxi(lista):
    mayor = 0
    for numero in lista:
        if numero>mayor:
            mayor=numero
    return mayor

def Mini(lista):
    menor = lista[9]
    for numero in lista:
        if numero<menor:
            menor=numero
    return menor

print(f"La suma de los valores de la lista es -> {suma(lista)}")
print(f"El valor promedio es -> {promedio(lista)}")
print(f"El valor mínimo encontrado es -> {Mini(lista)}")
print(f"El valor máximo encontrado es -> {Maxi(lista)}")    
